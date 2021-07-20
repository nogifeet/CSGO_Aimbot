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
