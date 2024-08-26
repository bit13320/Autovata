from machine import Pin, PWM

"""
Class to represent our robot car    pwm.duty(duty)    duty = int((angle / 180) * 75 + 40) 25~135 center70
>>> servo = PWM(Pin(8),freq=50)
>>> servo.duty(65)
"""
class RobotCar():
    def __init__(self, enable_pins, motor_pins, speed):
        self.right_pin = PWM(Pin(8), freq=50)
        self.left_pin = PWM(Pin(9), freq=50)
        
        self.speed = speed
        
    def stop(self):
        print('Car stopping')
        self.right_pin.duty(70)
        self.left_pin.duty(70)
        
    def forward(self):
        print('Move forward')
        self.right_pin.duty(75)
  
    def reverse(self):
        print('Move reverse')
        self.right_pin.duty(65)

    def turnLeft(self):
        print('Turning Left')
        self.left_pin.duty(75)
    
    def turnRight(self):
        print('Turning Right')
        self.left_pin.duty(63)
        
    def set_speed(self, new_speed):
        self.speed = new_speed
        
    def cleanUp(self):
        print('Cleaning up pins')
        self.right_motor_enable_pin.deinit()
        self.left_motor_enable_pin.deinit()
