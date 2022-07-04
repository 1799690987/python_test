import cv2
import numpy as np

if __name__ == '__main__':

    img = cv2.imread('./suoer.jpeg')
    gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)

    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.13, minNeighbors=1)

    for x, y, w, h in faces:
        cv2.rectangle(img,
                      pt1=(x, y),
                      pt2=(x + w, y + h),
                      color=[0, 0, 255],
                      thickness=2)

    cv2.imshow('face', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
