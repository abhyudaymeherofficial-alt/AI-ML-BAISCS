import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)


img1=cv.imread("D:/pythontrail1/images/cat3.jpg")
img1_rescale=rescaleFrame(img1,0.5)
cv.imshow("Cat",img1_rescale)

#converting to greyscale
gray=cv.cvtColor(img1_rescale,cv.COLOR_BGR2GRAY)
cv.imshow("Cat GREY",gray)

#BLUR
blur=cv.GaussianBlur(img1_rescale,(5,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

#EDGE CASCADE
canny=cv.Canny(img1_rescale,125,175)
cv.imshow("Canny edge",canny)

cannyblur=cv.Canny(blur,125,175)
cv.imshow("Canny edge blur",cannyblur)

# Dilated the image

# What Dilation Does ?
# Dilation increases the thickness of white regions (edges or objects) in an image.
# So if you apply it to a Canny edge image, the edges become thicker and more visible.

dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow("Dilated",dilated)

dilatedblur=cv.dilate(cannyblur,(3,3),iterations=1)
cv.imshow("DilatedBlur",dilatedblur)

# Eroding
#What Erosion Does ??
#Erosion shrinks the white regions (objects/edges) in an image.
#If dilation makes edges thicker, erosion does the opposite.

eroded=cv.erode(dilatedblur,(3,3),iterations=3)
cv.imshow("Eroded",eroded)

# Resize
resized=cv.resize(img1_rescale,(200,200),interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resized)

# Cropping
cropped=img1_rescale[100:250,200:400]
cv.imshow("Cropped",cropped)

cv.waitKey(0)