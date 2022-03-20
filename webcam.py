import cv2
from datetime import datetime
from time import sleep
from os import path

capture = cv2.VideoCapture(0)
faces = cv2.CascadeClassifier("detect.xml")

semi_fps = 0

while True:
    time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    text = 'Time ' + time
    ret, frame = capture.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detections = faces.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=6)

    if detections != ():
        for (x, y, w, h) in detections:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 1)

        filename = f'Person: {time}.jpg'
        print(f'Person found! [{time}] [{filename}]')
        cv2.imwrite(path.join('records', filename), frame)
        semi_fps = 1
    else:
        semi_fps = 0

    if cv2.waitKey(1) == ord('q'):
        break
    
    sleep(semi_fps)

capture.release()
cv2.destroyAllWindows()
