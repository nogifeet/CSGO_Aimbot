import os 
import cv2 
import tqdm
from tqdm import tqdm

class new_data:
    def __init__(self,h,w):
        self.h = int(h)
        self.w = int(w) 

    def save_annotation(self,frames):
        max_=[]
        
        if len(os.listdir())==0:
            idx = 1

        elif len(os.listdir())>0:
            for file in os.listdir():
                
                if file.split('.')[1] in ['jpg','jpeg','bmp']:
                    max_.append(int(file.split('.')[0].split('_')[1]))

            idx = max(max_)
        
        saved_images=0
        print("Saving Detected Images")

        for i in tqdm(range(0,len(frames))): 
            #print("Saving Image:{}".format(idx))
            cv2.imwrite('out_{}.jpg'.format(idx), i)
            idx+=1 
            saved_images+=1
        
        print("Done Saving Images")
        print(f"Total Images Saved {saved_images}")
        