import cv2 as cv
import numpy as np

"""
What is Image Transformation ?

Image transformation means changing the position, size, or orientation of an image.
Instead of changing the pixels themselves, we change where the pixels appear in the image 
plane.

Common image transformations in OpenCV:

Transformation	                Meaning
====================================================
Translation	                    Move image left/right/up/down
Rotation	                    Rotate image
Scaling	                        Resize image
Affine transformation	        Combination of rotation, translation, scaling
Perspective transformation	    Change viewing angle
"""

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#x > 0	move right
#x < 0	move left
#y > 0	move down
#y < 0	move up

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

img1=cv.imread("D:/pythontrail1/images/Cote-dAzur.jpg")
cv.imshow("France",img1)

translated=translate(img1,-100,-100)
cv.imshow("Translated",translated)

rotated=rotate(img1,60)
cv.imshow("Rotated",rotated)

rotated_rotated=rotate(rotated,-90 )
cv.imshow("Rotated_Rotated",rotated_rotated)

cv.waitKey(0)