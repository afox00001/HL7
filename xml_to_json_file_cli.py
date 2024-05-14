import xml_to_json
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Takes an XML file and converts it to a new JSON file')
    parser.add_argument('xml', type=str, help='the path to the XML file', nargs='?', default=os.getcwd())
    parser.add_argument('out', type=str, help='the path to the output JSON file', nargs='?', default=os.getcwd())
    parser.parse_args()

    args = parser.parse_args()
    xml_to_json.xml_file_to_json_file(os.path.realpath(args.xml), os.path.realpath(args.out))
