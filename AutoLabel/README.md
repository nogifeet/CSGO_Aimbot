# AutoImage Label Tool:

The idea behind this tool was that it takes a long time to label images! Instead of labelling each image, I decided to use my already trained Yolov4 and Yolov4-tiny model weights to label new images and save their bounding box coordinates. I created a script around the tool and made it so that anyone can use it. This tool allowed me to annotate around 4000 images in a matter of few hours. A task that would easily take a day or two has been reduced significantly.

### Note: 
* Double check all annotations from the tool before begining training.
* OpenCV GPU setup is required for faster detections.

## How to use AutoImage Label Tool:

Folder Structure:
There are two main arguments app.py expects (i) Image Directory with all the images you want to annotate and (ii) config directory which contains the classes.txt, yolo.cfg and yolo_final.weights.

* Pls Note in cfg directory keep all names as mentioned here or you will run into error.

```python

images_folder/
      image_1.jpg
      image_2.jpg
      image_3.jpg
      ....
      
config_folder/
      yolo.cfg
      classes.txt
      yolo_final.weights     
 ```
 * If your image files are not of 'jpg' format please change line 46 in app.py 

```python
#return all the required arguments by the program
python app.py --help   

usage: app.py [-h] -c CONFIG_DIR -i IMAGE_DIR

Yolo Object Detection Annotation Helper Tool

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_DIR, --config_dir CONFIG_DIR
                        Classes.txt file path location
  -i IMAGE_DIR, --image_dir IMAGE_DIR
                        Images Directory
                        
python app.py --image_dir=some_path --config_dir=some_path
 ```
 
 ## keyboard Commands:
 ```python
#keyboard Commands
1. Keypress-A Increases Threshold Value
2. Keypress-Z Decreases Threshold Value
3. Keypress-D Increases Probability Minimum Value
4. Keypress-R Decreases Probability Minimum Value
5. Keypress-S Saves Annotation File and move onto next image
6. Keypress-Q Go to previous image
7. Keypress-E Go to next image 
8. Keypress-X Quit/Exit

 ```
 
 The results from the AutoImage Label Tool are stored here https://github.com/nogifeet/CSGO_Aimbot/tree/main/AutoLabel/Images
 
 There are six different images having different dimensions which the AutoImage Label Tool was able to handle. More features will be added to this tool in the future.
 
 ## Updates:
 * 07/2021 Working on saving annotation in different formats like yolo, Pascal, OpenCV-Haar Cascade, CSV and Tensorflow records.

 
 ## Next
1. Utils_Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/utils

## Back 
1. Main_Page
* https://github.com/nogifeet/CSGO_Aimbot
2. Config_Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/config
3. Inference_Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/inference

