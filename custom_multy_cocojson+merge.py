import json
import os

local_path = './custom_json/'
json_file = 'custom_multy_json.json'
new_json_path = './custom_json_new/'


class New_json_line:
    def __init__(self, img, ant, ctg):
        # Get image info. Annotations are dealt with seperately

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
        categories = []
        for ctg in ctg:
            category = {"id": ctg["id"], "name": ctg["name"],
                        # "polyline": ctg["polyline"],
                        # "id": ctg["id"]
                        "supercategory": ctg["supercategory"], "color": ctg["color"], "metadata": ctg["metadata"],
                        "keypoint_colors": ctg["keypoint_colors"]}
            categories.append(category)

        # annotations = 'annotations'
        # categories = 'categories'

        self.__dict__['images'] = images
        self.__dict__["annotations"] = annotations
        self.__dict__["categories"] = categories  # categories


for file in os.listdir(local_path):
    # If file is a json, construct it's full path and open it, append all json data to list
    if 'json' in file:
        json_path = os.path.join(local_path, file)
        print(f" json_path ---  {json_path} ")
        with open(json_path) as f:
            js = json.load(f)
            source_images = js['images']
            source_categories = js['categories']
            source_annotations = js['annotations']

            print('images: ' + str(len(source_images)))
            print('annotations: ' + str(len(source_annotations)))
            print('categories: ' + str(len(source_categories)))
            # get source objects and feed them into class Json_line to process
            im = New_json_line(source_images, source_annotations, source_categories)

print('Overwriting Custom Labels manifest...')
# write new json file with new format
with open(new_json_path + json_file, 'a+') as outfile:
    json.dump(im.__dict__, outfile, sort_keys=True, indent=4, )
    outfile.write('\n')
    outfile.close()
    print(f'// Location: == {new_json_path} // Output-file: == {json_file} ')
    print(' ')
