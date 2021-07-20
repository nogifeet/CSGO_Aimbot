from window_capture import screen_grab 
from yolo import YoloInf
from save import new_data 
from pynput.mouse import Button, Controller
import cv2 
import time 
import os 
import argparse

parser = argparse.ArgumentParser(description='Run Yolo Inference on OpenCV GPU')
parser.add_argument('-c','--config_path', help='Directory Containing .cfg, classes.txt and yolo weights', type=str, required=True)
parser.add_argument('-d','--dims', help='Height_width seperated by "_"', type=str, required=True)
parser.add_argument('-t','--team', help='CT or T', type=str, required=True)
parser.add_argument('-p','--p_min', help='Probability Minimum Value between 0 to 1.0 ', type=str, required=True)
parser.add_argument('-tt','--thres', help='Threshold Value between 0 to 1.0', type=str, required=True)


opts = parser.parse_args()
h,w = opts.dims.split('_')[:]

#save video
name = 'yolov4.avi' 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(name,fourcc, 20.0, (800,600))

def click(x,y,cls,team=opts.team):
    mouse = Controller()

    if team == 'CT' and cls in ['ct_h','ct'] or team=='T' and cls in ['t','t_h']:
        pass

    else:
        #headshot
        if cls=='t_h' or 'ct_h':
                mouse.position = (x,y)
                mouse.press(Button.left)
                mouse.release(Button.left)
        #bodyshot
        elif cls=='ct' or 't':
                mouse.position = (x,y)
                mouse.press(Button.left)
                mouse.release(Button.left)
           
def draw(frame,coords,loop_time):
    cv2.rectangle(frame, (coords[0][1], coords[0][2]),(coords[0][3],coords[0][4]),(0,255,0), 2)
    cv2.circle(frame,(coords[0][5], coords[0][6]), 1, (0,0,255), -1)

    text_box_current = '{}'.format(coords[0][0])
    cv2.putText(frame, text_box_current, (coords[0][1], coords[0][2] - 10),cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0), 2)
    click(coords[0][5],coords[0][6],coords[0][0])

    fps_ = round(1/(time.time() - loop_time),0)
    cv2.putText(frame,"FPS: {}".format(fps_), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0))

    return frame

images=[]
sc = screen_grab(h,w)
inf = YoloInf(0.1,0.3,h,w,opts.config_path)

print('Loading Config Files....')
inf.load_config()
print('Done Loading Config Files....')

print('Starting Detection in 3 seconds')
time.sleep(3)

loop_time = time.time()
while True:
    frame = sc.window_capture()
    objFrame,coords = inf.inference(frame)

    if len(coords)>0:
        images.append(frame)
        drawFrame = draw(objFrame,coords,loop_time)
        cv2.moveWindow('frame',800,0)
        cv2.imshow('frame',drawFrame)
        out.write(drawFrame)

    else:
        fps_ = round(1/(time.time() - loop_time),0)
        cv2.putText(frame,"FPS: {}".format(fps_), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0))
        cv2.moveWindow('frame',800,0)
        cv2.imshow('frame',frame)
        out.write(frame)
    
    loop_time = time.time()

    if cv2.waitKey(1)==ord('q'):
        try: 
            os.makedirs('images')
            os.chdir('images')
        except:
            os.chdir('images')

        s = new_data(h,w)
        s.save_annotation(images)
        break 

print("Stopping Detection")
print("Destroying Frame")

cv2.destroyAllWindows()
out.release()