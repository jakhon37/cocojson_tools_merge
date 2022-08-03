import datetime
import json
import os

local_path = './json_sample/'
json_file = 'custom_multy_coco.json'
# new_json_path = './new_json'
new_json_path = './'
file_format = '.json'
new_json_file_name = 'custom_multy_coco'

# infos = []  # for multiple infos
images = []
annotations = []
# categories = []  # for multiple categories
num_found_files = 0


def find_json_a(json_path):
    with open(json_path) as f:
        js = json.load(f)

        s_infos = js['info']
        s_images = js['images']
        s_categories = js['categories']
        s_annotations = js['annotations']

        print('\nFILE < ' + str(num_found_files) + ' > details: ')
        # print('info: ' + str(len(source_infos)))
        # print('images: ' + str(len(source_images)))
        # print('annotations: ' + str(len(source_annotations)))
        # print('categories: ' + str(len(source_categories)))

        file_desc = s_infos['description']
        # print(f'file code is : {file_desc[1:33]}')
        # print(f'file type : {file_desc[33:47]}')
        if file_desc[33:47] == 'BBOX JSON file':
            print(f'file type is :{file_desc[33:47]}')
            print(f'file code is : {file_desc[1:33]}')
            jsonAtype = file_desc[33:47]
            jsonAcode = file_desc[1:33]

        else:
            print(f'did not match < BBOX JSON file >')
            jsonAcode = file_desc[1:33]
            jsonAtype = file_desc[33:47]


    return jsonAtype, jsonAcode, s_infos, s_images, s_categories, s_annotations

def find_json_b(json_path):
    with open(json_path) as f2:
        js2 = json.load(f2)

        source_infos2 = js2['info']
        source_images2 = js2['images']
        source_categories2 = js2['categories']
        source_annotations2 = js2['annotations']

        print('\nFILE < ' + str(num_found_files) + ' > details: ')
        # print('info: ' + str(len(source_infos2)))
        # print('images: ' + str(len(source_images2)))
        # print('annotations: ' + str(len(source_annotations2)))
        # print('categories: ' + str(len(source_categories2)))

        file_desc2 = source_infos2['description']
        # print(f'second file code is : {file_desc2[1:33]}')
        # print(f'second file type : {file_desc2[33:47]}')
        if file_desc2[33:47] == 'PGON JSON file':
            print(f'second file code is : {file_desc2[1:33]}')
            print(f'file type is :{file_desc2[33:47]}')
            jsonBtype = file_desc2[33:47]
            jsonBcode = file_desc2[1:33]

        else:
            print(f'did not match < PGON JSON file >')
            jsonBcode = file_desc2[1:33]
            jsonBtype = file_desc2[33:47]

    return jsonBtype, jsonBcode, source_infos2, source_images2, source_categories2, source_annotations2

for file in os.listdir(local_path):
    num_found_files += 1
    # If file is a json, construct it's full path and open it, append all json data to list
    if 'json' in file:
        json_path = os.path.join(local_path, file)



        aa = find_json_a(json_path)
        aa_code = aa[1]
        aa_type = aa[0]
        # print(f'return form function a: {aa_code}')
        if aa_type == 'BBOX JSON file':
            print(f'file {aa_code}{aa_type}')
            with open(json_path) as f:
                js = json.load(f)

                s_infos = js['info']
                s_images = js['images']
                s_categories = js['categories']
                s_annotations = js['annotations']

                print('\nFILE < ' + str(num_found_files) + ' > details: ')
                file_desc = s_infos['description']
                # print(f'file code is : {file_desc[1:33]}')
                print(f'file type AAA : {file_desc[33:47]}')

        bb = find_json_b(json_path)
        bb_code = bb[1]
        bb_type = bb[0]
        # print(f'return form function b: {bb_code}')

        # if bb_code == aa_code and aa_type != bb_type:
        #     print(f'they are the same picture')
        # else:
        #     print(f'not the target ')


        #
        # with open(json_path) as f2:
        #     js2 = json.load(f2)
        #
        #     source_infos2 = js2['info']
        #     source_images2 = js2['images']
        #     source_categories2 = js2['categories']
        #     source_annotations2 = js2['annotations']
        #
        #     print('\nFILE < ' + str(num_found_files) + ' > details: ')
        #     print('info: ' + str(len(source_infos2)))
        #     print('images: ' + str(len(source_images2)))
        #     print('annotations: ' + str(len(source_annotations2)))
        #     print('categories: ' + str(len(source_categories2)))
        #
        #     file_desc2 = source_infos2['description']
        #     print(f'second file code is : {file_desc2[1:33]}')
        #     print(f'second file last : {file_desc2[33:47]}')
        #     if file_desc2[33:47] == 'PGON JSON file':
        #         print(f'file type is :{file_desc2[33:47]}')
        #     else:
        #         print(f'did not match < PGON JSON file >')

        source_infos = aa[2]
        source_images = aa[3]
        source_annotations = aa[5]
        source_categories = aa[4]

        # INFO
        infos = []  # for single info
        # for inf in source_infos:
        inf = source_infos

        info = {"description": inf["description"], "url": inf["url"], "version": inf["version"],
                "year": inf["year"], "contributor": inf["contributor"], "date_created": inf["date_created"]
                }
        infos.append(info)

        #  IMAGES
        # for img in source_images:
        img = source_images

        image = {"file_name": img["file_name"], "id": img["id"], "width": img["width"],
                 "height": img["height"]}
        images.append(image)

        # ANNOTATIONS
        for ant in source_annotations:
            annotation = {"segmentation": ant["segmentation"], "image_id": ant["image_id"],
                          # "polyline": ant["polyline"],
                          "bbox": ant["bbox"], "category_id": ant["category_id"], "area": ant["area"],
                          "iscrowd": ant["is_crowd"], "id": ant["id"]}
            annotations.append(annotation)

        # CATEGORIES
        categories = []  # for single category
        for ctg in source_categories:
            category = {"id": ctg["id"], "name": ctg["name"],
                        # "polyline": ctg["polyline"],
                        # "id": ctg["id"]
                        # "supercategory": ctg["supercategory"], "color": ctg["color"], "metadata": ctg["metadata"],
                        # "keypoint_colors": ctg["keypoint_colors"]
                        }
            categories.append(category)
        # infos = 'infos'
        dd = {'images': images, 'annotations': annotations, 'categories': categories, 'infos': infos}

print(f'  \n {num_found_files} files has been merged :) \n')

# creating new file name with date attached
now = datetime.datetime.now()
currentDate = "_" + str(now.day) + "_" + str(now.hour) + "_" + str(now.minute) + "_" + str(now.second)
file_output = os.path.join(new_json_file_name + currentDate + file_format)

# writing file
for file in os.listdir(new_json_path):
    with open(new_json_path + file_output, 'a+') as outfile:
        json.dump(dd, outfile, sort_keys=True, indent=4, )  # , indent=4, im.__dict__
        outfile.write('\n')
        outfile.close()
print(f'    Location:  {new_json_path}  \n Output file:  {file_output} \n')



