import cv2
import numpy as np
import os
import handtracker as htm 

brushThickness = 25
eraserThickness = 100
folderpath = "Images"

imgList = os.listdir(folderpath)
overlayList = []
for imgPath in imgList:
    image = cv2.imread(f'{folderpath}/{imgPath}')
    image = cv2.resize(image, (1280, 125))
    overlayList.append(image)
    
header = overlayList[1]
drawColor = (255, 50, 50)
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.85)
xp,yp = 0,0
imgCanvas = np.zeros((720,1280,3),np.uint8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if lmList:
        if len(lmList) > 12:
            x1, y1 = lmList[8][1:]  # Index finger
            x2, y2 = lmList[12][1:]  # Middle finger

            finger = detector.fingersUp()
        else:
            print("Not enough landmarks detected")


        if finger[1] and finger[2] and finger[3]==False and finger[4]==False:
            xp, yp = 0, 0
            if y1 < 125:
                if 0 < x1 < 200:
                    imgCanvas = np.zeros((720,1280,3),np.uint8)
                elif 200 < x1 < 300:
                    if 0 < y1 < 60:
                        brushThickness = 15
                    else:
                        brushThickness = 25
                elif 300 < x1 < 550:                        
                    header = overlayList[0]
                    drawColor = (0, 0, 255)
                elif 551 < x1 < 800:
                    header = overlayList[1]
                    drawColor = (255, 50, 50)
                elif 801 < x1 < 1050:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                elif 1051 < x1 < 1200:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)
            # cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)


        if finger[1] and finger[2]==False and finger[3]==False and finger[4]==False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)

            else:
                if y1 > 145:
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
            xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)        

    img[0:125, 0:1280] = header
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img,imgInv)
    img = cv2.bitwise_or(img,imgCanvas)

    cv2.imshow("Image", img)
    # cv2.imshow("Image Canvas", imgCanvas)
    # cv2.imshow("Image Inverse", imgInv)
    cv2.waitKey(1)  