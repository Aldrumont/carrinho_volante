import threading
from threading import Thread
from simulador_camera import *
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

instancia = MyOutput()
def mqtt_loop():
    frame = record(instancia)
    logging.debug(str(frame)+' \r')
    print(8)
while 1:
    print(instancia.frame)


thread_mqtt_loop = threading.Thread(name='mqtt_loop', target=mqtt_loop)
thread_mqtt_loop.start()