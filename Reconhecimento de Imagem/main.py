import cv2
import pyautogui
from win32api import GetSystemMetrics

faceCascade = cv2.CascadeClassifier('haarcascade_face.txt')
#cv2.imread('')
webcam = cv2.VideoCapture(0)

while True:
    s, image = webcam.read()

    faces = faceCascade.detectMultiScale(image, minNeighbors=5, scaleFactor=1.1,minSize = (40,40), maxSize = (200,200))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow('Video', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.realease()
cv2.destroyAllWindows()
    
