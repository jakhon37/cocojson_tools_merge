import json
# from PIL import Image, ImageDraw
# from PIL._imaging import display
import numpy as np
import cv2
from matplotlib import pyplot as plt

coco_json_file = 'road_ant_pgon.json'

with open(coco_json_file) as f:
    data = json.load(f)
    # print(data)
# data["images"]["file_name"] = 'road_img.png'  # my image - only for tests
# img = cv2.imread(data["images"]["file_name"])
img = cv2.imread('road_img.png')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
print('Original Dimensions : ', img.shape)

print(f'print file name before {data["images"]["file_name"]} ')

data["images"]["file_name"] = 'road_img.png'  # my image - only for tests
print(f'print file name {data["images"]["file_name"]} ')


def read_poly(poly):
    x_values = []
    y_values = []
    res = []
    for i in (aa):
        x_values_s = []
        y_values_s = []

        for x, y in enumerate(i):
            #             print(f' count: {x} value: {y} ')
            if x % 2 == 1:
                y_values_s.append(y)
            #                 print(f' y_values {y} ')
            else:
                x_values_s.append(y)
        #                 print(f' x_values { y } ')
        #                 print(f' count { x } ')
        #                 print(f' count { x/2 } ')

        #         print(f' x values -s {x_values_s} ')
        #         print(f' y values -s {y_values_s} ')

        zipped = zip(list(x_values_s), list(y_values_s))
        z_v = list(zipped)
        #         print(' zv list')
        #         print( z_v)
        reslist = []
        for ele in z_v:
            #             print(ele)
            list(ele)

            reslist.append(list(ele))
        res.append(reslist)
        return res

#
# def poly_to_bbox(aa):
#     xcoords, ycoords = [], []
#     for i in range(0, len(aa), 2):
#         xcoords.append(aa[i])
#     for i in range(1, len(aa), 2):
#         ycoords.append(aa[i])
#
#     xmax, ymin = int(max(xcoords)), int(min(ycoords))
#     #     print(f'print xmax {xmax} print ymin {ymin} ')
#
#     ymax, xmin = int(max(ycoords)), int(min(xcoords))
#     #     print(f'print xmax {xmax} print ymin {ymin} ')
#
#     poly_bbox = [xmax, ymin, ymax, xmin]
#     #     print(poly_bbox, "poly_bbox")
#     width, height = xmax - xmin, ymax - ymin
#
#     return [xmin, ymin, width, height]


for item in data["annotations"]:
    area = item["area"]
    aa = item["segmentation"]
    #     print(aa)
    # bbox = poly_to_bbox(aa[0])
    # xmin, ymin, w, h = bbox
    poli_ll = read_poly(aa)

    # img_mod = cv2.rectangle(img, (xmin, ymin), ((xmin + w), (ymin + h)), (255, 0, 0), 2)

    res = np.array(poli_ll, np.int32)
    img_mod = cv2.polylines(img, [res], True, (255, 120, 255), 3)
plt.figure(figsize=(200, 20))
imgplot = plt.imshow(img_mod)
plt.show()
