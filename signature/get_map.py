import cv2
import copy

import numpy as np
from PIL import Image


def cv2_imread(filePath):
    cv2_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    return cv2_img


def cv2_imwrite(img, filePath):
    cv2.imdecode(".png", img)[1].tofile(filePath)


def getMap(img, gdThr):
    mask = (gdThr < img[:, :, 0]) & (gdThr < img[:, :, 1]) & (gdThr < img[:, :, 2])
    alpha = (1 - mask.astype(np.uint8)) * 255
    h, w, c = img.shape
    if c == 3:
        img_rgba = np.concatenate((img, alpha[:, :, np.newaxis]), -1)
    else:
        img_rgba = copy.deepcopy(img)
        img_rgba[:, :, -1] = alpha
    img_rgba = Image.fromarray(img_rgba)

    return img_rgba


def uiMain(imgPath, gdThr):
    try:
        img = cv2_imread(imgPath)
    except Exception as e:
        return e, 0

    featureMap = getMap(img, gdThr)
    distPath = imgPath.replace(".", "_Sign.").replace(".jpg", ".png")
    featureMap.save(distPath)

    return distPath, 1


if __name__ == '__main__':
    while True:
        imgPath = input("请输入图片绝对路径：")
        try:
            img = cv2_imread(imgPath)
        except Exception as e:
            print(f"图片路径错误：{e}")

        featureMap = getMap(img)
        featureMap.save(imgPath.replace(".", "_Sign."))

