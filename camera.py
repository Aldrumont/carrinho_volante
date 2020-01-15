import picamera
import numpy as np
import cv2 
from rasp_side import *

print(output_values)

class MyOutput(object):
    def __init__(self):
        self.frame = 0

    def write(self, s):
        height = 480
        width = 640
        channels = 3
        img = np.fromstring(s, dtype=np.uint8).reshape(height,width,channels)#altura,largura
        img = np.rot90(img)
        img = np.rot90(img)
        cv2.imwrite('frames/frame_{}.jpg'.format(self.frame), img)
        # print(self.frame)
        self.frame += 1
    
    def flush(self):
        # print(self.frame)
        pass

    def record(a):
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.framerate = 60
            camera.start_recording(MyOutput(), format='bgr')
            camera.wait_recording(500)
            camera.stop_recording()

cam = MyOutput()
cam.record()