with open(json_path) as f2:
    js2 = json.load(f2)

    source_infos2 = js2['info']
    source_images2 = js2['images']
    source_categories2 = js2['categories']
    source_annotations2 = js2['annotations']

    print('\nFILE < ' + str(num_found_files) + ' > details: ')
    print('info: ' + str(len(source_infos2)))
    print('images: ' + str(len(source_images2)))
    print('annotations: ' + str(len(source_annotations2)))
    print('categories: ' + str(len(source_categories2)))

    file_desc2 = source_infos2['description']
    print(f'second file code is : {file_desc2[1:33]}')
    print(f'second file last : {file_desc2[33:47]}')
    if file_desc2[33:47] == 'PGON JSON file':
        print(f'file type is :{file_desc2[33:47]}')
    else:
        print(f'did not match < PGON JSON file >')