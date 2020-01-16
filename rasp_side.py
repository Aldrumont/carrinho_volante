from __future__ import print_function
import paho.mqtt.client as mqtt
import json
import logging
import threading
import motor_control
import camera

broker="192.168.15.12"
topic = "test"
port=1883

key_names = {"pedal_key" : "A3", "steering_wheel_key":"A2"}
important_values = key_names.copy()
joystick_analogic_limits = (0,255)
steering_motor_limits=(-15.0,15.0)
pedal_motor_limits=(1.0,-1.0)
control = motor_control.motor_control_class()
output_values = 0

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
    # print(data)
    for key in key_names:
        if key_names[key] not in data:
            print("Not found the " + key +" ("+  key_names[key]+")")
        else: 
            if key == "pedal_key":
                output_value = correct_output_number(data[key_names[key]],joystick_analogic_limits,pedal_motor_limits)
            elif key == "steering_wheel_key":
                output_value = correct_output_number(data[key_names[key]],joystick_analogic_limits,steering_motor_limits)
            important_values[key] = output_value
            # print("test",enabled_cam.frame)
    # print(important_values)
    output_values = control.run(important_values)
    # print(img)

def enable_camera():
    camera.record()



def correct_output_number(x, input_limits, output_limits):
  return (x - input_limits[0]) * (output_limits[1] - output_limits[0]) / (input_limits[1] - input_limits[0]) + output_limits[0]

thread_mqtt_loop = threading.Thread(name='mqtt_loop', target=mqtt_loop)
thread_mqtt_loop.start()

thread_enable_camera = threading.Thread(name='enable_camera', target=enable_camera)
thread_enable_camera.start()



