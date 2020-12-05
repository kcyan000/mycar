from tensorflow import keras
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from adafruit_motorkit import MotorKit

model = load_model('/home/pi/mycar/models/rnn_2-1.h5')

kit = MotorKit()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    result = model.predict(frame)
    if result == 'label':
        
        kit.motor1.throttle = 1.0
        kit.motor2.throttle = 1.0
        time.sleep(0.5)
    
    elif result == 'label1':
        
        kit.motor1.throttle = -1.0
        kit.motor2.throttle = -1.0
        time.sleep(0.5)

    
    else:
        break