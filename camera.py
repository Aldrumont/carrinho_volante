import picamera
import numpy as np
import cv2 
# from rasp_side import *

class MyOutput(object):
    def __init__(self):
        self.frame = 0
        self.img = None
        f = open('data_frames/data.csv','w')
        f.write('frame,acelerador,freio,angulo\n') #Give your csv text here.
        f.close()
    def write(self, s):
        print("frame",self.frame)
        height = 480
        width = 640
        channels = 3
        img = np.fromstring(s, dtype=np.uint8).reshape(height,width,channels)#altura,largura
        img = np.rot90(img)
        self.img = np.rot90(img)
        self.frame += 1
    def register(self,values):
        cv2.imwrite('data_frames/frame_{}.jpg'.format(self.frame), self.img)
        f = open('data.csv','a')
        f.write('{},{},{},{}\n'.format(self.frame,values["Acelerador"],values["freio"],values["angulo"])) #Give your csv text here.
        f.close()
        print("Salvo o frame: ", self.frame)
    
    def flush(self):
        # print(self.frame)
        pass

def record():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 60
        camera.start_recording(MyOutput(), format='bgr')
        camera.wait_recording(500)
        camera.stop_recording()

if __name__ == '__main__':
    cam = MyOutput()
    cam.record()