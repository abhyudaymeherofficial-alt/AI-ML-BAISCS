import cv2 as cv

#reading images
img1=cv.imread("D:/pythontrail1/images/img.png")
cv.imshow("Cat",img1)

img2=cv.imread("D:/pythontrail1/images/Cute-Cat-Wallpaper-HD.jpg")
cv.imshow("Cat2",img2)
cv.waitKey(0)


#reading videos
#capture=cv.VideoCapture(0) for web cam
capture=cv.VideoCapture("D:/pythontrail1/images/catvid.mp4")
while True:
    isTrue,frame=capture.read()
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()




#   Resizing video and photos

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

def changeRes(capture,width,height):
    capture.set(3,width)
    capture.set(4,height)


capture=cv.VideoCapture("D:/pythontrail1/images/catvid.mp4")
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame,0.53789)
    cv.imshow("Video resized",frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()



# Webcam
capture=cv.VideoCapture(0)
changeRes(capture,300,400)
while True:
    isTrue,frame=capture.read()
    cv.imshow("Video live resized",frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


#DRAWING SHAPE

import numpy as np

img2=cv.imread("D:/pythontrail1/images/Cute-Cat-Wallpaper-HD.jpg")
cv.imshow("Cat2",img2)

blank=np.zeros((500,500,3),dtype="uint8")
cv.imshow("Blank",blank)

blank[200:300,300:400]=0,255,0
cv.imshow("Green",blank)

#cv.rectangle(blank,(50,50),(250,450),(0,255,0),thickness=cv.FILLED)
cv.rectangle(blank,(50,50),(250,450),(0,255,0),thickness=2)
cv.imshow("Rectangle",blank)

cv.rectangle(img2,(50,50),(250,250),(0,255,0),thickness=2)
cv.imshow("CAT Rectangle",img2)

blank2=np.zeros((500,500,3),dtype="uint8")
cv.rectangle(blank2,(0,0),(blank2.shape[1]//2,blank2.shape[0]//2),(0,255,0),
             thickness=-1)
cv.circle(blank2,(blank2.shape[1]//2,blank2.shape[0]//2),40,(0,0,255),
          thickness=3)
cv.line(blank2,(0,0),(blank2.shape[1]//2,blank2.shape[0]//2),(200,20,30),thickness=3)
cv.imshow("row->0 col->1",blank2)
#row->0 col->1
cv.waitKey(0)

# write text
img3=cv.imread("D:/pythontrail1/images/Cote-dAzur.jpg")
cv.putText(img3,"France",(25,25),cv.FONT_ITALIC,1.0,(100,235,30),2)
cv.imshow("Côte_dAzur",img3)

cv.waitKey(0)
