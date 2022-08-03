import datetime
import json
import os

local_path = './json_sample/'
json_file = 'custom_multy_coco.json'
# new_json_path = './new_json'
new_json_path = './'
file_format = '.json'
new_json_file_name = 'custom_multy_coco'

new_json_file = 'custom_json_seg_bbox_merged.json'

open(new_json_path + new_json_file, 'w').close()

json1 = '201213_E_14_CCW_in_E_B_002_02589_BBOX.json'
json2 = '201213_E_14_CCW_in_E_B_002_02589_PGON.json'

jsonA = local_path + json1
jsonB = local_path + json2

# JSON A
with open(jsonA) as f:
    jsA = json.load(f)
    source_imagesA = jsA['images']
    print('images: ' + str(len(source_imagesA)))
    for _ in source_imagesA:
        if _ == 'file_name':
            print(f'file name is {source_imagesA[_]}')

    source_annotationsA = jsA['annotations']
    print('annotations: ' + str(len(source_annotationsA)))
    for _ in source_annotationsA:
        for i in _:
            # print(_[i])
            list_bbox = []
            if i == 'bbox' and _[i][0] > 0:
                list_bbox.append(_[i])
                # print(f' list values inside bbox {_[i]}')
                bboxA_list = _[i]

                # print(f'list {list_bbox}')
                # print(f'first list {_[i][0]}')
                # for i in _[i]:
                #     print(f' list values inside bbox {i}')
                # print(f' found box {i, _[i]}')
    print(f' json a bbox list {bboxA_list}')
    print('json a is done \n')

# JSON B

with open(jsonB) as f:
    jsB = json.load(f)

    source_imagesB = jsB['images']
    print('images: ' + str(len(source_imagesB)))
    for _ in source_imagesB:
        if _ == 'file_name':
            print(f'file name is {source_imagesB[_]}')

    source_annotationsB = jsB['annotations']
    print('annotations: ' + str(len(source_annotationsB)))
    for _b in source_annotationsB:
        for ib in _b:
            if ib == 'bbox':
                if ib == _b[ib] >= 0:
                    print(f' list values inside bbox {_b[ib]}')
                else:
                    # print(f'no valid bbox value {_b[ib] }')
                    bboxB_list = _b[ib]

    print(f' json a bbox list {bboxB_list}')
    print('json b is done \n')


class Json_line:
    def __init__(self, img, ant, ctg, jsonA):
        # Get image info. Annotations are dealt with seperately
        annotations = []
        with open(jsonA) as f:
            jsA = json.load(f)

            source_imagesA = jsA['images']
            print('images: ' + str(len(source_imagesA)))
            for _ in source_imagesA:
                if _ == 'file_name':
                    print(f'file name is {source_imagesA[_]}')
                    bboxA_name = source_imagesA[_]


            source_annotationsA = jsA['annotations']
            print('annotations: ' + str(len(source_annotationsA)))

            for _ in source_annotationsA:
                for i in _:
                    # print(_[i])
                    # if i == 'bbox' and _[i][0] > 0:
                    if i == 'bbox':
                        bboxA_list = _[i]
                    if i == 'id':
                        bboxA_id = _[i]

                        # print(f' list values inside bbox {bboxA_list}')
                        ############## ANNOTATIONS


                        for a in ant:
                            if a["id"] == bboxA_id:
                                # print(f'same annotations: {bboxA_id}')
                                # print(a["image_id"])
                                annotation = {"segmentation": a["segmentation"], "image_id": a["image_id"],
                                                          # "polyline": ant["polyline"],
                                                          "bbox": bboxA_list, "category_id": a["category_id"], "area": a["area"],
                                                          "iscrowd": a["is_crowd"], "id": a["id"]}
                                annotations.append(annotation)



                                ############## IMAGES
                                images = []
                                # for img in img:
                                image = {"file_name": img["file_name"], "id": img["id"], "width": img["width"],
                                         "height": img["height"]}
                                images.append(image)

                                ############## CATEGORIES
                                categories = []
                                for ct in ctg:
                                    category = {"id": ct["id"], "name": ct["name"],
                                                # "polyline": ctg["polyline"],
                                                # "id": ctg["id"]
                                                # "supercategory": ctg["supercategory"], "color": ctg["color"], "metadata": ctg["metadata"],
                                                # "keypoint_colors": ctg["keypoint_colors"]
                                                }
                                    categories.append(category)

                self.__dict__['images'] = images
                self.__dict__["annotations"] = annotations
                self.__dict__["categories"] = categories  # categories


# open source json annotation file and print number of objects
with open(jsonB) as f:
    js = json.load(f)
    source_images = js['images']
    source_categories = js['categories']
    source_annotations = js['annotations']

    print('images: ' + str(len(source_images)))
    print('annotations: ' + str(len(source_annotations)))
    print('categories: ' + str(len(source_categories)))

# get source objects and feed them into class Json_line to process
im = Json_line(source_images, source_annotations, source_categories, jsonA)

print('Writing Custom Labels manifest...')
# write new json file with new format
with open(new_json_path + new_json_file, 'a+') as outfile:
    # print(f' OUTFILE: ==== {outfile}')
    json.dump(im.__dict__, outfile, sort_keys=True, indent=4)
    outfile.write('\n')
    outfile.close()

print(f' Outfile: == {new_json_file} // Location: == {new_json_path}')


print(f'  \n 2 files has been merged :) \n')

# creating new file name with date attached
now = datetime.datetime.now()
currentDate = "_" + str(now.day) + "_" + str(now.hour) + "_" + str(now.minute) + "_" + str(now.second)
file_output = os.path.join(new_json_file_name + currentDate + file_format)

# writing file
for file in os.listdir(new_json_path):
    with open(new_json_path + file_output, 'a+') as outfile:
        json.dump(im.__dict__, outfile, sort_keys=True, indent=4, )  # , indent=4, im.__dict__
        outfile.write('\n')
        outfile.close()
print(f'    Location:  {new_json_path}  \n Output file:  {file_output} \n')

