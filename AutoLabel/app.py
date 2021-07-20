from yolo import YoloInf 
import cv2 
import os 
import time 
import argparse
import win32api

parser = argparse.ArgumentParser(description='Yolo Object Detection Annotation Helper Tool')
parser.add_argument('-c','--config_dir', help='Classes.txt file path location', type=str,required=True)
parser.add_argument('-i','--image_dir', help='Images Directory', type=str, required=True)

opts = parser.parse_args()

def save_ann(coords,f_name,h,w):
    val=[]
    for coord in coords:
        cls_idx = labels.index(coord[0])
        x_coord = round(((coord[1]+coord[3])/2)/w,6)
        y_coord = round(((coord[2]+coord[4])/2)/h ,6)

        x1_coord = round((coord[3]-coord[1])/w,6)
        y1_coord = round((coord[4]-coord[2])/h,6) 
        
        name = '{}.txt'.format(f_name)
        txt = '{} {} {} {} {}'.format(cls_idx,x_coord,y_coord,x1_coord,y1_coord)
        val.append(txt)
    
    try:
        with open(name,'w') as wrt_txt:
            for v in val:
                    wrt_txt.writelines(v)
                    wrt_txt.writelines('\n')
                
        wrt_txt.close()
    
    except UnboundLocalError:
        pass
    

yolo = YoloInf(opts.config_dir)
print("Loading Config")
labels = yolo.load_config()
print("Done Loading Config")

os.chdir(opts.image_dir)
images = [i for i in os.listdir() if i.split('.')[1]=='jpg']

p=0.1
t=0.3
count=0

while True:

    try:
        f_name = images[count].split('.')[0]
        img = cv2.imread(images[count])
        h,w,_ = img.shape
        frame,coords= yolo.inference(img,p,t,h,w)
    except IndexError:
        print("No more Images Left!")
        count-=1

    cv2.imshow('frame',frame)
    cv2.moveWindow('frame',0,0)

    if win32api.GetAsyncKeyState(ord('S')):
        #save annotations 
        save_ann(coords,f_name,h,w)
        print('Image {} Annotation Saved'.format(images[count]))
        count+=1

    elif win32api.GetAsyncKeyState(ord('A')):
        t+=0.1
        if t>float(1):
            t=1.0
    
    elif win32api.GetAsyncKeyState(ord('Z')):
        t-=0.1
        if t<float(0):
            t=0.0

    elif win32api.GetAsyncKeyState(ord('D')):
        p_m+=0.1
        if p_m>float(1):
            p_m=1.0

    elif win32api.GetAsyncKeyState(ord('R')):
        p_m-=0.1
        if p_m<float(0):
            p_m=0.0

    elif win32api.GetAsyncKeyState(ord('E')):
        count+=1


    elif win32api.GetAsyncKeyState(ord('Q')):
        if count<0:
            count=0
        count-=1


    if cv2.waitKey(1)==ord('x'):
        print("Exiting App")
        break
        
cv2.destroyAllWindows()

