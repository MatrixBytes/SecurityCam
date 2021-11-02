import cv2
import datetime
import threading

capture = cv2.VideoCapture(0)
faces = cv2.CascadeClassifier("detect.xml")

while True:
    text = 'Time ' + datetime.datetime.now().strftime("%d-%m-%y ~ %H:%M:%S")
    ret, frame = capture.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detections = faces.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=6)

    for (x, y, w, h) in detections:
        cv2.line(frame, (x, y), (0, 0), (255, 0, 0))
        cv2.line(frame, (x, y), (640, 480), (0, 255, 0))
        cv2.line(frame, (x, y), (640, 0), (0, 0, 255))
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 1)
        cv2.putText(frame, 'Person found!', (230, 35), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), thickness = 1)

    cv2.putText(frame, text, (10, 465), cv2.FONT_HERSHEY_TRIPLEX, 0.65, (255, 255, 255), thickness = 1)
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()