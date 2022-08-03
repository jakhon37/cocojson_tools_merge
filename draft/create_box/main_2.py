import json
from PIL import Image, ImageDraw
from PIL._imaging import display
import numpy as np
import cv2
from matplotlib import pyplot as plt

coco_json_file = 'road_ant_pgon.json'

with open(coco_json_file) as f:
    data = json.load(f)

print(f'print file name before {data["images"]["file_name"]} ')

data["images"]["file_name"] = 'road_img.png'  # my image - only for tests
print(f'print file name {data["images"]["file_name"]} ')

img = Image.open(data["images"]["file_name"])
# img = img.resize((1900, 1200))        # resize - only for tests

draw = ImageDraw.Draw(img)

for item in data["annotations"]:
    area = item["area"]
    aa = item["segmentation"]  # [0]
    #     print(f'seg value: { item["segmentation"] }')
    for i in (aa):
        x_values = []
        y_values = []

        for x, y in enumerate(i):
            #             print(f' count: {x} value: {y} ')
            if x % 2 == 1:
                y_values.append(y)
            #                 print(f' y_values {y} ')
            else:
                x_values.append(y)
        #                 print(f' x_values { y } ')
        #                 print(f' count { x } ')
        #                 print(f' count { x/2 } ')
        #         print(f' x values {x_values} ')
        #         print(f' y values {y_values} ')

        zipped = zip(x_values, y_values)
        z_v = list(zipped)
        print(f' zipped values2 {z_v} ')
# print(z_v)
# print("The original list of tuples : " + str(z_v))

        # using list comprehension
        # convert list of tuples to list of list
        res = [list(ele) for ele in z_v]
        print(res)
        res = np.array([res], np.int32)
        # print(f'resss { res } res')


        img = cv2.imread(data["images"]["file_name"])

        # img = np.zeros((512, 512, 3), dtype = "uint8")
        # img = cv2.imread('white_img.png')

        print('Original Dimensions : ', img.shape)

        scale_percent = 260  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        img2 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


        penta = np.array([[[40,160],[120,100],[200,160],[160,240],[80,240]]], np.int32)
        triangle = np.array([[[240, 130], [380, 230], [190, 280]]], np.int32)
        # cv2.polylines(img, [triangle], True, (0,255,0), thickness=3)

        img_mod = cv2.polylines(img, [res], True, (255,120,255),3)

        imgplot = plt.imshow(img_mod)
        plt.show()
        # cv2.imshow('Shapes', img_mod)
        #
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

# display(img)

# img.show()
#             print(x, y)
# print('poligon values: { xy }')
# #     draw.rectangle([x, y, x+w, y+h], outline='green', width=2)
#     # draw.text([x, y-10], text)
# img.polygon(i, fill ="# eeeeff", outline ="blue")

# print(f'area { area }')
# # print(f'bbox values { x, y, w, h }')

# img.show()
# img.save('result.jpg')
