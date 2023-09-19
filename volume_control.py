import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from send_value import ArduinoController

#######################
wCam, hCam = 640, 480
#######################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=1)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400 

arduino = ArduinoController('COM3', 9600)  # Replace 'COMX' with the correct serial port
arduino.connect()
luce_accendere_old = 0

def num_led(vol):
    if vol >= 0 and vol < 0.25:
        return 0
    elif vol >= 0.25 and vol < 0.5:
        return 1
    elif vol >= 0.5 and vol < 0.75:
        return 2
    elif vol >= 0.75 and vol < 1:
        return 3
    else:
        return 4

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 15, (255, 203, 153), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 203, 153), cv2.FILLED)
        cv2.line(img, (x1,y1),(x2,y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 203, 153), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
    
        vol = np.interp(length, [35, 270], [0, 1])
        print(vol)
        volBar = np.interp(length, [35, 270], [400, 150])

        volume.SetMasterVolumeLevelScalar(vol, None)

        luce_accendere = num_led(vol)

        if luce_accendere_old != luce_accendere:
            arduino.send_value(luce_accendere)
            luce_accendere_old = luce_accendere

        if length<50:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    imgflip = cv2.flip(img, 1)
    cv2.imshow("Img", imgflip)
    cv2.waitKey(1)
    key = cv2.waitKey(5)

    if key == 27:  # Esc key to exit the loop
        break

arduino.disconnect()
cap.release()
cv2.destroyAllWindows()