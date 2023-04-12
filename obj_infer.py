# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 19:54:17 2022

@author: Bharathraj C L
"""

import json
import xmltodict
from xml.etree import ElementTree
from detecto.core import Dataset
from detecto.core import DataLoader, Model
import matplotlib.pyplot as plt
from detecto.utils import read_image
 
 
path = 'C:/Users/Bharathraj C L/Downloads/New folder (4)/archive (4)/real_img_act - name/dets/path.jpg'
# open the input xml file and read
# data in form of python dictionary
# using xmltodict module
import os
dir_name = os.path.dirname(path)
folder = os.path.basename(dir_name)
file_name = os.path.basename(path)


def create_xml(image_shape,data_list,path):
    
    dir_name = os.path.dirname(path)
    #print(dir_name)
    folder_name = os.path.basename(dir_name)
    file_name = os.path.basename(path)

    tree = ElementTree.ElementTree()
    
    root = ElementTree.Element("annotation")
    
    item = ElementTree.Element("folder")
    item.text = folder_name
    root.append(item)
    
    item = ElementTree.Element("filename")
    item.text = file_name
    root.append(item)
    
    item = ElementTree.Element("path")
    item.text = path
    root.append(item)
    
    item = ElementTree.Element("source")
    item1 =  ElementTree.Element("database")
    item1.text = "Unknown"
    item.append(item1)
    root.append(item)
    
    item = ElementTree.Element("size")
    
    item1 =  ElementTree.Element("width")
    item1.text = str(image_shape[0])
    item.append(item1)
    
    item1 =  ElementTree.Element("height")
    item1.text = str(image_shape[1])
    item.append(item1)
    
    item1 =  ElementTree.Element("depth")
    item1.text = str(image_shape[2])
    item.append(item1)
    
    root.append(item)
    
    item = ElementTree.Element("segmented")
    item.text = "0"
    root.append(item)
    
    
    for i in data_list:
        #print(i)
        item_object = ElementTree.Element("object")
        
        item_name =  ElementTree.Element("name")
        item_name.text = i[0]
        
        item_object.append(item_name)
        
        item_pose =  ElementTree.Element("pose")
        item_pose.text = 'Unspecified'
        
        item_object.append(item_pose)
        
        item_truncated = ElementTree.Element("truncated")
        item_truncated.text = "0"
        
        item_object.append(item_truncated)
        
        item_difficult = ElementTree.Element("difficult")
        item_difficult.text = "0"
        
        item_object.append(item_difficult)
    
        item_bndbox = ElementTree.Element("bndbox")
        
        item_xmin = ElementTree.Element("xmin")
        item_xmin.text = str(i[1][0])
        
        item_bndbox.append(item_xmin)
        

        item_ymin = ElementTree.Element("ymin")
        item_ymin.text = str(i[1][1])
        
        item_bndbox.append(item_ymin)

        item_xmax = ElementTree.Element("xmax")
        item_xmax.text = str(i[1][2])
        
        item_bndbox.append(item_xmax)

        
        item_ymax = ElementTree.Element("ymax")
        item_ymax.text = str(i[1][3])
        
        item_bndbox.append(item_ymax)
        
        
        item_object.append(item_bndbox)
        
        root.append(item_object)
    
    
    tree._setroot(root)
    xml_file = file_name.split('.')[0]+'.xml'
    tree.write(dir_name+'/'+xml_file)
    


path = 'C:/Users/Bharathraj C L/Downloads/New folder (4)/archive (4)/real_img_act - name/person2_org_new'

model = Model.load('C:/Users/Bharathraj C L/Downloads/New folder (4)/archive (4)/model_weights.pth', ['sig'])
#image = read_image(path+'/de.jpg')
#predictions = model.predict(image)

#image.shape



def re_process(predictions):
    
    lab = predictions[0]
    bnd = predictions[1].numpy()
    per = predictions[2].numpy()
    result = []
    len_lab = len(lab)
    for i in range(len_lab):
        if(per[i] >= 0.9):
            result.append([lab[i],list(bnd[i]),per[i]])
    return result

import glob

img_list = glob.glob(path+'/*.jpg')
    
for c,i in enumerate(img_list):
    print(c)
    image = read_image(i)
    image_shape = image.shape
    predictions = model.predict(image)
    data_list = re_process(predictions)
    create_xml(image_shape,data_list,i)
    #if(c > 20):
    #    break