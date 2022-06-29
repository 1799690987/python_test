import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def read_img():
    # 默认彩色读取
    img2 = cv.imread('/Users/bytedance/PycharmProjects/python_test/ov/utils/c.png')
    return img2


if __name__ == '__main__':
    windows = read_img()
    # 窗口可调节
    cv.namedWindow('windows', cv.WINDOW_NORMAL)
    # 设置窗口大小
    cv.resizeWindow('windows', 680, 480)
    # 展示窗口的名字new_windows
    cv.imshow('windows', windows)
    # 0等待按键 大于0是等待时间单位毫秒
    key = cv.waitKey(0)
    if key == 'q':
        cv.destroyAllWindows()
