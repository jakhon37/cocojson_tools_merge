import json
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('road_img.png')  # read image
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # convert rgb to bgr
print('Original Dimensions : ', img.shape)
coco_json_file = 'road_ant_pgon.json'  # read json annotation file


def sort_poly_value(seg_list_p):  # function - get the segmentation values from cocojson file and plot it on image
    x_seg_coords, y_seg_coords = [], []  # store x and v values of seg list in different lists
    for i in range(0, len(seg_list_p), 2):  # iterate seg list values and choose first value and skip second
        x_seg_coords.append(seg_list_p[i])  # append the extracted odd values to the list
    for i in range(1, len(seg_list_p), 2):  # iterate seg list values and choose second value and skip third
        y_seg_coords.append(seg_list_p[i])  # append the extracted even values to the list
    zipped = zip(x_seg_coords, y_seg_coords)  # zip the two files together
    poly_list_for_cv2 = [list(ele) for ele in zipped]  # iterate zipped list  and make a list for cv2 poligon
    return poly_list_for_cv2  # return list


def poly_to_bbox(seg_list_b):
    xcoords, ycoords = [], []
    for i in range(0, len(seg_list_b), 2):
        xcoords.append(seg_list_b[i])
    for i in range(1, len(seg_list_b), 2):
        ycoords.append(seg_list_b[i])
    xmax, ymin = int(max(xcoords)), int(min(ycoords))
    ymax, xmin = int(max(ycoords)), int(min(xcoords))
    poly_bbox = [xmax, ymin, ymax, xmin]
    width, height = xmax - xmin, ymax - ymin
    return [xmin, ymin, width, height]


with open(coco_json_file) as f:
    data = json.load(f)
print(f'print file name in json: {data["images"]["file_name"]} ')
data["images"]["file_name"] = 'road_img.png'  # my image - only for tests
print(f'print file name: {data["images"]["file_name"]} ')

for item in data["annotations"]:
    area = item["area"]
    seg_list = item["segmentation"]

    bbox = poly_to_bbox(seg_list[0])
    xmin, ymin, w, h = bbox
    img_mod = cv2.rectangle(img, (xmin, ymin), ((xmin + w), (ymin + h)), (255, 0, 0), 2)

    poli_ll = sort_poly_value(seg_list[0])
    res = np.array(poli_ll, np.int32)
    img_mod = cv2.polylines(img, [res], True, (255, 120, 255), 3)
plt.figure(figsize=(200, 20))
imgplot = plt.imshow(img_mod)
plt.show()
