import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('./zhuchiren.png')
    gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    faces = face_detector.detectMultiScale(gray)
    star = cv2.imread('wujiaoxing.png')
    for x, y, w, h in faces:
        cv2.rectangle(img,
                      pt1=(x, y),
                      pt2=(x + w, y + h),
                      color=[0, 0, 255],
                      thickness=2)
        d = (3 * w) // 8
        img[y:y + h // 4, x + d:x + d + w // 4] = cv2.resize(star, (w // 4, h // 4))
    cv2.imshow('face', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
