# -*- coding: utf-8 -*-

import os
import yaml
import sys

if __name__ == '__main__':
    argv = sys.argv

    mime = argv[1]
    exs = argv[2:]

    self_path = os.path.abspath(os.path.dirname(__file__))
    yaml_file_path = '%s/../mime_types.yaml' % self_path

    f = open(yaml_file_path, 'r')
    data = yaml.load(f)
    f.close()

    if mime in data:
        sys.stderr.write('[ERROR] `%s` has been registered\n' % mime)
        exit(1)

    data[mime] = []
    for ex in exs:
        data[mime].append(ex)

    f = open(yaml_file_path, 'w')
    f.write(yaml.dump(data, default_flow_style=False))
    f.close()

