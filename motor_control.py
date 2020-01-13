from gpiozero import PWMOutputDevice, AngularServo
from time import sleep

acelerator_pin = 1
brake_pin = 1
steering_wheel_key_pin = 1

class motor_control_class():
    def __init__(self, acelerator_pin=acelerator_pin , brake_pin=brake_pin, steering_wheel_key_pin=steering_wheel_key_pin):
        self.acelerator_pin = acelerator_pin
        self.brake_pin = brake_pin
        self.steering_wheel_key_pin = steering_wheel_key_pin
        # Initialise objects for H-Bridge PWM pins
        # Set initial duty cycle to 0 and frequency to 1000  
        self.acelerator = PWMOutputDevice(acelerator_pin, True, 0, 1000)
        self.brake = PWMOutputDevice(brake_pin, True, 0, 1000)
        self.steering_wheel = AngularServo(steering_wheel_key_pin, min_angle=-30, max_angle=30)

    def run(self,values):
        self.acelerator.value = values["acelerator_key"]
        self.brake.value = values["brake_key"]
        self.steering_wheel.angle = values["steering_wheel_key"]
 
 
