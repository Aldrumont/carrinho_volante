import paho.mqtt.client as mqtt
import json
import logging
import threading

broker="localhost"
topic = "test"
port=1883

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
def on_connect(client, userdata, flags, rc):
        client.subscribe("test")
def on_message(client, userdata, msg):
    message=json.loads(msg.payload)
    joystick_values_interpreter(message)
def mqtt_loop(broker=broker,topic = topic,port=port):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    client.loop_forever()

def joystick_values_interpreter(data):
    print(data)
    pass





thread_mqtt_loop = threading.Thread(name='mqtt_loop', target=mqtt_loop)
thread_mqtt_loop.start()




