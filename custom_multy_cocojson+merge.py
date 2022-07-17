import datetime
import json
import os

local_path = './custom_json/'
json_file = 'custom_multy_json.json'

new_json_path = './custom_json_new/'
new_json_file = 'custom_multy_json2.json'
new_json_file2 = '_coco.json'
new_json_file1 = 'custom_multy'

images = []
annotations = []
# categories = []  # for multiple categories

for file in os.listdir(local_path):
    # If file is a json, construct it's full path and open it, append all json data to list
    if 'json' in file:
        json_path = os.path.join(local_path, file)
        with open(json_path) as f:
            js = json.load(f)
            source_images = js['images']
            source_categories = js['categories']
            source_annotations = js['annotations']

            print('images: ' + str(len(source_images)))
            print('annotations: ' + str(len(source_annotations)))
            print('categories: ' + str(len(source_categories)))

        #  IMAGES
        for img in source_images:
            image = {"file_name": img["file_name"], "id": img["id"], "width": img["width"],
                     "height": img["height"]}
            images.append(image)

        # ANNOTATIONS
        for ant in source_annotations:
            annotation = {"segmentation": ant["segmentation"], "image_id": ant["image_id"],
                          # "polyline": ant["polyline"],
                          "bbox": ant["bbox"], "category_id": ant["category_id"], "area": ant["area"],
                          "iscrowd": ant["iscrowd"], "id": ant["id"]}
            annotations.append(annotation)

        # CATEGORIES
        categories = []  # for single category
        for ctg in source_categories:
            category = {"id": ctg["id"], "name": ctg["name"],
                        # "polyline": ctg["polyline"],
                        # "id": ctg["id"]
                        "supercategory": ctg["supercategory"], "color": ctg["color"], "metadata": ctg["metadata"],
                        "keypoint_colors": ctg["keypoint_colors"]}
            categories.append(category)

        dd = {'images': images, 'annotations': annotations, 'categories': categories}

print('Overwriting Custom Labels manifest...')
# write new json file with new format
for file in os.listdir(new_json_path):
    if file == json_file:
        print('file exist ------ ')
        now = datetime.datetime.now()
        currentDate = "_" + str(now.day) + "_" + str(now.hour) + "_" + str(now.minute)+ "_" + str(now.second)
        file_output = os.path.join(new_json_file1 + currentDate + new_json_file2)
        with open(new_json_path + file_output, 'a+') as outfile:
            json.dump(dd, outfile, sort_keys=True, indent=4, )  # , indent=4, im.__dict__
            outfile.write('\n')
            outfile.close()
            print(f' Outfile: == {json_file} // Location: == {new_json_path} \n')
    else:
        print(' no file found ------ ')
        with open(new_json_path + json_file, 'a+') as outfile:
            json.dump(dd, outfile, sort_keys=True, indent=4, )  # , indent=4, im.__dict__
            outfile.write('\n')
            outfile.close()
            print(f' Outfile: == {json_file} // Location: == {new_json_path} \n')

