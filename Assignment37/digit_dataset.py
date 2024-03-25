import cv2
import numpy as np
import os

img = cv2.imread('input\digits.jpg')
print(img.shape)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
id = 0
n2 = 0

for col in range(0, 1000,20):
    for row in range(0, 2000,20):
        digit = img[col: col + 20, row: row + 20]
        os.makedirs(f"output/num_{n2}",exist_ok=True)
        cv2.imwrite(f'output/num_{n2}/digit{n2}_{id}.jpg',digit)
        id += 1
        if id > 500:
            id = 1
            n2 += 1
