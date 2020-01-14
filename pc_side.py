import logging
import threading
import time
from jstest import JSTest
import json
import paho.mqtt.client as paho

broker="localhost"
topic = "test"
port=1883

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
def on_publish(client,userdata,result):             #create function for callback
        logging.debug('message published \r')
        pass

def mqtt_publisher(message,broker=broker,topic = topic,port=port):
    client1= paho.Client("control1")                           #create client object
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker,port)  
    ret = client1.publish(topic,message)
    
def joystick_values():
    logging.debug('Starting get joystick values')
    # time.sleep(2)
    jstest = JSTest()
    while 1:
        joystick = jstest.process_events()
        if type(joystick) == dict:
            joystick=json.dumps(joystick) # encode object to JSON
            mqtt_publisher(joystick)  

thread_joystick_values = threading.Thread(name='joystick_values', target=joystick_values)
thread_joystick_values.start()
