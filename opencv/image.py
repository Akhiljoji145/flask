import cv2
img=cv2.imread('car.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(20000)
cv2.imwrite('img',img)
cv2.destroyAllWindows()