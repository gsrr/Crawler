import os
import cv2
import numpy as np
import time

def mse(img1, img2):
    img = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    err = np.sum(img1.astype("float") - img.astype("float")) ** 2
    err /= float(img1.shape[0] * img1.shape[1])
    return err


#1 Generate train.data
img_train = []
files = os.listdir("trainSet")
files.sort()
for f in files:
    img_train.append(cv2.imread("trainSet/%s"%f,0))

fw = open("train.data", "w")
cnt = 0
for i in img_train:
       fw.write("%d "%cnt) 
       ccnt = 1
       for j in img_train:
           fw.write("%d"%(ccnt) + ":" + str(mse(i,j)) + " ")
           ccnt += 1
       fw.write("\n")
       cnt += 1
