import picamera
import numpy as np
import cv2 
import threading
import queue

q=queue.Queue()
# from rasp_side import *
def take_picture(values):
    print("apertou")
    print(999,values)
    q.put(values)

class MyOutput(object):
    def __init__(self,q):
        self.q = q
        self.frame = 0
        self.img = None
        f = open('data_frames/data.csv','w')
        f.write('frame,acelerador,freio,angulo\n') #Give your csv text here.
        f.close()
        self.thread_read_queue = threading.Thread(name='thread_read_queue', target=self.thread_read_queue)
        self.thread_read_queue.start()
    def write(self, s):
        # print("frame",self.frame)
        height = 480
        width = 640
        channels = 3
        img = np.fromstring(s, dtype=np.uint8).reshape(height,width,channels)#altura,largura
        img = np.rot90(img)
        self.img = np.rot90(img)
        self.frame += 1
    def register(self,values):
        cv2.imwrite('data_frames/frame_{}.jpg'.format(self.frame), self.img)
        f = open('data_frames/data.csv','a')
        f.write('{},{},{},{}\n'.format(self.frame,values["Acelerador"],values["freio"],values["angulo"])) #Give your csv text here.
        f.close()
        pass
    def thread_read_queue(self):
        while True:
            item = self.q.get()
            if item is None:
                break
            self.register(item)
            print("Salvo o frame: ", self.frame)
            self.q.task_done()
    def flush(self):
        # print(self.frame)
        pass

def record():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 60
        camera.start_recording(MyOutput(q), format='bgr')
        camera.wait_recording(500)
        camera.stop_recording()

# print("NICEEEEE")



if __name__ == '__main__':
    cam = MyOutput()
    cam.record()