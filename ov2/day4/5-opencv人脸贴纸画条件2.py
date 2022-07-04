import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('./rui.jpg')
    cv2.namedWindow('face', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('face', 480, 480)
    gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)

    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    faces = face_detector.detectMultiScale(gray)
    star = cv2.imread('wujiaoxing.png')
    for x, y, w, h in faces:
        star_s = cv2.resize(star, (w // 4, h // 4))
        w1 = w // 4
        h1 = (h // 4)
        for i in range(h1):
            for j in range(w1):  # 遍历 图片数据
                if not (star_s[i, j] > 200).all():
                    img[i + 2 * y - y // 8, j + x + x // 4] = star_s[i, j]
                    img[i + 2 * y - y // 8, j + 2 * x] = star_s[i, j]

            cv2.imshow('face', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
