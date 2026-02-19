#ex 01
import json
with open("sample-data.json", "r") as f:
    data = json.load(f)
    for item in data["imdata"]:
        print(item["l1PhysIf"]["attributes"]["dn"])

#ex 02
import json
with open("sample-data.json", "r") as f:
    data = json.load(f)
    print(len(data["imdata"]))

#ex 03
import json
with open("sample-data.json", "r") as f:
    data = json.load(f)
    first = data["imdata"][0]
    print(first.keys())

#ex 04
import json
with open("sample-data.json", "r") as f:
    data = json.load(f)
    attrs = data["imdata"][0]["l1PhysIf"]["attributes"]
    print(attrs.get("speed", "inherit"))

#ex 05
import json
with open("sample-data.json", "r") as f:
    data = json.load(f)
    items = [x for x in data["imdata"] if "attributes" in x["l1PhysIf"]]
    print(len(items))