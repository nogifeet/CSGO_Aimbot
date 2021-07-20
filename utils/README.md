# Conversion Scripts:

1. yolo2voc.py
* Takes Yolo annotations and converts to Pascal Voc format and creates classes.txt in output directory. 

```python
#returns all the required arguments 
python yolo2voc.py --help 

python yolo2voc.py --lbl_dir=some_path --cls_dir=path_to_classes.txt_file --output_dir=Some_output_path
```

2. voc2yolo.py
* Takes Pascal Voc annotations and converts them to Yolo format.
```python
#returns all the required arguments 
python voc2yolo.py --help 

python voc2yolo.py --lbl_dir=some_path --cls_dir=path_to_classes.txt_file --output_dir=Some_output_path
```

3. oid2yolo.py 
* Converts OID Annotations to Yolo format.
* Place Oid2yolo.py in main OIDV4_Toolkit folder.
* Create a new classes.txt file in the same folder with all the class labels that you want to convert.
* Run oid2yolo.py 

## Back 
1. Main_Page
* https://github.com/nogifeet/CSGO_Aimbot/blob/main/README.md
2. Config_Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/config
3. Inference_Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/inference
4. AutoImage Label Tool Readme
* https://github.com/nogifeet/CSGO_Aimbot/tree/main/AutoLabel
