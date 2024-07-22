
# HL7 Converter
This converts HL7 files to either XML or JSON files. There is also a module for converting XML files to JSON. NOTE the CLI scripts have to be ran in the same directory as the "HL7 Parser" package is located.
# Where I Got the Information for the HL7 Standard
I was able to write this project using the functionality that just takes in the HL7 file, and compares it to the "config.json" file. the config.json file contains a list of "segments" in the order they appear in HL7 files. I was able to pull this information from [https://hl7-definition.caristix.com/v2/HL7v2.5.1](https://hl7-definition.caristix.com/v2/HL7v2.5.1)using the "Config_grabber" script (located in the Config_grabber directory).
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
Output JSON file (test.json):
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
    "security": [
      ""
    ],
    "message_type": [
      "SIU",
      "S12"
    ],
    "message_control_id": [
      "24916560"
    ],
    "processing_id": [
      "P"
    ],
    "version_id": [
      "2.3"
    ],
    "sequence_number": [
      ""
    ],
    "continuation_pointer": [
      ""
    ],
    "accept_acknowledgment_type": [
      ""
    ],
    "application_acknowledgment_type": [
      ""
    ],
    "country_code": [
      ""
    ],
    "character_set": [
      ""
    ]
  },
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
    "appointment_duration_units": [
      "m"
    ],
    "appointment_timing_quantity": [
      "",
      "",
      "60",
      "20110617084500",
      "20110617093000"
    ],
    "placer_contact_person": [
      ""
    ],
    "placer_contact_phone_number": [
      ""
    ],
    "placer_contact_address": [
      ""
    ],
    "placer_contact_location": [
      ""
    ],
    "filler_contact_person": [
      "9",
      "DENT",
      "ARTHUR",
      ""
    ],
    "filler_contact_phone_number": [
      ""
    ],
    "filler_contact_address": [
      ""
    ],
    "filler_contact_location": [
      ""
    ],
    "entered_by_person": [
      "9",
      "DENT",
      "COREY",
      ""
    ],
    "entered_by_phone_number": [
      ""
    ],
    "entered_by_location": [
      ""
    ],
    "parent_placer_appointment_id": [
      ""
    ],
    "parent_filler_appointment_id": [
      ""
    ],
    "filler_status_code": [
      "Scheduled"
    ]
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
    "patient_alias": [
      ""
    ],
    "race": [
      ""
    ],
    "patient_address": [
      "1 Broadway Ave",
      "",
      "Fort Wayne",
      "IN",
      "46804"
    ],
    "county_code": [
      ""
    ],
    "phone_number___home": [
      "(260)555-1234"
    ],
    "phone_number___business": [
      ""
    ],
    "primary_language": [
      ""
    ],
    "marital_status": [
      "S"
    ],
    "religion": [
      ""
    ],
    "patient_account_number": [
      "999999999"
    ],
    "ssn_number___patient": [
      ""
    ],
    "driver's_license_number___patient": [
      ""
    ],
    "mother's_identifier": [
      ""
    ],
    "ethnic_group": [
      ""
    ],
    "birth_place": [
      ""
    ],
    "multiple_birth_indicator": [
      ""
    ],
    "birth_order": [
      ""
    ],
    "citizenship": [
      ""
    ],
    "veterans_military_status": [
      ""
    ],
    "nationality": [
      ""
    ],
    "patient_death_date_and_time": [
      ""
    ],
    "patient_death_indicator": [
      ""
    ],
    "identity_unknown_indicator": [
      ""
    ],
    "identity_reliability_code": [
      ""
    ],
    "last_update_date_time": [
      ""
    ],
    "last_update_facility": [
      ""
    ],
    "species_code": [
      ""
    ],
    "breed_code": [
      ""
    ],
    "strain": [
      ""
    ],
    "production_class_code": [
      ""
    ],
    "tribal_citizenship": [
      ""
    ]
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
    "consulting_doctor": [
      ""
    ],
    "hospital_service": [
      ""
    ],
    "temporary_location": [
      ""
    ],
    "preadmit_test_indicator": [
      ""
    ],
    "re_admission_indicator": [
      ""
    ],
    "admit_source": [
      ""
    ],
    "ambulatory_status": [
      ""
    ],
    "vip_indicator": [
      ""
    ],
    "admitting_doctor": [
      ""
    ],
    "patient_type": [
      ""
    ],
    "visit_number": [
      ""
    ],
    "financial_class": [
      ""
    ],
    "charge_price_indicator": [
      ""
    ],
    "courtesy_code": [
      ""
    ],
    "credit_rating": [
      ""
    ],
    "contract_code": [
      ""
    ],
    "contract_effective_date": [
      ""
    ],
    "contract_amount": [
      ""
    ],
    "contract_period": [
      ""
    ],
    "interest_code": [
      ""
    ],
    "transfer_to_bad_debt_code": [
      ""
    ],
    "transfer_to_bad_debt_date": [
      ""
    ],
    "bad_debt_agency_code": [
      ""
    ],
    "bad_debt_transfer_amount": [
      ""
    ],
    "bad_debt_recovery_amount": [
      ""
    ],
    "delete_account_indicator": [
      ""
    ],
    "delete_account_date": [
      ""
    ],
    "discharge_disposition": [
      ""
    ],
    "discharged_to_location": [
      ""
    ],
    "diet_type": [
      ""
    ],
    "servicing_facility": [
      ""
    ],
    "bed_status": [
      ""
    ],
    "account_status": [
      ""
    ],
    "pending_location": [
      ""
    ],
    "prior_temporary_location": [
      ""
    ],
    "admit_date_time": [
      ""
    ],
    "discharge_date_time": [
      ""
    ],
    "current_patient_balance": [
      ""
    ],
    "total_charges": [
      ""
    ],
    "total_adjustments": [
      ""
    ],
    "total_payments": [
      ""
    ],
    "alternate_visit_id": [
      "99158"
    ],
    "visit_indicator": [
      ""
    ],
    "other_healthcare_provider": [
      ""
    ]
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
	<AIL>
	  <allow_substitution_code></allow_substitution_code>
	  <duration>45</duration>
	  <duration_units>m</duration_units>
	  <duration_units>Minutes</duration_units>
	  <filler_status_code>Scheduled</filler_status_code>
	  <location_group></location_group>
	  <location_resource_id>OFFICE</location_resource_id>
	  <location_resource_id></location_resource_id>
	  <location_resource_id></location_resource_id>
	  <location_resource_id>OFFICE</location_resource_id>
	  <location_type_ail></location_type_ail>
	  <location_type_ail>Main Office</location_type_ail>
	  <segment_action_code>A</segment_action_code>
	  <set_id___ail>1</set_id___ail>
	  <start_date_time>20110614084500</start_date_time>
	  <start_date_time_offset></start_date_time_offset>
	  <start_date_time_offset_units></start_date_time_offset_units>
	</AIL>
	<AIP>
	  <allow_substitution_code></allow_substitution_code>
	  <duration>45</duration>
	  <duration_units>m</duration_units>
	  <duration_units>Minutes</duration_units>
	  <filler_status_code>Scheduled</filler_status_code>
	  <personnel_resource_id>1</personnel_resource_id>
	  <personnel_resource_id>White</personnel_resource_id>
	  <personnel_resource_id>Charles</personnel_resource_id>
	  <personnel_resource_id>A</personnel_resource_id>
	  <personnel_resource_id>MD</personnel_resource_id>
	  <personnel_resource_id></personnel_resource_id>
	  <personnel_resource_id></personnel_resource_id>
	  <personnel_resource_id></personnel_resource_id>
	  <personnel_resource_id></personnel_resource_id>
	  <resource_group></resource_group>
	  <resource_type>D</resource_type>
	  <resource_type>White, Douglas</resource_type>
	  <segment_action_code>A</segment_action_code>
	  <set_id___aip>1</set_id___aip>
	  <start_date_time>20110614084500</start_date_time>
	  <start_date_time_offset></start_date_time_offset>
	  <start_date_time_offset_units></start_date_time_offset_units>
	</AIP>
	<MSH>
	  <accept_acknowledgment_type></accept_acknowledgment_type>
	  <application_acknowledgment_type></application_acknowledgment_type>
	  <character_set></character_set>
	  <continuation_pointer></continuation_pointer>
	  <country_code></country_code>
	  <date_time_of_message>20110613061611</date_time_of_message>
	  <encoding_characters>^~\&amp;</encoding_characters>
	  <field_separator>|</field_separator>
	  <message_control_id>24916560</message_control_id>
	  <message_type>SIU</message_type>
	  <message_type>S12</message_type>
	  <processing_id>P</processing_id>
	  <receiving_application>iFW</receiving_application>
	  <receiving_facility>ABC_HOSPITAL</receiving_facility>
	  <security></security>
	  <sending_application>MESA_OP</sending_application>
	  <sending_facility>XYZ_HOSPITAL</sending_facility>
	  <sequence_number></sequence_number>
	  <version_id>2.3</version_id>
	</MSH>
	<PID>
	  <administrative_sex>M</administrative_sex>
	  <alternate_patient_id___pid></alternate_patient_id___pid>
	  <birth_order></birth_order>
	  <birth_place></birth_place>
	  <breed_code></breed_code>
	  <citizenship></citizenship>
	  <county_code></county_code>
	  <date_time_of_birth>19781012</date_time_of_birth>
	  <driver_s_license_number___patient></driver_s_license_number___patient>
	  <ethnic_group></ethnic_group>
	  <identity_reliability_code></identity_reliability_code>
	  <identity_unknown_indicator></identity_unknown_indicator>
	  <last_update_date_time></last_update_date_time>
	  <last_update_facility></last_update_facility>
	  <marital_status>S</marital_status>
	  <mother_s_identifier></mother_s_identifier>
	  <mother_s_maiden_name></mother_s_maiden_name>
	  <multiple_birth_indicator></multiple_birth_indicator>
	  <nationality></nationality>
	  <patient_account_number>999999999</patient_account_number>
	  <patient_address>1 Broadway Ave</patient_address>
	  <patient_address></patient_address>
	  <patient_address>Fort Wayne</patient_address>
	  <patient_address>IN</patient_address>
	  <patient_address>46804</patient_address>
	  <patient_alias></patient_alias>
	  <patient_death_date_and_time></patient_death_date_and_time>
	  <patient_death_indicator></patient_death_indicator>
	  <patient_id></patient_id>
	  <patient_identifier_list>42</patient_identifier_list>
	  <patient_name>SMITH</patient_name>
	  <patient_name>PAUL</patient_name>
	  <phone_number___business></phone_number___business>
	  <phone_number___home>(260)555-1234</phone_number___home>
	  <primary_language></primary_language>
	  <production_class_code></production_class_code>
	  <race></race>
	  <religion></religion>
	  <set_id___pid>1</set_id___pid>
	  <species_code></species_code>
	  <ssn_number___patient></ssn_number___patient>
	  <strain></strain>
	  <tribal_citizenship></tribal_citizenship>
	  <veterans_military_status></veterans_military_status>
	</PID>
	<PV1>
	  <account_status></account_status>
	  <admission_type></admission_type>
	  <admit_date_time></admit_date_time>
	  <admit_source></admit_source>
	  <admitting_doctor></admitting_doctor>
	  <alternate_visit_id>99158</alternate_visit_id>
	  <ambulatory_status></ambulatory_status>
	  <assigned_patient_location></assigned_patient_location>
	  <attending_doctor>1</attending_doctor>
	  <attending_doctor>Smith</attending_doctor>
	  <attending_doctor>Miranda</attending_doctor>
	  <attending_doctor>A</attending_doctor>
	  <attending_doctor>MD</attending_doctor>
	  <attending_doctor></attending_doctor>
	  <attending_doctor></attending_doctor>
	  <attending_doctor></attending_doctor>
	  <attending_doctor></attending_doctor>
	  <bad_debt_agency_code></bad_debt_agency_code>
	  <bad_debt_recovery_amount></bad_debt_recovery_amount>
	  <bad_debt_transfer_amount></bad_debt_transfer_amount>
	  <bed_status></bed_status>
	  <charge_price_indicator></charge_price_indicator>
	  <consulting_doctor></consulting_doctor>
	  <contract_amount></contract_amount>
	  <contract_code></contract_code>
	  <contract_effective_date></contract_effective_date>
	  <contract_period></contract_period>
	  <courtesy_code></courtesy_code>
	  <credit_rating></credit_rating>
	  <current_patient_balance></current_patient_balance>
	  <delete_account_date></delete_account_date>
	  <delete_account_indicator></delete_account_indicator>
	  <diet_type></diet_type>
	  <discharge_date_time></discharge_date_time>
	  <discharge_disposition></discharge_disposition>
	  <discharged_to_location></discharged_to_location>
	  <financial_class></financial_class>
	  <hospital_service></hospital_service>
	  <interest_code></interest_code>
	  <other_healthcare_provider></other_healthcare_provider>
	  <patient_class>O</patient_class>
	  <patient_type></patient_type>
	  <pending_location></pending_location>
	  <preadmit_number></preadmit_number>
	  <preadmit_test_indicator></preadmit_test_indicator>
	  <prior_patient_location></prior_patient_location>
	  <prior_temporary_location></prior_temporary_location>
	  <re_admission_indicator></re_admission_indicator>
	  <referring_doctor>2</referring_doctor>
	  <referring_doctor>Withers</referring_doctor>
	  <referring_doctor>Peter</referring_doctor>
	  <referring_doctor>D</referring_doctor>
	  <referring_doctor>MD</referring_doctor>
	  <referring_doctor></referring_doctor>
	  <referring_doctor></referring_doctor>
	  <referring_doctor></referring_doctor>
	  <referring_doctor></referring_doctor>
	  <servicing_facility></servicing_facility>
	  <set_id___pv1>1</set_id___pv1>
	  <temporary_location></temporary_location>
	  <total_adjustments></total_adjustments>
	  <total_charges></total_charges>
	  <total_payments></total_payments>
	  <transfer_to_bad_debt_code></transfer_to_bad_debt_code>
	  <transfer_to_bad_debt_date></transfer_to_bad_debt_date>
	  <vip_indicator></vip_indicator>
	  <visit_indicator></visit_indicator>
	  <visit_number></visit_number>
	</PV1>
	<RGS>
	  <segment_action_code>A</segment_action_code>
	  <set_id___rgs>1</set_id___rgs>
	</RGS>
	<SCH>
	  <appointment_duration>60</appointment_duration>
	  <appointment_duration_units>m</appointment_duration_units>
	  <appointment_reason>reason for the appointment</appointment_reason>
	  <appointment_timing_quantity></appointment_timing_quantity>
	  <appointment_timing_quantity></appointment_timing_quantity>
	  <appointment_timing_quantity>60</appointment_timing_quantity>
	  <appointment_timing_quantity>20110617084500</appointment_timing_quantity>
	  <appointment_timing_quantity>20110617093000</appointment_timing_quantity>
	  <appointment_type>OFFICE</appointment_type>
	  <entered_by_location></entered_by_location>
	  <entered_by_person>9</entered_by_person>
	  <entered_by_person>DENT</entered_by_person>
	  <entered_by_person>COREY</entered_by_person>
	  <entered_by_person></entered_by_person>
	  <entered_by_phone_number></entered_by_phone_number>
	  <event_reason>OFFICE</event_reason>
	  <event_reason>Office visit</event_reason>
	  <filler_appointment_id>2196178</filler_appointment_id>
	  <filler_appointment_id>2196178</filler_appointment_id>
	  <filler_contact_address></filler_contact_address>
	  <filler_contact_location></filler_contact_location>
	  <filler_contact_person>9</filler_contact_person>
	  <filler_contact_person>DENT</filler_contact_person>
	  <filler_contact_person>ARTHUR</filler_contact_person>
	  <filler_contact_person></filler_contact_person>
	  <filler_contact_phone_number></filler_contact_phone_number>
	  <filler_status_code>Scheduled</filler_status_code>
	  <occurrence_number></occurrence_number>
	  <parent_filler_appointment_id></parent_filler_appointment_id>
	  <parent_placer_appointment_id></parent_placer_appointment_id>
	  <placer_appointment_id>10345</placer_appointment_id>
	  <placer_appointment_id>10345</placer_appointment_id>
	  <placer_contact_address></placer_contact_address>
	  <placer_contact_location></placer_contact_location>
	  <placer_contact_person></placer_contact_person>
	  <placer_contact_phone_number></placer_contact_phone_number>
	  <placer_group_number></placer_group_number>
	  <schedule_id>10345</schedule_id>
	</SCH>
