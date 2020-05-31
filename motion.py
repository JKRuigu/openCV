import cv2,imutils,time,math,random
import numpy as np

cap = cv2.VideoCapture("D:\\jk\\Video\\programming\\PYTHON\\Visual\\y2mate.com - Intro to Data Analysis Visualization with Python, Matplotlib and Pandas Matplotlib Tutorial_a9UrKTVEeZA_1080p.MP4")

ret,frame = cap.read()
ret,frame2 = cap.read()
text = 'Unoccupied'
times = []
timesText = []
status_list = [None,None]
first_frame = None
red = 0
green = 255
print(ret)
# frame2 = imutils.resize(frame2, width=500)

while ret:
	text = 'Unoccupied'
	green = 0
	red = 255
	status = 0
	timer = cv2.getTickCount()
	
	# print(time.time())

	diff = cv2.absdiff(frame,frame2)	
	gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	_,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

	dilate_image = cv2.dilate(thresh,None,iterations=2)

	if first_frame is None:
		first_frame = frame
		continue

	cnts,_ = cv2.findContours(dilate_image.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.putText(frame,"objects: {}".format(len(cnts)),(5,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)

	text = f"Unoccupied"

	for cnt in cnts:
		(x,y,w,h) = cv2.boundingRect(cnt)
		if cv2.contourArea(cnt) > 20000:
			print(len(cnts))
			text = 'Occupied'
			red = 0
			green = 255
			status =1
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
			continue
	
	status_list.append(status)
	status_list = status_list[-2:]

	# if status_list[-1] == 1 and status_list[-2] == 0:
		# times.append(datetime.now())
		# print("Start:",time.time())
	# if status_list[-1] == 0 and status_list[-2] == 1:
		# times.append(datetime.now())
		# print("End:",time.time())

	cv2.putText(frame,"Status: {}".format(text),(5,110),cv2.FONT_HERSHEY_SIMPLEX,2,(0,green,red),3)
	cv2.imshow("motion",imutils.resize(frame, width=500))

	frame =frame2
	ret,frame2 = cap.read()

	if cv2.waitKey(40) == 27:
		break

cv2.destroyAllWindows()
cap.release()