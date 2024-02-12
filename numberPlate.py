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

#Find the contours based on the image
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#Here cnts is contours which means that it is like the curve joining all the contour points
#new is hierarchy - relationship
#RETR_LIST- it retrieves all the contours but doesn't create any parent-child relationship
#CHAIN_APPROX_SIMPLE - it removes all the redundant points and compress the contour by saving memory


#Create a copy of our original image to draw all the contours

image1 = image.copy()
cv2.drawContours(image1, cnts, -1, (0,255,0), 3) #this values are fixed ## to draw all the contours in an image
cv2.imshow('Canny after contouring', image1)
cv2.waitKey(0)


