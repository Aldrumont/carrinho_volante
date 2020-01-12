import paho.mqtt.client as mqtt
import json
import logging
import threading

broker="localhost"
topic = "test"
port=1883

key_pins = {"acelerator_key" : "A0", "brake_key" : "A3", "steering_wheel_key":"A2"}
important_keys = key_pins.copy()
joystick_analogic_limits = (0,255)
steering_motor_limits=(-5,5)
acelerator_motor_limits=(5,0)
brake_motor_limits=(0,-5)

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
    for key in key_pins:
        # print(data)
        if key_pins[key] not in data:
            print(f"Not found the {key} ({key_pins[key]}) ")
        else: 
            if key == "acelerator_key":
                output_value = correct_output_number(data[key_pins[key]],joystick_analogic_limits,acelerator_motor_limits)
            elif key == "brake_key":
                output_value = correct_output_number(data[key_pins[key]],joystick_analogic_limits,brake_motor_limits)
            elif key == "steering_wheel_key":
                output_value = correct_output_number(data[key_pins[key]],joystick_analogic_limits,steering_motor_limits)
            important_keys[key] = output_value
    print(important_keys)

def correct_output_number(x, input_limits, output_limits):
  return (x - input_limits[0]) * (output_limits[1] - output_limits[0]) / (input_limits[1] - input_limits[0]) + output_limits[0]




thread_mqtt_loop = threading.Thread(name='mqtt_loop', target=mqtt_loop)
thread_mqtt_loop.start()




