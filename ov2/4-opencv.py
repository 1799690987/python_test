import cv2

if __name__ == '__main__':
    rose = cv2.imread( "./rose.jpg")
    cv2.imshow('rose', rose[:, :, ::-1])
    cv2.waitKey()
    cv2.destroyAllWindows()
