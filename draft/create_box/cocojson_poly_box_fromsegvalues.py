import json

local_path = './'
coco_json = 'road_ant_pgon.json'
coco_json_file = local_path + coco_json

new_json_file = 'custom_json.json'

open(local_path + new_json_file, 'w').close()



class Json_line:



    def __init__(self, img, ant, ctg):
        # Get image info. Annotations are dealt with seperately

        ############## IMAGES
        images = []
        # for img in img:
        img = img

        image = {"file_name": img["file_name"], "id": img["id"], "width": img["width"],
                     "height": img["height"]}
        images.append(image)
        print(f'file_name { img["file_name"] } ')

        ############## ANNOTATIONS
        annotations = []
        for ant_i in ant:

            for ant_i in ant:
                area = ant_i["area"]
                seg_list = ant_i["segmentation"][0]
                xcoords, ycoords = [], []
                for i in range(0, len(seg_list), 2):
                    xcoords.append(seg_list[i])
                for i in range(1, len(seg_list), 2):
                    ycoords.append(seg_list[i])
                xmax, ymin = float(max(xcoords)), float(min(ycoords))
                ymax, xmin = float(max(ycoords)), float(min(xcoords))
                # poly_bbox = [xmax, ymin, ymax, xmin]
                width, height = xmax - xmin, ymax - ymin
                bbox_values = xmin, ymin, width, height
                # print(f' bbox_values list {bbox_values}')

                annotation = {"segmentation": ant_i["segmentation"], "image_id": ant_i["image_id"],
                              # "polyline": ant["polyline"],
                              "bbox": [bbox_values], "category_id": ant_i["category_id"], "area": ant_i["area"],
                              "iscrowd": ant_i["is_crowd"], "id": ant_i["id"]}
                annotations.append(annotation)

        ############## CATEGORIES
        categories = []
        for ctg_i in ctg:
            category = {"id": ctg_i["id"], "name": ctg_i["name"],
                        # "polyline": ctg["polyline"],
                        # "id": ctg["id"]
                        # "supercategory": ctg["supercategory"], "color": ctg["color"], "metadata": ctg["metadata"],
                        # "keypoint_colors": ctg["keypoint_colors"]
                        }
            categories.append(category)

        self.__dict__['images'] = images
        self.__dict__["annotations"] = annotations
        self.__dict__["categories"] = categories    # categories


# open source json annotation file and print number of objects
with open(coco_json_file) as f:
    js = json.load(f)
    source_images = js['images']
    source_categories = js['categories']
    source_annotations = js['annotations']
    # print(source_annotations)
    # i_s = source_annotations[3]
    # i_seg = i_s['segmentation'][0]
    # print(i_seg)

    print('images: ' + str(len(source_images)))
    print('annotations: ' + str(len(source_annotations)))
    print('categories: ' + str(len(source_categories)))

# get source objects and feed them into class Json_line to process
im = Json_line(source_images, source_annotations, source_categories)

print('Writing Custom Labels manifest...')
# write new json file with new format
with open(local_path + new_json_file, 'a+') as outfile:
    # print(f' OUTFILE: ==== {outfile}')
    json.dump(im.__dict__, outfile, sort_keys=True, indent=4)
    outfile.write('\n')
    outfile.close()

print(f' Outfile: == {new_json_file} // Location: == {local_path}')
