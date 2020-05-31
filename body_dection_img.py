import cv2
fullbody_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_fullbody.xml")
upperbody_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_upperbody.xml")

img = cv2.imread("./img/img4.jpg")

body_cascade = upperbody_cascade

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
body = body_cascade.detectMultiScale(gray_img)
for (x,y,w,h) in body:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray_img[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]

resize_img = cv2.resize(img,(int(img.shape[1]/8),int(img.shape[0]/4)))
# cv2.imshow('img',resize_img)
cv2.imshow('img',resize_img)
k = cv2.waitKey(10000) & 0xff    


cv2.destroyAllWindows()