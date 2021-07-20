# File Structure:

1. main.py 
* main file to run use following commands

```python
#returns all the required arguments
python main.py --help 

python main.py --config_path=some_path --dims=1080_1920 --team=CT --p_min=0.2 --thresh=0.3
```

2. window_capture.py 
* used for grabbing specific window screen using Windows API

3. yolo.py 
* runs inference on image with GPU and returns frame and coords

4. save.py 
* saves all the detected images into new folder images/new_images.jpg

## Performmance Measure:

![Alt text](https://github.com/nogifeet/CSGO_Aimbot/blob/main/Data/Capture.PNG "FPS Table")

1. Yolov4 Model
* Yolov4 model was highly accurate with a low False Positive Rate.
* High Inference time resulting in low fps rate(9-11)
* Due to low FPS some click(x,y) decision made by the script were slightly inaccurate.

2. Yolov4 Tiny Model
* Yolov4 Tiny model had a high False Positive rate even at low threshold values. 
* Low Inference Time resulting in high fps rate(25-30)
* Due to the high false positive rate it was common for the model to predict an outside object as roi object.

## Results:
https://www.youtube.com/watch?v=lf7Cke5pj5Q

## Next
2. AutoImage Label Tool Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/AutoLabel
3. Utils_Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/utils

## Back 
1. Main_Page
* https://github.com/nogifeet/CSGO_Aimbot/blob/main/README.md
2. Config_Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/config

