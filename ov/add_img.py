import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 1 读取图像
    img1 = cv.imread("s.jpeg")
    img2 = cv.imread("y.jpeg")

    # 2 加法操作
    img3 = cv.add(img1, img2)  # cv中的加法
    img4 = img1 + img2  # 直接相加

    # 3 图像显示
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
    axes[0].imshow(img3[:, :, ::-1])
    axes[0].set_title("cv中的加法")
    axes[1].imshow(img4[:, :, ::-1])
    axes[1].set_title("直接相加")
    plt.show()
