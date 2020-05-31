import cv2
fullbody_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_fullbody.xml")
upperbody_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_upperbody.xml")

cap = cv2.VideoCapture('./video/2.MP4')
bodyNumber = 0
ret,img = cap.read()

body_cascade = upperbody_cascade

while ret:
	gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	body = body_cascade.detectMultiScale(gray_img)
	for (x,y,w,h) in body:
	    bodyNumber = body.size
	    if body.size <= 4:
		    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		    cv2.putText(img,"{},{}".format(x,y),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
		    roi_gray = gray_img[y:y+h,x:x+w]
		    roi_color = img[y:y+h,x:x+w]
	    pass

	resize_img = cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/2)))
	print()
	cv2.putText(img,"bodys: {}".format(bodyNumber/4),(5,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,105,255),2)
	cv2.imshow('img',resize_img)

	k = cv2.waitKey(5) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()