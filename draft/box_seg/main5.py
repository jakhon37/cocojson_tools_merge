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
            if file_desc[33:47] == 'BBOX JSON file':
                with open(json_path) as f:
                    js = json.load(f)
                    s_infos = js['info']
                    s_images = js['images']
                    s_categories = js['categories']
                    s_annotations = js['annotations']

                    print('\nFILE < A ' + str(num_found_files) + ' > details: ')
                    file_desc = s_infos['description']
                    print(f'file A code is : {file_desc[1:33]}')
                    print(f'file type AAA : {file_desc[33:47]}')

        with open(json_path) as f:
            js = json.load(f)
            s_infos = js['info']
            file_desc = s_infos['description']
            if file_desc[33:47] == 'PGON JSON file':
                with open(json_path) as f:
                    js = json.load(f)
                    s_infos = js['info']
                    s_images = js['images']
                    s_categories = js['categories']
                    s_annotations = js['annotations']

                    print('\nFILE < B ' + str(num_found_files) + ' > details: ')
                    file_desc = s_infos['description']
                    print(f'file B code is : {file_desc[1:33]}')
                    print(f'file type BBB : {file_desc[33:47]}')