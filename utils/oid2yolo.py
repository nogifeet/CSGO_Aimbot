import os 
import time 
import tqdm 
from tqdm import tqdm
import numpy as np 
import cv2 

def convert(coords,h,w):
    '''
    Conver coords
    '''
    coords[2] -= coords[0]
    coords[3] -= coords[1]
    x_diff = int(coords[2]/2)
    y_diff = int(coords[3]/2)
    coords[0] = coords[0]+x_diff
    coords[1] = coords[1]+y_diff
    coords[0] /= int(w)
    coords[1] /= int(h)
    coords[2] /= int(w)
    coords[3] /= int(h)
    return coords

def process(file_name,annotations,h,w):
    '''
    read each line in file
    read class 
    read annotation and send to convert 

    '''
    new_final_coords=[]
    for ann_txt in annotations:
        cls = classes.index(ann_txt.split(' ')[0])
        x_1 = float(ann_txt.split(' ')[1])
        x_2 = float(ann_txt.split(' ')[2])
        x_3 = float(ann_txt.split(' ')[3])
        x_4 = float(ann_txt.split(' ')[4])
        coords = [x_1,x_2,x_3,x_4]
        new_coords = convert(coords,h,w)
        txt = '{} {} {} {} {}'.format(cls,round(new_coords[0],4),round(new_coords[1],4),round(new_coords[2],4),round(new_coords[3],4))
        new_final_coords.append(txt)
    
    return new_final_coords


classes=[]
with open('classes.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        classes.append(line.rstrip('\n'))

print("Total Classes:{}".format(len(classes)))

path = os.getcwd() 
data_path = os.path.join(path,r"OID\Dataset\train")
os.chdir(data_path)

for cls_folder in os.listdir():
    os.chdir('{}'.format(cls_folder))
    for file in tqdm(os.listdir(),desc='Converting {} Annotations'.format(cls_folder)):
        try:
            if file.split('.')[1]=='jpg':
                img = cv2.imread(file)
                h,w,_ = img.shape
                os.chdir('Label')
                with open('{}.txt'.format(file.split('.')[0]),'r') as txt_file:
                    annotations = txt_file.readlines()
                    pr_data=process(file,annotations,h,w)
                txt_file.close()
                os.chdir('..')
                with open('{}.txt'.format(file.split('.')[0]),'w') as write_txt:
                    for new_ann in pr_data:
                        write_txt.writelines(new_ann)
                        write_txt.writelines('\n')
                write_txt.close()
        except IndexError:
            continue
    os.chdir('..')

            

            