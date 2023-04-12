# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:39:22 2022

@author: Bharathraj C L
"""

from detecto.core import Dataset
from detecto.utils import xml_to_csv


path = 'C:/Users/Bharathraj C L/Downloads/New folder (4)/archive (4)/real_img_act - name/det'
xml_to_csv(path, 'labels.csv')