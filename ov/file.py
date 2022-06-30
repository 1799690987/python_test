import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from ov.utils.utils import cv_show
from ov.utils.utils import read_img
from ov.utils.utils import write_img

if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    while True:
        success, img = cap.read()
        cv.imshow("Video", img)
        if cv.waitKey(0) == ord('q'):
            break
