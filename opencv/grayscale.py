import cv2

# Load the image
image = cv2.imread('bmw-drifting-1366x768.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('car1.jpg', gray_image)

# Display the original and grayscale images (optional)
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()
