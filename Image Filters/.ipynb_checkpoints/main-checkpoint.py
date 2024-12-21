import cv2 


# Reads the image
img = cv2.imread("Image/Dog.jpg")

#Display the image (Image have too high resolution u wont be able to see the full image because it dont fit the window)
cv2.imshow("Display Window",img)
cv2.waitKey(0)

#Resize the display window having 500 height and 500 width
imgS = cv2.resize(img, (500,500))
cv2.imshow("Resize Display Window",imgS)
cv2.waitKey(0)
