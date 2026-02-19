#ex 01
import json
with open("data.json", "r") as f:
    print(json.load(f))

#ex 02
import json
with open("config.json", "r") as f:
    d = json.load(f)
    print(d.get("theme"))

#ex 03
import json
f = open("list.json", "r")
content = json.load(f)
print(len(content))
f.close()

#ex 04
import json
with open("data.json", "r") as f:
    res = json.load(f)
    print(type(res))

#ex 05
import json
try:
    with open("empty.json", "r") as f:
        json.load(f)
except:
    print("Error reading")