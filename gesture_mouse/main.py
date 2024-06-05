# Mouse Using Computer Vision
import os
import sys
import cv2
import numpy as np
import pyautogui
import keyboard
import time
import autopy
import mouse
from pynput.mouse import Controller

# Add parent directory to path to enable package execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gesture_mouse.utils.hand_tracking import handDetector

mous = Controller()
wCam, hCam = 1280, 720
frameR = 50
smoothening = 5

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        
    fingers = detector.fingersUp()
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
    
    if fingers[1] == 1 and fingers[2] == fingers[3] == fingers[4] == fingers[0] == 0:
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening
        autopy.mouse.move(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY

    if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == fingers[4] == fingers[0] == 0:
        length, img, lineInfo = detector.findDistance(8, 12, img)
        if length < 50:
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 10, (0, 255, 0), cv2.FILLED)
            mouse.click('left')

    if fingers[0] == 1 and fingers[1] == 1 and fingers[3] == fingers[4] == fingers[2] == 0:
        length, img, lineInfo = detector.findDistance(4, 8, img)
        if length > 30 and length < 120:
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 10, (0, 255, 0), cv2.FILLED)
            pyautogui.keyDown('ctrl')
            mous.scroll(0, 0.6)
            pyautogui.keyUp('ctrl')
        if length > 120 and length < 200:
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 10, (0, 255, 0), cv2.FILLED)
            pyautogui.keyDown('ctrl')
            mous.scroll(0, -0.6)
            pyautogui.keyUp('ctrl')

    if detector.allFingersClosed():
        mous.scroll(0, 1)
    if detector.fingersUp() == [1, 0, 0, 0, 0]:
        mous.scroll(0, -1)
    if detector.fingersUp() == [0, 0, 0, 0, 1]:
        mouse.click('right')
    if detector.fingersUp() == [0, 1, 0, 0, 1]:
        mous.scroll(1, 0)
    if detector.fingersUp() == [1, 1, 0, 0, 1]:
        mous.scroll(-1, 0)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.imshow("Image", img)
    if cv2.waitKey(1) and keyboard.is_pressed("f2"):
        break
