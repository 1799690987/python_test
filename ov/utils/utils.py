import cv2


def read_img(path):
    # 默认彩色读取
    img2 = cv2.imread(path)
    return img2


def write_img(name, img):
    cv2.imwrite(name, img)


def cv_show(name, img):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    # 设置窗口大小
    cv2.resizeWindow(name, 620, 480)

    cv2.imshow(name, img)
    key = cv2.waitKey(0)
    if key == ord('q'):
        cv2.destroyAllWindows()
