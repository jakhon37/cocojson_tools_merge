import datetime
import json
import os

local_path = './json_sample/'
json_file = 'custom_multy_coco.json'
# new_json_path = './new_json'
new_json_path = './'
file_format = '.json'
new_json_file_name = 'custom_multy_coco'



# json1 = '201213_E_14_CCW_in_E_B_002_02589_BBOX.json'
# json2 = '201213_E_14_CCW_in_E_B_002_02589_PGON.json'

json1 = 'multy_coco_bbox_18_22_16_49.json'
json2 = 'multy_coco_pgon_18_22_17_56.json'

jsonA = new_json_path + json1
jsonB = new_json_path + json2

num_found_files = 0



for file in os.listdir(local_path):
    num_found_files += 1
    # If file is a json, construct it's full path and open it, append all json data to list
    if 'json' in file:
        json_path = os.path.join(local_path, file)

        with open(json_path) as f:
            js = json.load(f)
            s_infos = js['info']
            file_desc = s_infos['description']
            if file_desc[33:47] == 'PGON JSON file':
                print(f'file B type: {file_desc[33:47]}')

                # JSON B

                with open(json_path) as f:
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

                    print(f' json b bbox list {bboxB_list}')
                    print('json b is done \n')


        with open(json_path) as f:
            js = json.load(f)
            s_infos = js['info']
            file_desc = s_infos['description']
            if file_desc[33:47] == 'BBOX JSON file':
                print(f'file A type: {file_desc[33:47]}')


                # JSON A

                with open(json_path) as f:
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
                            list_seg = []
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


class Json_line:
    def __init__(self, img, ant, ctg, json_path):
        # Get image info. Annotations are dealt with seperately
        annotations = []
        print('HELLO CLASS ')

        with open(json_path) as f:
            js = json.load(f)
            s_infos = js['info']
            file_desc = s_infos['description']
            if file_desc[33:47] == 'BBOX JSON file':
                print('HI THERE ')



                with open(json_path) as f:
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
                                print(f' json a bbox list INSIDE CLASS {bboxA_list}')

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

            elif file_desc[33:47] == 'PGON JSON file':
                print('HI THERE IT IS PGON // EXPECTED BBOX')

                with open(json_path) as f:
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
                            if i == 'segmentation':
                                bboxA_list = _[i]
                                print(f' json a bbox list INSIDE CLASS {bboxA_list}')

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

for file in os.listdir(local_path):
    num_found_files += 1
    # If file is a json, construct it's full path and open it, append all json data to list
    if 'json' in file:
        json_path = os.path.join(local_path, file)

        with open(json_path) as f:
            js = json.load(f)
            s_infos = js['info']
            file_desc = s_infos['description']
            if file_desc[33:47] == 'BBOX JSON file':
                print(f'file A type: {file_desc[33:47]} GO TO CLASS')
                with open(json_path) as f:
                    js = json.load(f)
                    source_images = js['images']
                    source_categories = js['categories']
                    source_annotations = js['annotations']

                    print('images: ' + str(len(source_images)))
                    print('annotations: ' + str(len(source_annotations)))
                    print('categories: ' + str(len(source_categories)))
            else:
                print(f'no imput for class ')





 # with open(json_path) as f1:
 #     js = json.load(f1)
 #     s_infos = js['info']
 #     file_desc = s_infos['description']
 #     if file_desc[33:47] == 'BBOX JSON file':
 #        print(f'file A type: {file_desc[33:47]} GO TO CLASS')

# get source objects and feed them into class Json_line to process
        im = Json_line(source_images, source_annotations, source_categories, json_path)

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
