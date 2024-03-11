import cv2
img=cv2.imread('images.jpg',1)
cv2.rectangle(img,(1,1),(223,223),(240,0,0),5)
cv2.circle(img,(15,15),7,(0,0,240),-1)
cv2.circle(img,(15,210),7,(0,0,240),-1)
cv2.circle(img,(210,15),7,(0,0,240),-1)
cv2.circle(img,(210,210),7,(0,0,240),-1)
cv2.rectangle(img,(50,60),(180,160),(0,240,0),5)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'hello',(75,120),font,1,(0,0,0))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()