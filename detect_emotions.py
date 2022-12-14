from keras.models import load_model
from tensorflow.keras.utils import img_to_array
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = load_model('Emotions-Model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture("myvid1.mp4")


while True:
    _, frame = cap.read()
    # labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.4, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48,48), interpolation=cv2.INTER_AREA)      ## reshaping as model is trained on 48x48x1



        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

            prediction = model.predict(roi)[0]
            # print(model.predict(roi))
            label = emotion_labels[prediction.argmax()]
            cv2.putText(frame, label, (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,255,0), 2)
        else:
            continue
            # cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0), 2)
    cv2.imshow('Detected Emotion',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()