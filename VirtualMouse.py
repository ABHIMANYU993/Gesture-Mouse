# Mouse Using Computer Vision
import cv2
import numpy as np
import pyautogui
import keyboard
import HandFunctions as hf
import time
import autopy
import mouse
from pynput.mouse import Controller

mous = Controller()
##########################
wCam, hCam = 1280, 720
frameR = 50  # Frame Reduction
smoothening = 5
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = hf.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
print(wScr, hScr)

while True:
    #  Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    #  Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

    #  Check which fingers are up
    fingers = detector.fingersUp()
    # print(fingers)
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                  (255, 0, 255), 2)
    #  Only Index Finger : Moving Mode
    if fingers[1] == 1 and fingers[2] == fingers[3] == fingers[4] == fingers[0] == 0:
        #  Convert Coordinates
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        #  Smoothen Values
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        # Move Mouse
        autopy.mouse.move(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY

    # Both Index and middle fingers are up : Clicking Mode
    if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == fingers[4] == fingers[0] == 0:
        #  Find distance between fingers
        length, img, lineInfo = detector.findDistance(8, 12, img)
        print(length)
        #  Click mouse if distance short
        if length < 50:
            cv2.circle(img, (lineInfo[4], lineInfo[5]),
                       10, (0, 255, 0), cv2.FILLED)
            mouse.click('left')  # Left Click

    # Both Index and Thumb fingers are up : Zooming Mode
    if fingers[0] == 1 and fingers[1] == 1 and fingers[3] == fingers[4] == fingers[2] == 0:
        #  Find distance between fingers
        length, img, lineInfo = detector.findDistance(4, 8, img)
        print(length)

        #  Scroll mouse if distance short By Holding CTRL On Keyboard
        if length > 30 and length < 120:
            cv2.circle(img, (lineInfo[4], lineInfo[5]),
                       10, (0, 255, 0), cv2.FILLED)
            pyautogui.keyDown('ctrl')
            mous.scroll(0, 0.6) # Zoom In
            pyautogui.keyUp('ctrl')
        if length > 120 and length < 200:
            cv2.circle(img, (lineInfo[4], lineInfo[5]),
                       10, (0, 255, 0), cv2.FILLED)
            pyautogui.keyDown('ctrl')
            mous.scroll(0,-0.6) # Zoom Out
            pyautogui.keyUp('ctrl')

    # Check All Fingers Are Closed:
    if detector.allFingersClosed():
        mous.scroll(0, 1)  # Scroll up
    #  Check Thumb Finger is Open:
    if detector.fingersUp() == [1, 0, 0, 0, 0]:
        mous.scroll(0, -1)  # Scroll down
    #  Check Pinky Finger is Open:
    if detector.fingersUp() == [0, 0, 0, 0, 1]:
        mouse.click('right')  # Right Click
    #  Check Pinky And Index Fingers Are Open:
    if detector.fingersUp() == [0, 1, 0, 0, 1]:
        mous.scroll(1, 0)  # Scroll Right
    #  Check Pinky And Index And Thumb Fingers Are Open:
    if detector.fingersUp() == [1, 1, 0, 0, 1]:
        mous.scroll(-1, 0)  # Scroll Left
    #  Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # To dispaly fps un-comment the below line
    # cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    #             (255, 0, 0), 3)

    #  Display
    cv2.imshow("Image", img)

    # Exit the loop on 'F2' key press
    if cv2.waitKey(1) and keyboard.is_pressed("f2"):
        break
