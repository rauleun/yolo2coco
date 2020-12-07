import os
import argparse
import cv2
import json
from tqdm import tqdm
import time
from datetime import date

def get_args_parser():
    parser = argparse.ArgumentParser('Set conditions', add_help=False)
    parser.add_argument('--path_base', default='/hd/hyunsung/data/gov-thermal/test-20201126/total', type=str)
    parser.add_argument('--txt', default='train.txt', type=str)
    parser.add_argument('--data_path', default='obj_train_data', type=str)
    parser.add_argument('--output_path', default = 'output', type=str)
    parser.add_argument('--cls_path', default = 'obj.names', type=str)
    return parser

def main(args):
    path_base = args.path_base
    path_txt = os.path.join(path_base, args.txt)
    
    if not os.path.isdir(args.output_path):
        os.mkdir(args.output_path)
    if not os.path.isdir(os.path.join(args.output_path, 'images')):
        os.mkdir(os.path.join(args.output_path, 'images'))
        os.mkdir(os.path.join(args.output_path, 'annotations'))

    image_list = []
    annotation_list = []
    with open(path_txt, 'r') as f:
        while True:
            line = f.readline()
            if not line: break
            image_list.append(line[:-1])
            annotation_list.append(line[:-4]+'txt')

    label_json = {}
    label_json['info'] = {'description':'YOLO Dataset', 'url':None, 'version':None, 'contributor':'rauleun', 'date created':date.today().isoformat()}
    label_json['licenses'] = [{'url' : None, 'id':1, 'name':'github.com/rauleun/yolo2coco'}]
    label_json['images'] = []
    label_json['annotations'] = []
    
    img_count = 1
    annt_count = 1
    
    for image_path in tqdm(image_list):
        #time.sleep(0.1)
        json_img = {}
        json_img['license'] = 1
        json_img['file_name'] = image_path.split('/')[-1]
        json_img['coco_url'] = None
        img = cv2.imread(image_path)
        height, width, _ = img.shape 
        json_img['height'] = height
        json_img['width'] = width
        json_img['date_captured'] = None
        json_img['flickr_url'] = None
        json_img['id'] = img_count
        label_json['images'].append(json_img)
        
        with open(os.path.join(path_base, args.data_path, image_path.split('/')[-1][:-3]+'txt')) as f_annt:
            while True:
                line_annt = f_annt.readline()
                if not line_annt: break

                annt_cls, annt_x, annt_y, annt_w, annt_h = line_annt.split()
                annt_x = width * float(annt_x)
                annt_w = width * float(annt_w)
                annt_y = height * float(annt_y)
                annt_h = height * float(annt_h)
               
                json_annt = {}
                json_annt['segmentation'] = None
                json_annt['area'] = annt_w * annt_h
                json_annt['iscrowd'] = None
                json_annt['image_id'] = img_count
                bbox = [annt_x - annt_w/2, annt_y-annt_h/2, annt_w, annt_h]
                if((bbox[0] < 0) or (bbox[1]<0)):
                    bbox[0] = max(0, bbox[0])
                    bbox[1] = max(0, bbox[1])
                json_annt['bbox'] = bbox
                json_annt['category_id'] = annt_cls
                json_annt['id'] = annt_count
                label_json['annotations'].append(json_annt)
                annt_count += 1
        img_count += 1
    
    label_json['categories'] = []
    with open(os.path.join(path_base, args.cls_path)) as f_cls:
        cls_count = 0
        while True:
            line_cls = f_cls.readline()
            if not line_cls: break
            cls = line_cls[:-1]
            cls_annt = {}
            cls_annt['supercategory'] = cls
            cls_annt['id'] = cls_count
            cls_annt['name'] = cls
            label_json['categories'].append(cls_annt)
            cls_count += 1
    
    with open(os.path.join(args.output_path, 'annotations', 'label.json'), "w+") as json_file:
        json.dump(label_json, json_file, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Conversion script', parents = [get_args_parser()])
    args = parser.parse_args()
    main(args)


