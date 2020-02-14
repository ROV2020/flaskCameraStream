import numpy as np
import cv2
import os

class Camera:
    __brake__=False
    camIndex=0

    #init and open camera
    def __init__(self,camIndex=0):
        self.camIndex=camIndex
        self.cap = cv2.VideoCapture(self.camIndex)
        self.isOpened=self.cap.isOpened()
        if not (self.cap.isOpened()):
            print("Could not open video device")
        
    def captureVideo(self):
        #loop only if camera is opend
        while(True and self.cap.isOpened()):
            # Capture frame-by-frame
            self.ret, self.frame = self.cap.read()

            # Display the resulting frame
            cv2.imshow('frame',gray)

            #return frame
            yield self.frame
            if(self.__brake__):
                self.__brake__=False
                break

        if not (self.cap.isOpened()):
            print("Could not open video device")
    
    #stop video forever don't use it till the end
    def stopVideo(self):
        self.__brake__=True
        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()
    
    #Use it to stop temporarly 
    def pauseVideo(self):
        self.__brake__=True

    #
    def resumeVideo(self):
        self.__brake__=False
        self.captureVideo()

    #see all available camera
    def listCameras(self):  
        print(os.system("v4l2-ctl --list-devices"))
        return os.system("v4l2-ctl --list-devices")

