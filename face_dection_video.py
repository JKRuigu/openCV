import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_eye.xml")

cap = cv2.VideoCapture('./video/4.3GP')
ret,img = cap.read()
facesNumber = 0

while ret:
	gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray_img)
	for (x,y,w,h) in faces:
	    facesNumber = faces.size
	    if faces.size <= 4:
		    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		    cv2.putText(img,"{},{}".format(x,y),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
		    roi_gray = gray_img[y:y+h,x:x+w]
		    roi_color = img[y:y+h,x:x+w]

		    eyes = eye_cascade.detectMultiScale(roi_gray)


		    for (ex,ey,ew,eh) in eyes:
		    	if eyes.size <= 8:
		    		cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,255,0), 2)	    		
		    		pass	    		
	    	# cv2.putText(roi_color,"{},{}".format(ex,ey),(ex,ey),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
	    pass

	resize_img = cv2.resize(img,(int(img.shape[1]/1.5),int(img.shape[0]/1.2)))
	print()
	cv2.putText(img,"faces: {}".format(facesNumber/4),(5,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,105,255),2)
	cv2.imshow('img',resize_img)

	k = cv2.waitKey(5) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()