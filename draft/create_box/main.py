import json
from PIL import Image, ImageDraw

coco_json_file = 'road_ant_bbox.json'

with open(coco_json_file) as f:
    data = json.load(f)

print(f'print file name before { data["images"]["file_name"] } ')

data["images"]["file_name"] = 'road_img.png'       # my image - only for tests
print(f'print file name { data["images"]["file_name"] } ')

img = Image.open(data["images"]["file_name"])
# img = img.resize((1900, 1200))        # resize - only for tests

draw = ImageDraw.Draw(img)

for item in data["annotations"]:
    area = item["area"]
	aa =  item["segmentation"] 
	print(aa)
	
	# print(f'seg value: { item["segmentation"] }')

#     for i in item["segmentation"]:
# 	    print(i)
# print('poligon values: { xy }')
# #     draw.rectangle([x, y, x+w, y+h], outline='green', width=2)
#     # draw.text([x, y-10], text)
# img.polygon(xy, fill ="# eeeeff", outline ="blue") 

# print(f'area { area }')
# # print(f'bbox values { x, y, w, h }')

# img.show()
# img.save('result.jpg')