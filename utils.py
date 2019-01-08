import csv
import os
import re

from lxml import etree

import config


def match_regex(pattern, string, position=0, tuple_pos=0):
    m = re.findall(pattern, string)
    if m:
        if position <= len(m) + 1:
            if isinstance(m[position], tuple):
                if tuple_pos <= len(m[position]) + 1:
                    return m[position][tuple_pos].strip()
            else:
                return m[position].strip()
    return ''


def write_csv(filename, content, keys=[]):
    create_directory_if_not_exists(filename)
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, keys, delimiter=';')
        writer.writeheader()
        writer.writerows(content)


def create_directory_if_not_exists(filename):
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_xml(values):
    for value in values:
        xml_path = re.sub(r'^/', '',
                          re.sub(r'docx|doc|pdf$', 'xml', value['path']))
        xml_path = os.path.join(config.XML_FOLDER_PATH, xml_path)

        root = etree.Element('root')
        for key, val in value.items():
            node = etree.SubElement(root, key)
            node.text = val

        write_file(xml_path,
                   etree.tostring(root, pretty_print=True, encoding='unicode'))


def write_file(filename, content):
    create_directory_if_not_exists(filename)
    with open(filename, 'w') as file:
        file.write(content)
