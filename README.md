# Yolo2Coco

Object Detection annotation Convert from YOLO Darknet to COCO

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;  


## YOLO annotation format

file format : ".txt"

```
 <object-class> <x> <y> <width> <height>
```

x and y indicate the center coordinates of bbox.

values of x, y, width, and height are nomalized.




## COCO annotation format

file format : ".json"

```
<x> <y> <width> <height>
```

x and y indicate the top left coordinates of bbox.

values are not normalized.




## Requirements

```
pip install -r requirements.txt
```
