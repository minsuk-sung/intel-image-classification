import os
import sys
import warnings

warnings.filterwarnings('ignore')

import cv2
import pickle
import numpy as np
from tensorflow.keras.models import load_model

TEXT_LOC = (30,30)
FONT_SIZE = 0.8

THESHOLD = 0.3

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

model = load_model('./bin/mobilenetv2_class20.h5')

with open('./bin/class20.pickle','rb') as f:
    class20 = pickle.load(f)

(major_ver,minor_ver,subminor_ver) = cv2.__version__.split('.')

while True:
    ret, frame = capture.read()

    if int(major_ver) < 3:
        fps = capture.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = capture.get(cv2.CAP_PROP_FPS)

    

    img = cv2.resize(frame,(224,224),fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = img / 255

    expanded_img = np.expand_dims(img,axis=0)

    pred = model.predict(expanded_img)

    _cls = class20[np.argmax(pred)]
    _prob = np.max(pred)
    
    font_color = (0,0,0)
    label = 'Prediction : ...'

    if _prob > THESHOLD:

        font_color = (0,0,255)
        label = 'Prediction : {} ({:.2f}%)'.format(_cls.upper(),_prob * 100) 

    cv2.putText(frame,label,TEXT_LOC,cv2.FONT_HERSHEY_SIMPLEX,FONT_SIZE,font_color,2)
    cv2.putText(frame,'{} FRAMES'.format(fps),(450,30),cv2.FONT_HERSHEY_SIMPLEX,FONT_SIZE,(0,0,0),2)

    cv2.imshow('test',frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()