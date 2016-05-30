import os
import cv2
import numpy as np
import time

def mse(img1, img2):
    img = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    err = np.sum(img1.astype("float") - img.astype("float")) ** 2
    err /= float(img1.shape[0] * img1.shape[1])
    return err

def generate():
    #Generate testing data
    imgs = []
    files = os.listdir("base")
    files.sort()
    for f in files:
        imgs.append(cv2.imread("base/%s"%f, 0))

    imgsTest = []
    files = os.listdir("img")
    files.sort()
    for f in files:
        imgsTest.append(cv2.imread("img/%s"%f, 0))

    fw = open("test.data", "w")
    for i in imgsTest:
        fw.write("0 ")
        cnt_j = 1
        for j in imgs:
            fw.write("%d:"%cnt_j + str(mse(i,j)) + " " )
            cnt_j += 1
        fw.write("\n")
    fw.close()

    #start to predict
    cmds = [
        'model/svm-scale -r model/range1 test.data > test.scale',
        'model/svm-predict test.scale model/img.model test.predict > /dev/null'
    ]
    for cmd in cmds:
        os.system(cmd)

    #Read the predict result
    fr = open("test.predict", "r")
    data = fr.readlines()
    return "".join([i.strip() for i in data])


if __name__ == "__main__":
    generate()
