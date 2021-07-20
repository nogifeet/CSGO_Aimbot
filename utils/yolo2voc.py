import os 
import argparse 
import os 
import numpy as np 
import cv2 
import time 
import tqdm 
from tqdm import tqdm
import xml.etree.ElementTree as ET
import argparse
import concurrent.futures
import multiprocessing
from multiprocessing import freeze_support


def make_dirs():
    os.chdir(opts.output_dir)
    os.makedirs('vocAnn')

def read_labels():
    labels =[]
    os.chdir(opts.cls_dir)
    with open('classes.txt','r') as read_txt:
        classes = read_txt.readlines()
        for i in classes:
           labels.append(i.strip('\n'))
    
    return labels

def yolo2voc(fname):

    def read_yolo():
        os.chdir(opts.lbl_dir)
        img = cv2.imread(fname+'.jpg')
        h,w,_ = img.shape 

        with open(fname+'.txt','r') as lbl_txt:
            lines = lbl_txt.readlines() 
            annotations = []
            for line in lines:
                cls_id = line.split(' ')[0]
                yolo_xmin = float(line.split(' ')[1])
                yolo_ymin = float(line.split(' ')[2])
                yolo_xmax = float(line.split(' ')[3])
                yolo_ymax = float(line.split(' ')[4])
                ann = conv(yolo_xmin,yolo_ymin,yolo_xmax,yolo_ymax,h,w)
                ann.append(cls_id)
                annotations.append(ann)

        create_voc_ann(annotations,fname,h,w,_)
        cv2.imwrite(fname+'.jpg',img)
        os.chdir(opts.lbl_dir)


    def conv(x_min,y_min,x_max,y_max,h,w):
    #convert yolo coords
        voc_xmin = (((x_min*float(w))*2) - x_max*float(w))/2
        voc_ymin = (((y_min*float(h))*2) - y_max*float(h))/2

        voc_xmax = x_max * float(w) + voc_xmin
        voc_ymax = y_max * float(h) + voc_ymin 

        return [int(round(voc_xmin,0)),int(round(voc_ymin,0)),int(round(voc_xmax,0)),int(round(voc_ymax,0))]

    def create_voc_ann(ann,fname,h,w,d):
        os.chdir(opts.output_dir)
        os.chdir('vocAnn')
        root = ET.Element("annotations")
        ET.SubElement(root, "folder").text = 'vocAnn'
        ET.SubElement(root, "filename").text = fname+'.xml'
        img_path = '{}\{}\{}'.format(opts.output_dir,'vocAnn',str(fname+'.jpg'))
        ET.SubElement(root, "path").text = img_path
        source = ET.SubElement(root, "source")
        ET.SubElement(source, "path").text = "unknown"
        size = ET.SubElement(root, "size")
        ET.SubElement(size, "width").text = str(w)
        ET.SubElement(size, "height").text = str(h)
        ET.SubElement(size, "depth").text = str(d)
        ET.SubElement(root, "segmented").text = "0"
        for i in ann:
            object = ET.SubElement(root, "object")
            cls_name = labels[int(i[-1])]
            ET.SubElement(object, "name").text = cls_name
            ET.SubElement(object, "pose").text = "Unspecified"
            ET.SubElement(object, "truncated").text = "0"
            ET.SubElement(object, "difficult").text = "0"
            bndbox = ET.SubElement(object, "bndbox")
            ET.SubElement(bndbox, "xmin").text = str(i[0])
            ET.SubElement(bndbox, "ymin").text = str(i[1])
            ET.SubElement(bndbox, "xmax").text = str(i[2])
            ET.SubElement(bndbox, "ymax").text = str(i[3])
        tree = ET.ElementTree(root)
        tree.write(fname+'.xml')

    read_yolo()


parser = argparse.ArgumentParser(description='Takes Yolo annotations and converts to Pascal Voc format and creates classes.txt in output directory.')
parser.add_argument('--lbl_dir', help='Yolo Label Directory', type=str,required=True)
parser.add_argument('--cls_dir', help='classes.txt file Directory ', type=str, required=True)
parser.add_argument('--output_dir', help='Pascal-Voc output Directory', type=str, required=True)

opts = parser.parse_args()
labels = read_labels()

def main():
    fcnt=0
    make_dirs()
    cores = multiprocessing.cpu_count()
    print(f"{cores} CPU Cores Found")
    
    os.chdir(opts.lbl_dir)
    files = [i.split('.')[0] for i in os.listdir() if i.split('.')[1]=='txt']
    print("Processing Files....")
    #timer
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=int(cores)) as executor:
        for f in files:
            fcnt+=1
            executor.submit(yolo2voc,f)
    
    end = time.time()

    print(f"{fcnt} files Processed")
    print(f"Process Finished in {round(end-start,2)} secs")


if __name__ == "__main__":
    freeze_support()
    main()