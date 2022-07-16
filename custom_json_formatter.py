import json

local_path = './custom_json/'
coco_json = 'e_motor_val.json'
coco_json_file = local_path + coco_json

new_json_file = 'custom_json_labels.json'

open(local_path + new_json_file, 'w').close()

label_att = 'annotations'


class Json_line:
    def __init__(self, img, ant, ctg):
        # Get image info. Annotations are dealt with separately

        ############## IMAGES
        images = []
        for img in img:
            image = {"file_name": img["file_name"], "id": img["id"], "width": img["width"],
                     "height": img["height"]}
            images.append(image)

        ############## ANNOTATIONS
        annotations = []
        for ant in ant:
            annotation = {"segmentation": ant["segmentation"], "image_id": ant["image_id"],
                          # "polyline": ant["polyline"],
                          "bbox": ant["bbox"], "category_id": ant["category_id"], "area": ant["area"],
                          "iscrowd": ant["iscrowd"], "id": ant["id"]}
            annotations.append(annotation)

        ############## CATEGORIES
        # categories = []
        for ctg in ctg:
            category = {"id": ctg["id"], "name": ctg["name"],
                        # "polyline": ctg["polyline"],
                        # "id": ctg["id"]
                        "supercategory": ctg["supercategory"], "color": ctg["color"], "metadata": ctg["metadata"],
                        "keypoint_colors": ctg["keypoint_colors"]}
            # categories.append(category)

        self.__dict__['images'] = images
        self.__dict__["annotations"] = annotations
        self.__dict__["categories"] = category  # categories


# open source json annotation file and print number of objects
with open(coco_json_file) as f:
    js = json.load(f)
    source_images = js['images']
    source_categories = js['categories']
    source_annotations = js['annotations']

    print('Images: ' + str(len(source_images)))
    print('annotations: ' + str(len(source_annotations)))
    print('categories: ' + str(len(source_categories)))

# get source objects and feed them into class Json_line to process
im = Json_line(source_images, source_annotations, source_categories)

print('Writing Custom Labels manifest...')
# write new json file with new format
with open(local_path + new_json_file, 'a+') as outfile:
    # print(f' OUTFILE: ==== {outfile}')
    json.dump(im.__dict__, outfile)
    outfile.write('\n')
    outfile.close()

print(f' Outfile: == {new_json_file} // Location: == {local_path}')
