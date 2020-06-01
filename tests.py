import numpy as np
from PIL import Image
import time
import cv2


testarr = np.zeros((20, 20, 3), dtype=np.uint8)
for i in range(20):
    for j in range(20):
        if i%2 == 0:
            if j%3 == 0:
                testarr[i][j] = 255, 0, 255





img = Image.fromarray(testarr, "RGB")
img = img.resize((500, 500))

for i in range(20):
    newtest = testarr
    cv2.waitKey(30)
    newtest[i][11] = 0, 255, 150
    img = Image.fromarray(newtest, "RGB")
    img = img.resize((500, 500))
    cv2.imshow("", np.array(img))

