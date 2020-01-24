import os
import time

cmd = "raspistill -p 1000,50,640,480 -t 1 -ISO 400 -ss 750000 -e png -set -awb off -awbg 1.5,1.2 -ag 1.5,1.2 -dg 1.0,1.0 -w 640 -h 480 -o timelapse_0.png"
init = time.time()
for i in range(1):
	os.system(cmd)
print(time.time()-init)
