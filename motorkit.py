import time
from adafruit_motorkit import adafruit_motorkit

kit = MotorKit()

kit.motor1.throttle = 1.0
kit.motor2.throttle = 1.0
time.sleep(2)

kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
time.sleep(2)

kit.motor1.throttle = -1.0
kit.motor2.throttle = -1.0
time.sleep(2)

kit.motor1.throttle = None
kit.motor2.throttle = None