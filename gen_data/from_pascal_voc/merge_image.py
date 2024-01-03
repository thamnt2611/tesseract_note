# Merge digit line images into a big picture
import os
import cv2
from pathlib import Path
import numpy as np
import random
data_dir = '/home/asi/camera/thamnt/det_train/meter_reg/train/data8'
image_files = [os.path.join(data_dir, path) for path in os.listdir(data_dir) if path.endswith('jpg')]
save_dir = '/home/asi/camera/thamnt/det_train/meter_reg/train/data_roboflow/processed'
page = 0
all_images = []
max_width = 0
height = 0
for path in image_files:
    img = cv2.imread(path)
    w, h = img.shape[1], img.shape[0]
    max_width = max(w, max_width)
    height += h
    all_images.append(img)

res_img = np.ones((height + 10, max_width, 3)).astype(np.uint8) * 255
i = 10
for img in all_images:
    w, h = img.shape[1], img.shape[0]
    diff = max_width - w
    xmin = random.randint(0, diff)
    res_img[i : i + h, xmin : xmin + w] = img
    i += h
    print(i)
cv2.imwrite(os.path.join(save_dir, f'merge_data8.jpg'), res_img)

    