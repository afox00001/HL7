
# HL7 Converter
This converts HL7 files to either XML or JSON files. There is also a module for converting XML files to JSON. NOTE the CLI scripts have to be ran in the same directory as the "HL7 Parser" package is located.
# Where I Got the Information for the HL7 Standard
I was able to write this project using the functionality that just takes in the HL7 file, and compares it to the "config.json" file. the config.json file contains a list of "segments" in the order they appear in HL7 files. I was able to pull this information from [https://hl7-definition.caristix.com/v2/HL7v2.5.1](https://hl7-definition.caristix.com/v2/HL7v2.5.1) using the "Config_grabber" script (located in the Config_grabber directory).

I go over how this project works in detail in my [Medium artical] (https://ashtonsfox.medium.com/how-to-convert-hl7-files-to-json-and-xml-using-python-fdaa2c15370b)
# HL7Parse Library
The HL7Parse Library consists of 6 main functions:

**`hl7_to_dict`**, **`hl7_to_xml`**, **`hl7_to_xml_file`**, **`hl7_to_json_file`**, **`hl7_file_to_json_file`**, and **`hl7_file_to_xml_file`**.

**`hl7_to_dict`** takes in the HL7 message as a string, and returns the dictionary (in this case, it's basically JSON)

**`hl7_to_xml`** takes in the HL7 message as a string, and returns the XML as a string

**`hl7_to_xml_file`** takes in the HL7 message as a string, and the file path to the output XML file (as a string). This function takes the raw HL7, and outputs the XML equivalent in the specified XML output file.

**`hl7_to_json_file`** takes in the HL7 message as a string, and the file path to the output JSON file (as a string). This function takes the raw HL7, and outputs the JSON equivalent in the specified JSON output file.

**`hl7_file_to_json_file`** takes in a file path to an HL7 file, and an output path to the output JSON file.

**`hl7_file_to_xml`** takes in a file path to an HL7 file, and an output path to the output XML file.

# xml_to_json Library
the xml_to_json library has 2 main functions: **`xml_to_json`**, and **`xml_file_to_json_file`**.

**`xml_to_json`** takes in the raw XML data as a string, and outputs the raw JSON as a json dump

**`xml_file_to_json_file`** takes in the file path to an XML file, and a file path to the output JSON file
## Usage/Examples
To convert HL7 to an XML file, use this CMD command:
```cmd
python HL7_to_xml_file_cli.py [hl7_file.hl7] [output_XML_file.XML]
```

To convert a HL7 file to JSON, use this CMD command:

```cmd
python HL7_to_json_file_cli.py [hl7_file.hl7] [output_JSON_file.json]
```
Command Line:
```cmd
python HL7_to_json_file_cli.py test.hl7 test.json
```

input HL7 file (test.hl7):
```hl7
MSH|^~\&|MESA_OP|XYZ_HOSPITAL|iFW|ABC_HOSPITAL|20110613061611||SIU^S12|24916560|P|2.3||||||
SCH|10345^10345|2196178^2196178|||10345|OFFICE^Office visit|reason for the appointment|OFFICE|60|m|^^60^20110617084500^20110617093000|||||9^DENT^ARTHUR^||||9^DENT^COREY^|||||Scheduled
PID|1||42||SMITH^PAUL||19781012|M|||1 Broadway Ave^^Fort Wayne^IN^46804||(260)555-1234|||S||999999999|||||||||||||||||||||
PV1|1|O|||||1^Smith^Miranda^A^MD^^^^|2^Withers^Peter^D^MD^^^^||||||||||||||||||||||||||||||||||||||||||99158||
RGS|1|A
AIG|1|A|1^White, Charles|D^^
AIL|1|A|OFFICE^^^OFFICE|^Main Office||20110614084500|||45|m^Minutes||Scheduled
AIP|1|A|1^White^Charles^A^MD^^^^|D^White, Douglas||20110614084500|||45|m^Minutes||Scheduled
```
Example output JSON file (test.json):
```json
{
  "MSH": {
    "field_separator": [
      "|"
    ],
    "encoding_characters": [
      "^~\\&"
    ],
    "sending_application": [
      "MESA_OP"
    ],
    "sending_facility": [
      "XYZ_HOSPITAL"
    ],
    "receiving_application": [
      "iFW"
    ],
    "receiving_facility": [
      "ABC_HOSPITAL"
    ],
    "date_time_of_message": [
      "20110613061611"
    ],
    ...
  }
  "SCH": {
    "placer_appointment_id": [
      "10345",
      "10345"
    ],
    "filler_appointment_id": [
      "2196178",
      "2196178"
    ],
    "occurrence_number": [
      ""
    ],
    "placer_group_number": [
      ""
    ],
    "schedule_id": [
      "10345"
    ],
    "event_reason": [
      "OFFICE",
      "Office visit"
    ],
    "appointment_reason": [
      "reason for the appointment"
    ],
    "appointment_type": [
      "OFFICE"
    ],
    "appointment_duration": [
      "60"
    ],
  ...
  },
  "PID": {
    "set_id___pid": [
      "1"
    ],
    "patient_id": [
      ""
    ],
    "patient_identifier_list": [
      "42"
    ],
    "alternate_patient_id___pid": [
      ""
    ],
    "patient_name": [
      "SMITH",
      "PAUL"
    ],
    "mother's_maiden_name": [
      ""
    ],
    "date_time_of_birth": [
      "19781012"
    ],
    "administrative_sex": [
      "M"
    ],
  ...
  },
  "PV1": {
    "set_id___pv1": [
      "1"
    ],
    "patient_class": [
      "O"
    ],
    "assigned_patient_location": [
      ""
    ],
    "admission_type": [
      ""
    ],
    "preadmit_number": [
      ""
    ],
    "prior_patient_location": [
      ""
    ],
    "attending_doctor": [
      "1",
      "Smith",
      "Miranda",
      "A",
      "MD",
      "",
      "",
      "",
      ""
    ],
    "referring_doctor": [
      "2",
      "Withers",
      "Peter",
      "D",
      "MD",
      "",
      "",
      "",
      ""
    ],
   ...
  },
  "RGS": {
    "set_id___rgs": [
      "1"
    ],
    "segment_action_code": [
      "A"
    ]
  },
  "AIG": {
    "set_id___aig": [
      "1"
    ],
    "segment_action_code": [
      "A"
    ],
    "resource_id": [
      "1",
      "White, Charles"
    ],
    "resource_type": [
      "D",
      "",
      ""
    ]
  },
  "AIL": {
    "set_id___ail": [
      "1"
    ],
    "segment_action_code": [
      "A"
    ],
    "location_resource_id": [
      "OFFICE",
      "",
      "",
      "OFFICE"
    ],
    "location_type_ail": [
      "",
      "Main Office"
    ],
    "location_group": [
      ""
    ],
    "start_date_time": [
      "20110614084500"
    ],
    "start_date_time_offset": [
      ""
    ],
    "start_date_time_offset_units": [
      ""
    ],
    "duration": [
      "45"
    ],
    "duration_units": [
      "m",
      "Minutes"
    ],
    "allow_substitution_code": [
      ""
    ],
    "filler_status_code": [
      "Scheduled"
    ]
  },
  "AIP": {
    "set_id___aip": [
      "1"
    ],
    "segment_action_code": [
      "A"
    ],
    "personnel_resource_id": [
      "1",
      "White",
      "Charles",
      "A",
      "MD",
      "",
      "",
      "",
      ""
    ],
    "resource_type": [
      "D",
      "White, Douglas"
    ],
    "resource_group": [
      ""
    ],
    "start_date_time": [
      "20110614084500"
    ],
    "start_date_time_offset": [
      ""
    ],
    "start_date_time_offset_units": [
      ""
    ],
    "duration": [
      "45"
    ],
    "duration_units": [
      "m",
      "Minutes"
    ],
    "allow_substitution_code": [
      ""
    ],
    "filler_status_code": [
      "Scheduled"
    ]
  }
}
```

## XML to JSON Usage/Examples:

Command Line:
```
python xml_to_json_file_cli.py test.xml test.json
```
XML input (test.xml):
```xml
<message>
	<AIG>
	  <resource_id>1</resource_id>
	  <resource_id>White, Charles</resource_id>
	  <resource_type>D</resource_type>
	  <resource_type></resource_type>
	  <resource_type></resource_type>
	  <segment_action_code>A</segment_action_code>
	  <set_id___aig>1</set_id___aig>
	</AIG>
   ...
</message>
```

Example JSON output file contents:
```json
{
  "message": {
    "AIG": {
      "resource_id": [
        "1",
        "White, Charles"
      ],
      "resource_type": [
        "D",
        null,
        null
      ],
      "segment_action_code": "A",
      "set_id___aig": "1"
    },
    "AIL": {
      "allow_substitution_code": null,
      "duration": "45",
      "duration_units": [
        "m",
        "Minutes"
      ],
      "filler_status_code": "Scheduled",
      "location_group": null,
      "location_resource_id": [
        "OFFICE",
        null,
        null,
        "OFFICE"
      ],
      "location_type_ail": [
        null,
        "Main Office"
      ],
      "segment_action_code": "A",
      "set_id___ail": "1",
      "start_date_time": "20110614084500",
      "start_date_time_offset": null,
      "start_date_time_offset_units": null
    },
    "AIP": {
      "allow_substitution_code": null,
      "duration": "45",
      "duration_units": [
        "m",
        "Minutes"
      ],
      "filler_status_code": "Scheduled",
      "personnel_resource_id": [
        "1",
        "White",
        "Charles",
        "A",
        "MD",
        null,
        null,
        null,
        null
      ],
      "resource_group": null,
      "resource_type": [
        "D",
        "White, Douglas"
      ],
      "segment_action_code": "A",
      "set_id___aip": "1",
      "start_date_time": "20110614084500",
      "start_date_time_offset": null,
      "start_date_time_offset_units": null
    },
    "MSH": {
      "accept_acknowledgment_type": null,
      "application_acknowledgment_type": null,
      "character_set": null,
      "continuation_pointer": null,
      "country_code": null,
      "date_time_of_message": "20110613061611",
      "encoding_characters": "^~\\&",
      "field_separator": "|",
      "message_control_id": "24916560",
      "message_type": [
        "SIU",
        "S12"
      ],
      "processing_id": "P",
      "receiving_application": "iFW",
      "receiving_facility": "ABC_HOSPITAL",
      "security": null,
      "sending_application": "MESA_OP",
      "sending_facility": "XYZ_HOSPITAL",
      "sequence_number": null,
      "version_id": "2.3"
    },
...
}
```
