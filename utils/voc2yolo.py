import os 
import numpy as np
import time 
import tqdm 
from tqdm import tqdm
import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description='Takes Pascal VOC annotations and converts to yolo format and creates classes.txt in output directory.')
parser.add_argument('-l','--lbl_dir', help='Pascal-Voc Label Directory', type=str,required=True)
parser.add_argument('-c','--cls_dir', help='classes.txt file Directory ', type=str, required=True)
parser.add_argument('-o','--output_dir', help='Yolo output Directory', type=str, required=True)

opts = parser.parse_args()
classes=[]
os.chdir(opts.cls_dir)
with open('classes.txt','r') as read_txt:
    names = read_txt.readlines()
    for name in names:
        classes.append(name.rstrip('\n').lower())

os.chdir(opts.output_dir)
with open('classes.txt','w') as wrt_txt:
    for c in classes:
        wrt_txt.writelines(c)
        wrt_txt.writelines('\n')
wrt_txt.close()


os.chdir(opts.lbl_dir)
for i in tqdm(os.listdir(),desc='Converting Annotations'):
    new_coords=[]
    if i.split('.')[1]=='xml':
        Xmin=[]
        Ymin=[]
        Xmax=[]
        Ymax=[]
        class_ = []

        tree = ET.parse(i)
        root = tree.getroot()
        xmin = root.findall('.//xmin')
        ymin = root.findall('.//ymin')
        xmax = root.findall('.//xmax')
        ymax = root.findall('.//ymax')
        cls_name = root.findall('.//name')
        img_h = root.findall('.//height')
        img_w = root.findall('.//width')
        filename = root.findall('.//filename')

        for x in xmin:
            Xmin.append(int(x.text))
        for y in ymin:
            Ymin.append(int(y.text))
        for x_1 in xmax:
            Xmax.append(int(x_1.text))
        for y_1 in ymax:
            Ymax.append(int(y_1.text))
        for cls in cls_name:
            class_.append(cls.text)
        for h in img_h:
            height = int(h.text)
        for w in img_w:
            width = int(w.text)
        for f in filename:
            filename = f.text.split('.')[0]+'.txt'

        for i in range(len(Xmin)):
            x_coord = ((Xmin[i]+Xmax[i])/2)/width
            y_coord = ((Ymin[i]+Ymax[i])/2)/height 

            x1_coord = (Xmax[i]-Xmin[i])/width
            y1_coord = (Ymax[i]-Ymin[i])/height 

            cls = classes.index(class_[i])

            txt = '{} {} {} {} {}'.format(cls,x_coord,y_coord,x1_coord,y1_coord)
            #print(txt)
            new_coords.append(txt)
        
        os.chdir(opts.output_dir)
        with open(filename,'w') as wrt_txt:
            for val in new_coords:
                wrt_txt.writelines(val)
                wrt_txt.writelines('\n')
        
        wrt_txt.close()

        os.chdir(opts.lbl_dir)




        
        
