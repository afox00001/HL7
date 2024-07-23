import json
import os

from dict2xml import dict2xml


def parse(message: str, line_separator='\n'):
    field_separator_index = 3
    subcomponent_separator_index = 4
    segment_name_index = 0
    meta_data_header_name = "MSH"

    parsed_message = ParsedMessage(message)
    field_separator = message[field_separator_index]
    subcomponent_separator = message[subcomponent_separator_index]

    for line in message.split(line_separator):
        repeated_segment = False

        fields = line.split(field_separator)
        segment_name = fields[segment_name_index]

        if parsed_message.segment_exists(segment_name):
            segment = parsed_message.get_segment(segment_name)
            repeated_segment = True

        else:
            segment = HL7Segment()
            segment.name = segment_name

        subcomponents = [[segment_name]]
        field_start = 1
        if segment_name == meta_data_header_name:
            subcomponents.append([field_separator])
            subcomponents.append([fields[1]])
            field_start = 2
        for field in fields[field_start:]:
            subcomponents.append(field.split(subcomponent_separator))
        segment.values.append(subcomponents)
        if not repeated_segment:
            parsed_message.segments.append(segment)

    return parsed_message


class ParsedMessage:
    def __init__(self, message: str) -> None:
        self.segments = []
        self.raw_message = message
        self.raw_message_length = len(message)

    def get_segment(self, segment_name: str):
        return [seg for seg in self.segments if seg.name == segment_name][0]

    def segment_exists(self, segment_name: str) -> bool:
        return segment_name in [seg.name for seg in self.segments]

    def segment_count(self, segment_name=None) -> int:
        if segment_name is None:
            return sum(len(segment.values) for segment in self.segments)
        return len(self.get_segment(segment_name).values)

    def get_value(self, segment_name, repetition, field,
                  sub=1):
        repetition -= 1
        sub -= 1

        segment = self.get_segment(segment_name)
        if (len(segment.values) > repetition and
                len(segment.values[repetition]) > field and
                len(segment.values[repetition][field]) > sub):
            return segment.values[repetition][field][sub]
        return None


class HL7Segment:

    def __init__(self):
        self.values = []
        self.name = ''


def hl7_to_dict(hl7_text: str) -> dict:
    parsed_message = parse(hl7_text, '\n')
    data = {}
    segment_truth_tables = json.load(
        open(os.path.dirname(os.path.realpath(__file__)) + "\\config\\segment_truth_table.json", "r"))
    for segment in parsed_message.segments:
        """The 'segment name' is in the first sub-segment, hence [0][0][0]"""
        segment_name = str(segment.values[0][0][0]).upper()
        data[segment_name] = {}
        for sub_segment_id, sub_segment in enumerate(segment.values[0][1:]):
            if segment_name in segment_truth_tables:
                data[segment_name][segment_truth_tables[segment_name][sub_segment_id]] = sub_segment
            elif segment_name is None or segment_name == "":
                pass
            else:
                raise KeyError(f"The '{segment_name}' segment is not in config/segment_truth_table.json")
    return data


def hl7_to_xml(hl7_text: str) -> str:
    """dict2xml will not have a main root tag, so I have to add the root tag in manually here"""
    parsed_message = dict2xml(hl7_to_dict(hl7_text))
    updated_parsed_message = ""
    for line in parsed_message.splitlines():
        updated_parsed_message += "\n\t" + line
    return f"<message>{updated_parsed_message}\n</message>"


def hl7_to_xml_file(hl7_text: str, output_fp: str) -> None:
    data = hl7_to_xml(hl7_text)
    with open(output_fp, 'w') as output_file:
        output_file.write(data)


def hl7_to_json_file(hl7_text: str, output_fp: str) -> None:
    data = hl7_to_dict(hl7_text)
    json.dump(data, open(output_fp, 'w'))


def hl7_file_to_json_file(hl7_fp: str, output_fp: str) -> None:
    with open(hl7_fp, 'r') as hl7_file:
        hl7_to_json_file(hl7_file.read(), output_fp)


def hl7_file_to_xml_file(hl7_fp: str, output_fp: str) -> None:
    with open(hl7_fp, 'r') as hl7_file:
        hl7_to_xml_file(hl7_file.read(), output_fp)
