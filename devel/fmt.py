# -*- coding: utf-8 -*-

import os
import yaml

if __name__ == '__main__':
    self_path = os.path.abspath(os.path.dirname(__file__))
    yaml_file_path = '%s/../mime_types.yaml' % self_path

    f = open(yaml_file_path, 'r')
    data = yaml.load(f)
    f.close()

    f = open(yaml_file_path, 'w')
    f.write(yaml.dump(data, default_flow_style=False))
    f.close()

