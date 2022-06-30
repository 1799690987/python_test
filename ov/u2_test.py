import cv2


def read_img(path):
    # 默认彩色读取
    img2 = cv2.imread(path)
    return img2


def cv_show(name, img):
    cv2.imshow(name, img)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()


if __name__ == '__main__':
    pass