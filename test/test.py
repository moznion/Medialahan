# -*- coding: utf-8 -*-

import unittest
import os
import re

class MedialahanTest(unittest.TestCase):
    def test_should_not_be_duplicated_content_type(self):
        self_path = os.path.abspath(os.path.dirname(__file__))
        yaml_file_path = '%s/../mime_types.yaml' % self_path

        f = open(yaml_file_path, 'r')

        bag = {}
        duplicated = {}
        for line in f:
            line = line.rstrip()
            if re.match('^[^-]', line):
                if line in bag:
                    duplicated[line] = True
                else:
                    bag[line] = True

        if len(duplicated) > 0:
            err_msg = '\n'.join(duplicated.keys())
            self.fail('Duplicated content types >>>\n%s' % err_msg)

        f.close()

        self.assertEqual('name', 'name')

if __name__ == '__main__':
    unittest.main()

