import HL7Parse
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Takes a HL7 file and converts it to a new json file')
    parser.add_argument('hl7', type=str, help='the path to the HL7 file', nargs='?', default=os.getcwd())
    parser.add_argument('out', type=str, help='the path to the output json file', nargs='?', default=os.getcwd())
    parser.parse_args()

    args = parser.parse_args()
    HL7Parse.hl7_file_to_json_file(os.path.realpath(args.hl7), os.path.realpath(args.out))
