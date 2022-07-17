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
for file in os.listdir(local_path):
    num_found_files += 1
    # If file is a json, construct it's full path and open it, append all json data to list
    if 'json' in file:
        json_path = os.path.join(local_path, file)
        with open(json_path) as f:
            js = json.load(f)

            source_infos = js['info']
            source_images = js['images']
            source_categories = js['categories']
            source_annotations = js['annotations']

            print('\nFILE < ' + str(num_found_files) + ' > details: ')
            print('info: ' + str(len(source_infos)))
            print('images: ' + str(len(source_images)))
            print('annotations: ' + str(len(source_annotations)))
            print('categories: ' + str(len(source_categories)))

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



