import datetime
import json
import os

local_path = './json_sample/'
json_file = 'custom_multy_coco.json'
# new_json_path = './new_json'
new_json_path = './'
file_format = '.json'
new_json_file_name = 'custom_multy_coco'

new_json_file = 'custom_json_seg_bbox_merged.json'

open(new_json_path + new_json_file, 'w').close()

json1 = '201213_E_14_CCW_in_E_B_002_02589_BBOX.json'
json2 = '201213_E_14_CCW_in_E_B_002_02589_PGON.json'

pathA = local_path + json1
pathB = local_path + json2


def compare_json(jsonA, jsonB):

    # JSON A
    with open(jsonA) as f:
        jsA = json.load(f)
        source_annotationsA = jsA['annotations']
        print('annotations: ' + str(len(source_annotationsA)))
        for _ in source_annotationsA:
            for i in _:
                # print(_[i])
                list_bbox = []
                if i == 'bbox' and _[i][0] > 0:
                    list_bbox.append(_[i])
                    # print(f' list values inside bbox {_[i]}')
                    bboxA_list = _[i]
                if i == 'id':
                    # print(f' list values inside bbox {_[i]}')
                    bboxA_id_list = _[i]



                    # print(f'list {list_bbox}')
                    # print(f'first list {_[i][0]}')
                    # for i in _[i]:
                    #     print(f' list values inside bbox {i}')
                    # print(f' found box {i, _[i]}')
        print(f' json a bbox list {bboxA_list} and id number {bboxA_id_list}')
        print('json a is done \n')

    # JSON B

    with open(jsonB) as f:
        jsB = json.load(f)
        source_annotationsB = jsB['annotations']
        print('annotations: ' + str(len(source_annotationsB)))
        for _b in source_annotationsB:
            for ib in _b:
                if ib == 'bbox':
                    if ib == _b[ib] >= 0:
                        print(f' list values inside bbox {_b[ib]}')
                    else:
                        # print(f'no valid bbox value {_b[ib] }')
                        bboxB_list = _b[ib]

        print(f' json a bbox list {bboxB_list}')
        print('json b is done \n')

if __name__ == "__main__":
    compare_json(pathA, pathB)
