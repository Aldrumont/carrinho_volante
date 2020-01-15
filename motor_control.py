from gpiozero import PWMOutputDevice, AngularServo
from time import sleep

acelerator_pin = 26
brake_pin = 19
steering_wheel_key_pin = 21

class motor_control_class():
    def __init__(self, acelerator_pin=acelerator_pin , steering_wheel_key_pin=steering_wheel_key_pin):
        self.acelerator_pin = acelerator_pin
        self.brake_pin = brake_pin
        self.steering_wheel_key_pin = steering_wheel_key_pin
        # Initialise objects for H-Bridge PWM pins
        # Set initial duty cycle to 0 and frequency to 1000  
        self.acelerator = PWMOutputDevice(acelerator_pin, True, 0, 1000)
        self.brake = PWMOutputDevice(brake_pin, True, 0, 1000)
        self.steering_wheel = AngularServo(steering_wheel_key_pin, min_angle=-15.0, max_angle=15.0)

    def run(self,values,correction=1.5,servo_constant=-6):
        print(values)
        pedal_value = values["pedal_key"]
        steering_value = values["steering_wheel_key"]
        if abs(pedal_value) <= 0.3:
            self.brake.value = 0
            self.acelerator.value = 0
        elif pedal_value > 0:
            self.acelerator.value = pedal_value/correction
            self.brake.value = 0
        else:
            self.acelerator.value = 0
            self.brake.value = -pedal_value/correction
        self.steering_wheel.angle = -steering_value
        # print(self.steering_wheel.angle)
        print("Acelerador ",self.acelerator.value, "freio ",self.brake.value, "angulo ",self.steering_wheel.angle)

        
 
