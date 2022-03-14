# Importing libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

# A function called showimage  for showing the images
def showimage(img):
	plt.imshow(img, cmap="gray")
	plt.axis('off')
	plt.style.use('seaborn')
	plt.show()

# Reading an image using OpenCV --> OpenCV reads images by default in BGR format
image = cv2.imread("img.jpg")

# Converting BGR image into a RGB image
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show the original image
showimage(image)

# Haar cascades are machine learning object detection algorithms.
detect_face = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt.xml')
result = detect_face.detectMultiScale(image, 1.2, 1) # return number
# print(result)  # saved in x y w h 

# Draw rectangle around the faces which is in ( saved in x y w h ) region of interest (ROI)
for (x, y, w, h) in result:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) # bulid rectangle 
	roi = image[y:y+h, x:x+w]
	# applying a gaussian blur over this new rectangle area
	roi = cv2.GaussianBlur(roi, (23, 23), 30)
	# put the  blurred image on original image to get final image
	image[y:y+roi.shape[0], x:x+roi.shape[1]] = roi
    
# get the output
showimage(image)



