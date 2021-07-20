# Conversion Scripts:

1. yolo2voc.py

```python
#returns all the required arguments 
python yolo2voc.py --help 

usage: yolo2voc.py [-h] --lbl_dir LBL_DIR --cls_dir CLS_DIR --output_dir OUTPUT_DIR

Takes Yolo annotations and converts to Pascal Voc format and creates classes.txt in output directory.

optional arguments:
  -h, --help            show this help message and exit
  --lbl_dir LBL_DIR     Yolo Label Directory
  --cls_dir CLS_DIR     classes.txt file Directory
  --output_dir OUTPUT_DIR
                        Pascal-Voc output Directory

python yolo2voc.py --lbl_dir=some_path --cls_dir=path_to_classes.txt_file --output_dir=Some_output_path
```

2. voc2yolo.py
```python
#returns all the required arguments 
python voc2yolo.py --help 

usage: voc2yolo.py [-h] -l LBL_DIR -c CLS_DIR -o OUTPUT_DIR

Takes Pascal VOC annotations and converts to yolo format and creates classes.txt in output directory.

optional arguments:
  -h, --help            show this help message and exit
  -l LBL_DIR, --lbl_dir LBL_DIR
                        Pascal-Voc Label Directory
  -c CLS_DIR, --cls_dir CLS_DIR
                        classes.txt file Directory
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Yolo output Directory
                        
python voc2yolo.py --lbl_dir=some_path --cls_dir=path_to_classes.txt_file --output_dir=Some_output_path
```

3. oid2yolo.py 
* Converts OID Annotations to Yolo format.
* Place Oid2yolo.py in main OIDV4_Toolkit folder.
* Create a new classes.txt file in the same folder with all the class labels that you want to convert.
* Run oid2yolo.py 

## Back 
1. Main_Page
* https://github.com/nogifeet/CSGO_Aimbot
2. Config_Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/config
3. Inference_Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/inference
4. AutoImage Label Tool Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/AutoLabel
