import json
import os


local_path = './custom_json/'
json_file = 'custom_multy_json.json'

new_json_path = './custom_json_new/'
new_json_file = 'custom_multy_json2.json'

class Json_line:
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

        self.__dict__['images'] = images
        self.__dict__["annotations"] = annotations
        self.__dict__["categories"] = categories    # categories


class New_json_line:
    def __init__(self, img, ant, ctg, c_img, c_ant, c_ctg):
        # Get image info. Annotations are dealt with seperately

        ############## IMAGES
        # images = []
        for img in img:
            image = {"file_name": img["file_name"], "id": img["id"], "width": img["width"],
                     "height": img["height"]}
            # images.append(image)
            c_img.append(image)

        ############## ANNOTATIONS
        # annotations = []
        for ant in ant:
            annotation = {"segmentation": ant["segmentation"], "image_id": ant["image_id"],
                          # "polyline": ant["polyline"],
                          "bbox": ant["bbox"], "category_id": ant["category_id"], "area": ant["area"],
                          "iscrowd": ant["iscrowd"], "id": ant["id"]}
            # annotations.append(annotation)
            c_ant.append(annotation)

        ############## CATEGORIES
        # categories = []
        for ctg in ctg:
            category = {"id": ctg["id"], "name": ctg["name"],
                        # "polyline": ctg["polyline"],
                        # "id": ctg["id"]
                        "supercategory": ctg["supercategory"], "color": ctg["color"], "metadata": ctg["metadata"],
                        "keypoint_colors": ctg["keypoint_colors"]}
            # categories.append(category)
            c_ctg.append(category)

        self.__dict__['images'] = c_img    #images
        self.__dict__["annotations"] = c_ant
        self.__dict__["categories"] = c_ctg  # categories


data_list = []
for file in os.listdir(local_path):
    # If file is a json, construct it's full path and open it, append all json data to list
    if 'json' in file:
        json_path = os.path.join(local_path, file)

        ##############################

        if os.path.isfile(new_json_path + json_file):
            print(f" File  {json_file} exist")

            with open(new_json_path + json_file) as ff:
                jss = json.load(ff)
                current_images = jss['images']
                current_categories = jss['categories']
                current_annotations = jss['annotations']

                print('Images name: ' + str(current_images[-1]['file_name']))
                print('current_Images: ' + str(len(current_images)))
                print('current_annotations: ' + str(len(current_annotations)))
                print('current_categories: ' + str(len(current_categories)))


                with open(json_path) as f:
                    js = json.load(f)
                    source_images = js['images']
                    source_categories = js['categories']
                    source_annotations = js['annotations']

                    print('Images name: ' + str(source_images[-1]['file_name']))
                    print('Images: ' + str(len(source_images)))
                    print('annotations: ' + str(len(source_annotations)))
                    print('categories: ' + str(len(source_categories)))

                    # get source objects and feed them into class Json_line to process
                    im = New_json_line(source_images, source_annotations, source_categories, current_images, current_annotations, current_categories)

                    print('Overwriting Custom Labels manifest...')
                    # write new json file with new format
                    with open(new_json_path + json_file, 'a+') as outfile:
                        # print(f' OUTFILE: ==== {outfile}')
                        json.dump(im.__dict__, outfile)
                        outfile.write('\n')
                        outfile.close()

                    print(f' Outfile: == {json_file} // Location: == {new_json_path}')
                    print(' ')







        else:
            print(f" No {json_file} yet")
            with open(json_path) as f:
                js = json.load(f)
                source_images = js['images']
                source_categories = js['categories']
                source_annotations = js['annotations']

                print('Images name: ' + str(source_images[-1]['file_name']))
                print('Images: ' + str(len(source_images)))
                print('annotations: ' + str(len(source_annotations)))
                print('categories: ' + str(len(source_categories)))

                # print('json_path: ' + str(json_path))

                # get source objects and feed them into class Json_line to process
                im = Json_line(source_images, source_annotations, source_categories)

                print('Writing New Custom Labels manifest...')
                # write new json file with new format
                with open(new_json_path + json_file, 'a+') as outfile:
                    # print(f' OUTFILE: ==== {outfile}')
                    json.dump(im.__dict__, outfile)
                    outfile.write('\n')
                    outfile.close()

                print(f' Outfile: == {json_file} // Location: == {new_json_path}')
                print(' ')
