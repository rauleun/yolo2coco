# Yolo2Coco

Object Detection annotation Convert from YOLO Darknet to COCO

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;  



## YOLO annotation format

1. *txt* file format


2. bbox annotation
```
 <object-class> <x> <y> <width> <height>
```

<x> and <y> indicate the center coordinates of bbox. All values are nomalized by image's original width and height.

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;



## COCO annotation format

1. *json* file format


2. bbox annotation
```
<x> <y> <width> <height>
```

<x> and <y> indicate the top left coordinates of bbox. All values are not normalized.

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

- *base_path*  
Parameter *'base_path'* indicates a path to the YOLO dataset folder. The dataset folder must include the '.txt file', '.names file', and the image folder. Txt file contains the absolute path of each image file. Names file contains the whole class categories. Data folder contains all the image and annotation files. Each image-annotation pair has the same filename except for the file format. ('png'/ 'txt')


- *txt*  
Parameter *'txt'* indicates the filename of txt file. Txt file contains the absolute path of whole images.

- *data_path*  
Parameter *'data_path'* indicates the name of data folder. Data folder contains all the images(.png or .jpg) and the annotation files(.txt).

- *cls*  
Parameter *'cls'* indicates the filename of names file. Names file contains the whole class categories. Below is the example of names file.

**.names file example**
```
person
ship
car
truck
tree
```

- *output_path*  
Parameter *'output_path'* indicates the output folder name. The converted COCO format data will saved.


## Example
```
python yolo2coco.py --base_path /YOLO_dataset --txt train.txt --data_path images --cls obj.names --output_path coco_output
```
