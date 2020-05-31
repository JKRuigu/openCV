import cv2
face_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_eye.xml")

img = cv2.imread("img2.jpg")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,1.03,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray_img[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
    	cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
    
resize_img = cv2.resize(img,(int(img.shape[1]/8),int(img.shape[0]/4)))
# cv2.imshow('img',resize_img)
cv2.imshow('img',img)
k = cv2.waitKey(10000) & 0xff    


cv2.destroyAllWindows()