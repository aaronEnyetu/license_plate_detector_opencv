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

#Not all the contours are needed, only the ones on the number plate
#But can't directly locate them so sorting them on the basis of their areas
#Selecting those areas which are maximum so will select top 30 areas
#For that the order of sorting will be reversed



cnts = sorted(cnts, key = cv2.contourArea, reverse= True)[:30]
NumberPlateCount = None


#Currently there are no contours||it will show how many number plates are there in the image
#To draw top 30 contours- make a copy of the original image and use
#use because there will be no need to edit anything on the original image


image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0,255,0),3)
cv2.imshow('Top 30 Contours', image2)
cv2.waitKey(0)


#Run a For loop on the contours to find the best possible contour of the number plate
count = 0
name = 1 #name of the image(cropped image)


for i in cnts:
    perimeter = cv2.arcLength(i, True)
    #perimeter is also called as archLength and it can be found directly in python using archLength function

    approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)
    #approxPolyDp is used because it approximates the curve of polygon with the precision

    if(len(approx)==4): #4 means it has 4 corners which will be most probably be the number plate and it also has 4 corners
        NumberPlateCount = approx

        #Now crop that rectangle part

        x, y, w, h = cv2.boundingRect(i)
        crp_img = image[y:y+h, x:x+w]


            ###############################
            #                             #
 #(y+h)     #                             # Lets suppose this is the figure with 4 corners
            #                             #
            ###############################
        #(x,y)             ---(x+w)------->
        #this much part will be cropped

        cv2.imwrite(str(name) + '.jpg', crp_img)

        break
    #Draw contour in the main image that has been identified as a number plate
    cv2.drawContours(image, [NumberPlateCount], -1, (0,255,0), 3)
    cv2.imshow('Final Image', image)
    cv2.waitKey(0)
    
