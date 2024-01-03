from lxml import etree
import os
import glob
import cv2
from tqdm import tqdm
import pickle
import numpy as np
import matplotlib.pyplot as plt
import collections
import random
import shutil
from pathlib import Path
LABELS = [] #FIXME
def voc_parse(xml_path):
    boxes = []
    doc = etree.parse(xml_path)

    for obj in doc.xpath('//object'):
        name = obj.xpath('./name/text()')[0]
        xmin = int(float(obj.xpath('./bndbox/xmin/text()')[0]))
        ymin = int(float(obj.xpath('./bndbox/ymin/text()')[0]))
        xmax = int(float(obj.xpath('./bndbox/xmax/text()')[0]))
        ymax = int(float(obj.xpath('./bndbox/ymax/text()')[0]))
        boxes.append((name, xmin, ymin, xmax, ymax))
    return boxes

def dump_box_to_tessstr(boxes, page, w, h):
    label_str = ''
    prev_ymin = boxes[0][2]
    for i, box in enumerate(boxes):
        name, xmin, ymin, xmax, ymax = box
        print(prev_ymin, ymin - prev_ymin)
        if ymin - prev_ymin > 10 and i != 0 and name != '.':
            label_str += f'\t {boxes[i-1][3]} {h - boxes[i-1][2]} {boxes[i-1][3] + 1} {h - boxes[i-1][2] + 1}\n'
            prev_ymin = ymin
            print("--")
        label_str += ' '.join([str(name), str(xmin), str(h - ymax), str(xmax), str(h - ymin), str(page)]) +'\n'
    return label_str
    

data_dir = '/home/asi/camera/thamnt/det_train/meter_reg/train/data_roboflow/train'
image_files = [os.path.join(data_dir, path) for path in os.listdir(data_dir) if path.endswith('jpg')]
save_dir = '/home/asi/camera/thamnt/det_train/meter_reg/train/data_roboflow/processed/v2'
for i, path in enumerate(image_files):
    i += 6
    all_label = ''
    img = cv2.imread(path)
    w, h = img.shape[1], img.shape[0]
    lb_path = path[:-4] + '.xml'
    boxes = voc_parse(lb_path)
    lb_str = dump_box_to_tessstr(boxes, 0, w, h)
    cv2.imwrite(os.path.join(save_dir, f'image_{i}.jpg'), img)
    all_label += lb_str
    with open(os.path.join(save_dir, f'image_{i}.box'), 'w') as f:
        f.write(all_label)


