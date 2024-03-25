import cv2
import numpy as np
import os


img = cv2.imread('input\digits.png')
img = cv2.resize(img,(500,250))

# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
id = 0


for i in range(0, 250,5):
    for j in range(0, 500,5):
        number = img[i:i+5, j:j+5]
        cv2.imwrite(f'output/num_0/digit0_{id}.jpg',number)
        id += 1

