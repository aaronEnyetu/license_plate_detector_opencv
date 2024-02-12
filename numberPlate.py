import cv2
import imutils # to resize the image
import pytesseract 


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#now to read the image file
image = cv2.imread('plate2.jpg')

#Resize and standardize the image to 500

image = imutils.resize(image, width = 500)


#Display original image
cv2.imshow('Original Image', image) #here the Original Image is th name of window /// you can give your own suitable name
cv2.waitKey(0) #till i press anything it will not execute further


# NOW Here, convert image to gray scale
# This is done because it will reduce the dimension, also reduces complexity of image
# and yeah there are few algorithms like canny, etc which only works on grayscale images

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Scale Image', gray)
cv2.waitKey(0)


#now the noise will be reduced from the image and make it smooth
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow('Smoother Image', gray)
cv2.waitKey(0)


#Find the edges of the images

edged = cv2.Canny(gray, 170, 200)
cv2.imshow('Canny Edge', edged)
cv2.waitKey(0)


