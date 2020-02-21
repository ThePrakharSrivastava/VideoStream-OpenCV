import cv2
import sys

mycamera = cv2.VideoCapture(0)

if mycamera.isOpened == False:
    print("error in opening the camera ")
    sys.exit

while(mycamera.isOpened()):

    print("camera is open-----")

    ret, frame  =mycamera.read()

    if ret == True:

        print("starting camera-------")
        cv2.imshow('myframe', frame)

        #press a to stop recording
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
            print("exiting the video stream")