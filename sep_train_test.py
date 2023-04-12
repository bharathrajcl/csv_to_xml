# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:29:03 2023

@author: Bharathraj C L
"""


import detecto
from detecto import core, utils
import pandas as pd
import cv2
import os
import random
import shutil


for_path = os.listdir('C:/Users/Bharathraj C L/Downloads/New folder (4)/archive (4)/real_img_act - name/for_path_train')
org_path = os.listdir('C:/Users/Bharathraj C L/Downloads/New folder (4)/archive (4)/real_img_act - name/org_path_train')


for_test = []
for i in range(1000):
    for_test.append(random.choice(for_path))
    for_test = list(set(for_test))
    if(len(for_test) == 300):
        break
    
org_test = []
for i in range(1000):
    org_test.append(random.choice(org_path))
    org_test = list(set(org_test))
    if(len(org_test) == 300):
        break
    
for i in for_test:
    cur = 'C:/Users/Bharathraj C L/Downloads/New folder (4)/archive (4)/real_img_act - name/for_path_train/'+i
    tar = 'C:/Users/Bharathraj C L/Downloads/New folder (4)/archive (4)/real_img_act - name/for_path_test/'+i
    shutil.move(cur, tar)

    
    
for i in org_test:
    cur = 'C:/Users/Bharathraj C L/Downloads/New folder (4)/archive (4)/real_img_act - name/org_path_train/'+i
    tar = 'C:/Users/Bharathraj C L/Downloads/New folder (4)/archive (4)/real_img_act - name/org_path_test/'+i
    shutil.move(cur, tar)

