import json
import os

local_path = './custom_json/'
json_file = 'custom_multy_json.json'

new_json_path = './custom_json_new/'
new_json_file = 'custom_multy_json2.json'

# infos = []  # for multiple infos
images = []
annotations = []
# categories = []  # for multiple categories

for file in os.listdir(local_path):
    # If file is a json, construct it's full path and open it, append all json data to list
    if 'json' in file:
        json_path = os.path.join(local_path, file)
        with open(json_path) as f:
            js = json.load(f)

            source_infos = js['infos']
            source_images = js['images']
            source_categories = js['categories']
            source_annotations = js['annotations']

            print('images: ' + str(len(source_images)))
            print('images: ' + str(len(source_images)))
            print('annotations: ' + str(len(source_annotations)))
            print('categories: ' + str(len(source_categories)))


        # INFO
        infos = []  # for single info
        for inf in source_infos:
            info = {"description": inf["description"], "url": inf["url"], "version": inf["version"],
                         "year": inf["year"], "contributor": inf["contributor"], "date_created": inf["date_created"]
                    }
            infos.append(inf)

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

        dd = {'images': images, 'annotations': annotations, 'categories': categories, 'infos': infos}

print('Overwriting Custom Labels manifest...')
# write new json file with new format
with open(new_json_path + json_file, 'a+') as outfile:
    # print(f' OUTFILE: ==== {outfile}')
    json.dump(dd, outfile, sort_keys=True, indent=4, )  # , indent=4, im.__dict__
    outfile.write('\n')
    outfile.close()
    print(f' Outfile: == {json_file} // Location: == {new_json_path} \n')

