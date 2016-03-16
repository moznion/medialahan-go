# -*- coding: utf-8 -*-

import os
import yaml

if __name__ == '__main__':
    self_path = os.path.abspath(os.path.dirname(__file__))
    yaml_file_path = '%s/../medialahan/mime_types.yaml' % self_path

    f = open(yaml_file_path, 'r')
    data = yaml.load(f)
    f.close()

    print('package medialahan\n')

    print('var ContentTypeToExt map[string]string = map[string]string{')
    for content_type, exts in data.items():
        print('\t"%s": "%s",' % (content_type, exts[0]))
    print('}\n')

    print('var ExtToContentType map[string]string = map[string]string{')
    bag = {}
    for content_type, exts in data.items():
        for ext in exts:
            if bag.get(ext) == None:
                print('\t"%s": "%s",' % (ext, content_type))
                bag[ext] = True
    print('}')
