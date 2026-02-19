#ex 01
import json
user = {"id": 1, "admin": False}
print(json.dumps(user))

#ex 02
import json
colors = ["red", "blue"]
print(json.dumps(colors))

#ex 03
import json
data = {"status": None}
print(json.dumps(data))

#ex 04
import json
d = {"key": "val"}
print(json.dumps(d, indent=4))

#ex 05
import json
d = {"b": 1, "a": 2}
print(json.dumps(d, sort_keys=True))