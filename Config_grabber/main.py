import json
import requests
print()
data = {}
jfile = json.load(open("segs.json", "r", errors="ignore"))
for seg in jfile:
    print(seg["id"])
    req_data = requests.get("https://hl7-definition.caristix.com/v2-api/1/HL7v2.5/Segments/" + seg["id"]).json()
    print(req_data)
    data[seg["id"]] = []
    for item in req_data["fields"]:
        data[seg["id"]].append(item["name"].lower().replace(" ", "_").replace("/", "_").replace("-", "_"))
json.dump(data, open("config.json", "w"))
print(data)
