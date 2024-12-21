import cv2 
import matplotlib.pyplot as plt

# Reads the image
img = cv2.imread("Image/Dog.jpg")

# Display the image (Image have too high resolution u wont be able to see the full image because it dont fit the window)
# cv2.imshow("Display Window",img)
# cv2.waitKey(0)

# Resize the display window having 500 height and 500 width
imgS = cv2.resize(img, (500,500))
cv2.imshow("Resize Display Window",imgS)
cv2.waitKey(0)


# Opencv reads the image in BGR format i.e (Blue, Green, Red). Whenever you read the image using cv2.imread() and show using cv2.imshow()
# they both work with BGR format so you will not see the difference. But when you read the image using opencv and display using the
# matplotlib plt.imshow() you can see the image output in BGR format. 

# Using plt figure to display the image
plt.figure()
plt.imshow(imgS)
plt.show()

#Convert the image to Grayscale (Black and White)
grayscale_img = cv2.cvtColor(imgS, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", grayscale_img)
cv2.waitKey(0)

# Blurring the image using the Box Filter
box_blur = cv2.boxFilter(imgS, -1, (5,5))
cv2.imshow("Box Blur", box_blur)
cv2.waitKey(0)


# Blurring the image using Gaussian Blur
blur_img = cv2.GaussianBlur(imgS, (15,15), 0)
cv2.imshow("Gaussian Blur Image", blur_img)
cv2.waitKey(0)

# Apply edge detection
edge_img = cv2.Canny(grayscale_img, 255/3, 255) # lower threshold and higher threshold. Edges Intensity higher than max threshold 
# are considered sure edges while edges lower than min threshold are considered non edges, edges whose connected with the sure edges
# are considered to be an edge.
cv2.imshow("Canny Edge Detection", edge_img)
cv2.waitKey(0)

