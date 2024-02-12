import cv2
import imutils # to resize the image
import pytesseract 


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#now to read the image file
image = cv2.imread('plate1.jpg')

#Resize and standardize the image to 500

image = imutils.resize(image, width = 500)


#Display original image
cv2.imshow('Original Image', image) #here the Original Image is th name of window /// you can give your own suitable name
cv2.waitKey(0) #till i press anything it will not execute further
