# AutoImage Label Tool:

The idea behind this app was that it takes a long time to label images! Instead of labelling each image I decided to use my already trained Yolov4 and Yolov4-tiny model weights to label new images and save their bounding box coordinates. I created a wrapper around the app and made it so that anyone can use it. This app allowed me to annotate around 4000 images in a matter of few hours. A task which would easily take a day or two has been reduced significantly.

## How to use AutoImage Label Tool:

Folder Structure:
There are two main arguments app.py expects (i) Image Directory with all the images you want to annotate and (ii)config directory which contains the classes.txt, yolo.cfg and yolo_final.weights.

* Pls Note in cfg directory keep all names as mentioned here or you will run into error.


```python

images_folder/
      image_1.jpg
      image_2.jpg
      image_3.jpg
      ....
      
config_folder/
      yolov4.cfg
      classes.txt
      yolo_final.weights     
 ```
