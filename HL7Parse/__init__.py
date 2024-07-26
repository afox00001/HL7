import json
import os

from dict2xml import dict2xml


def append_array_to_array(old_array, new_array, index=0):
    if index == len(new_array):
        return old_array
    old_array.append(new_array[index])
    return append_array_to_array(old_array, new_array, index + 1)


def parse(message: str, line_separator='\n'):
    field_separator_index = 3
    segment_name_index = 0
    meta_data_header_name = "MSH"

    parsed_message = ParsedMessage(message)
    field_separator = message[field_separator_index]

    def process_message(message, line_index=0):
        if line_index == len(message.split(line_separator)):
            return None
        line = message.split(line_separator)[line_index]
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
        append_array_to_array(subcomponents, fields[field_start:])
        segment.values.append(subcomponents)
        if not repeated_segment:
            parsed_message.segments.append(segment)

    process_message(message)

    return parsed_message


class ParsedMessage:
    def __init__(self, message: str) -> None:
        self.segments = []
        self.raw_message = message
        self.raw_message_length = len(message)

    def get_segment(self, segment_name: str, segments_found=[], index=0):
        if index == len(self.segments):
            return None
        if segment_name == self.segments[index].name:
            segments_found.append(self.segments[index])
        return self.get_segment(segment_name, segments_found, index + 1)

    def segment_exists(self, segment_name: str, index=0) -> bool:
        if index == len(self.segments):
            return False
        if segment_name == self.segments[index].name:
            return True

    def segment_count(self, segment_name=None, segment_count=0, segment_index=0) -> int:
        if segment_index == len(self.segments):
            return segment_count
        if segment_name is not None:
            return len(self.get_segment(segment_name).values)
        segment_count += len(self.segments[segment_index].values)
        return self.segment_count(segment_name, segment_count, segment_index + 1)

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
    segment_truth_tables = json.load(
        open(os.path.dirname(os.path.realpath(__file__)) + "\\config\\segment_truth_table.json", "r"))

    def get_sub_segments(segment, segment_name, current_sub_segments={}, sub_segment_id=0) -> dict:
        if sub_segment_id == len(segment.values[0]) - 1:
            return current_sub_segments
        if segment_name not in segment_truth_tables:
            raise KeyError(f"The '{segment_name}' segment is not in config/segment_truth_table.json")
        current_sub_segments[segment_truth_tables[segment_name][sub_segment_id]] = segment.values[0][
            sub_segment_id + 1]  # its [sub_segment_id + 1) because the 0th id is just the name of the segment itself
        return get_sub_segments(segment, segment_name, current_sub_segments, sub_segment_id + 1)

    def parse_segments(segments, segment_index=0, current_data={}):
        if segment_index == len(segments):
            return current_data
        segment = segments[segment_index]
        segment_name = str(segment.values[0][0][0]).upper()
        current_data[segment_name] = get_sub_segments(segment, segment_name)
        return parse_segments(segments, segment_index + 1, current_data)

    parsed_message = parse(hl7_text, '\n')
    return parse_segments(parsed_message.segments)


def hl7_to_xml(hl7_text: str) -> str:
    """dict2xml will not have a main root tag, so I have to add the root tag in manually here"""

    def add_root_tag_to_xml(xml, updated_xml="", line_index=0):
        if line_index == len(xml.splitlines()):
            updated_xml += "\n</message>"
            return updated_xml
        line = xml.splitlines()[line_index]
        if line_index == 0:
            updated_xml += "<message>"

        updated_xml += f"\n\t{line}"
        return add_root_tag_to_xml(xml, updated_xml, line_index + 1)

    return add_root_tag_to_xml(dict2xml(hl7_to_dict(hl7_text)))


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
