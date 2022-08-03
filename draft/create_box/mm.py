import datetime
import json
import os

local_path = './DATA/'
json_file = 'custom_multy_coco.json'
new_json_path = './'
# new_json_path = './'
file_format = '.json'
new_json_file = 'merged_cocos.json'


def test():
    print('hello test')


class JsonAnt:
    jsonAnt = {}

    # LOAD DATA
    def __init__(self):
        # self.C = []
        self.load()

    def load(self):
        print(' Loading Coco json')
        num_found_files = 0
        for file in os.listdir(new_json_path):
            # If file is a json, construct it's full path and open it, append all json data to list
            if 'json' not in file:
                print(' Skipping, nothing to load')
                return
            try:
                json_path = os.path.join(local_path, file)
                with open(json_path) as f:
                    num_found_files += 1
                    js = json.load(f)
                    print(' Loaded!')
            except:
                print("No date in list")
                # writing file
               with open(new_json_path + new_json_file, 'a+') as outfile:
                   json.dump(self.jsonAnt, outfile, sort_keys=True, indent=4, )  # , indent=4, im.__dict__
                   outfile.write('\n')
                   outfile.close()
                   print(f'    Location:  {new_json_path}  \n Output file:  {new_json_file} \n')
                   print('New CocoJson Created!')


# RUN THE PROGRAM
def main():




if __name__ == '__main__':
    main()
