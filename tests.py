import numpy as np
from PIL import Image
from PIL import ImageFilter
import time
import cv2
import matplotlib.pyplot as plt


'''
testarr = np.zeros((20, 20, 3), dtype=np.uint8)
for i in range(20):
    for j in range(20):
        if i%2 == 0:
            if j%3 == 0:
                testarr[i][j] = 222, 150, 150





img = Image.fromarray(testarr, "RGB")
img = img.resize((500, 500))

for i in range(20):
    newtest = np.copy(testarr)
    cv2.waitKey(30)
    newtest[i][11] = 0, 255, 150
    newtest[11][i] = 0, 255, 150
    newtest[i][i] = 0, 255, 150
    img = Image.fromarray(newtest, "RGB")
    img = img.resize((500, 500))
    cv2.imshow("", np.array(img))
'''




game_map = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ])


map_image = np.zeros((10, 10, 3), dtype=np.uint8)  # sera tamaño
print(map_image[0][0])
line_index = 0
for line in game_map:
    for pixel in range(len(line)):
        if game_map[line_index][pixel] == 1:
            map_image[line_index][pixel] = 200, 200, 200
    line_index += 1



img = Image.fromarray(map_image, mode="RGB")
img = img.resize((400, 400), resample=Image.NEAREST)
cv2.imshow("", np.array(img))
cv2.waitKey(5000)