</message>
```

JSON output file contents:
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
    "PID": {
      "administrative_sex": "M",
      "alternate_patient_id___pid": null,
      "birth_order": null,
      "birth_place": null,
      "breed_code": null,
      "citizenship": null,
      "county_code": null,
      "date_time_of_birth": "19781012",
      "driver_s_license_number___patient": null,
      "ethnic_group": null,
      "identity_reliability_code": null,
      "identity_unknown_indicator": null,
      "last_update_date_time": null,
      "last_update_facility": null,
      "marital_status": "S",
      "mother_s_identifier": null,
      "mother_s_maiden_name": null,
      "multiple_birth_indicator": null,
      "nationality": null,
      "patient_account_number": "999999999",
      "patient_address": [
        "1 Broadway Ave",
        null,
        "Fort Wayne",
        "IN",
        "46804"
      ],
      "patient_alias": null,
      "patient_death_date_and_time": null,
      "patient_death_indicator": null,
      "patient_id": null,
      "patient_identifier_list": "42",
      "patient_name": [
        "SMITH",
        "PAUL"
      ],
      "phone_number___business": null,
      "phone_number___home": "(260)555-1234",
      "primary_language": null,
      "production_class_code": null,
      "race": null,
      "religion": null,
      "set_id___pid": "1",
      "species_code": null,
      "ssn_number___patient": null,
      "strain": null,
      "tribal_citizenship": null,
      "veterans_military_status": null
    },
    "PV1": {
      "account_status": null,
      "admission_type": null,
      "admit_date_time": null,
      "admit_source": null,
      "admitting_doctor": null,
      "alternate_visit_id": "99158",
      "ambulatory_status": null,
      "assigned_patient_location": null,
      "attending_doctor": [
        "1",
        "Smith",
        "Miranda",
        "A",
        "MD",
        null,
        null,
        null,
        null
      ],
      "bad_debt_agency_code": null,
      "bad_debt_recovery_amount": null,
      "bad_debt_transfer_amount": null,
      "bed_status": null,
      "charge_price_indicator": null,
      "consulting_doctor": null,
      "contract_amount": null,
      "contract_code": null,
      "contract_effective_date": null,
      "contract_period": null,
      "courtesy_code": null,
      "credit_rating": null,
      "current_patient_balance": null,
      "delete_account_date": null,
      "delete_account_indicator": null,
      "diet_type": null,
      "discharge_date_time": null,
      "discharge_disposition": null,
      "discharged_to_location": null,
      "financial_class": null,
      "hospital_service": null,
      "interest_code": null,
      "other_healthcare_provider": null,
      "patient_class": "O",
      "patient_type": null,
      "pending_location": null,
      "preadmit_number": null,
      "preadmit_test_indicator": null,
      "prior_patient_location": null,
      "prior_temporary_location": null,
      "re_admission_indicator": null,
      "referring_doctor": [
        "2",
        "Withers",
        "Peter",
        "D",
        "MD",
        null,
        null,
        null,
        null
      ],
      "servicing_facility": null,
      "set_id___pv1": "1",
      "temporary_location": null,
      "total_adjustments": null,
      "total_charges": null,
      "total_payments": null,
      "transfer_to_bad_debt_code": null,
      "transfer_to_bad_debt_date": null,
      "vip_indicator": null,
      "visit_indicator": null,
      "visit_number": null
    },
    "RGS": {
      "segment_action_code": "A",
      "set_id___rgs": "1"
    },
    "SCH": {
      "appointment_duration": "60",
      "appointment_duration_units": "m",
      "appointment_reason": "reason for the appointment",
      "appointment_timing_quantity": [
        null,
        null,
        "60",
        "20110617084500",
        "20110617093000"
      ],
      "appointment_type": "OFFICE",
      "entered_by_location": null,
      "entered_by_person": [
        "9",
        "DENT",
        "COREY",
        null
      ],
      "entered_by_phone_number": null,
      "event_reason": [
        "OFFICE",
        "Office visit"
      ],
      "filler_appointment_id": [
        "2196178",
        "2196178"
      ],
      "filler_contact_address": null,
      "filler_contact_location": null,
      "filler_contact_person": [
        "9",
        "DENT",
        "ARTHUR",
        null
      ],
      "filler_contact_phone_number": null,
      "filler_status_code": "Scheduled",
      "occurrence_number": null,
      "parent_filler_appointment_id": null,
      "parent_placer_appointment_id": null,
      "placer_appointment_id": [
        "10345",
        "10345"
      ],
      "placer_contact_address": null,
      "placer_contact_location": null,
      "placer_contact_person": null,
      "placer_contact_phone_number": null,
      "placer_group_number": null,
      "schedule_id": "10345"
    }
  }
}
```
