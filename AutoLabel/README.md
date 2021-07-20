# AutoImage Label Tool:

The idea behind this app was that it takes a long time to label images! Instead of labelling each image, I decided to use my already trained Yolov4 and Yolov4-tiny model weights to label new images and save their bounding box coordinates. I created a wrapper around the app and made it so that anyone can use it. This app allowed me to annotate around 4000 images in a matter of few hours. A task that would easily take a day or two has been reduced significantly.

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
      yolo.cfg
      classes.txt
      yolo_final.weights     
 ```
 * If your image files are not of 'jpg' format please change line 46 in app.py 

```python
#return all the required arguments by the program
python app.py --help   

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
