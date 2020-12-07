# Yolo2Coco

Object Detection annotation Convert from YOLO Darknet to COCO

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;  



## YOLO annotation format

1. txt file format


2. bbox annotation
```
 <object-class> <x> <y> <width> <height>
```

x and y indicate the center coordinates of bbox.

values of x, y, width, and height are nomalized.

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;



## COCO annotation format

1. json file format


2. bbox annotation
```
<x> <y> <width> <height>
```

x and y indicate the top left coordinates of bbox.

values are not normalized.

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;



## Requirements

```
pip install -r requirements.txt
```


&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;


## Parameters

1. base_path 
- Path to YOLO dataset folder
- The folder must include .txt file, .names file, and image folder (2, 3, 4)


2. txt
- .txt file with path of images inside


3. data_path
- Name of the image folder

4. cls_path
- Name of the .names file
- .names file includes category names

**.names file example**
```
person
ship
car
truck
tree
```

5. output_path
- Name of the output folder

```
python yolo2coco.py --base_path /YOLO_dataset --txt train.txt --data_path images --cls_path obj.names --output_path coco_output
```
