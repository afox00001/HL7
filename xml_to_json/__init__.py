import json
import xmltodict


def xml_to_json(xml_str: str):
    data_dict = xmltodict.parse(xml_str)
    return json.dumps(data_dict)


def xml_file_to_json_file(xml_file_path: str, json_output_file_path: str) -> None:
    with open(xml_file_path) as xml_file:
        json_data = xml_to_json(xml_file.read())
        with open(json_output_file_path, "w") as json_file:
            json_file.write(json_data)
