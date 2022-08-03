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
            print('\nFILE < A ' + str(num_found_files) + ' > details: ')
            s_infos = js['info']
            file_desc = s_infos['description']
            # print(f'file A code is : {file_desc[1:33]}')
            print(f'file type  : {file_desc[33:47]}')
            source_imagesB = js['images']
            print('images: ' + str(len(source_imagesB)))
            for _ in source_imagesB:
                if _ == 'file_name':
                    print(f'file name is {source_imagesB[_]}')

            source_annotationsB = js['annotations']
            print('annotations: ' + str(len(source_annotationsB)))



            #
            # if file_desc[33:47] == 'PGON JSON file':
            #     print(f'file B type: {file_desc[33:47]}')
            #
            #     # JSON B
            #
            #     with open(json_path) as f:
            #         jsB = json.load(f)
            #
            #         source_imagesB = jsB['images']
            #         print('images: ' + str(len(source_imagesB)))
            #         for _ in source_imagesB:
            #             if _ == 'file_name':
            #                 print(f'file name is {source_imagesB[_]}')
            #
            #         source_annotationsB = jsB['annotations']
            #         print('annotations: ' + str(len(source_annotationsB)))
            #         for _b in source_annotationsB:
            #             for ib in _b:
            #                 if ib == 'bbox':
            #                     if ib == _b[ib] >= 0:
            #                         print(f' list values inside bbox {_b[ib]}')
            #                     else:
            #                         # print(f'no valid bbox value {_b[ib] }')
            #                         bboxB_list = _b[ib]
            #
            #         print(f' json b bbox list {bboxB_list}')
            #         print('json b is done \n')
            #
