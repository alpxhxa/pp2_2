#ex 01
import json
data = {"score": 100}
with open("data.json", "w") as f:
    json.dump(data, f)

#ex 02
import json
with open("list.json", "w") as f:
    json.dump([1, 2, 3], f)

#ex 03
import json
config = {"theme": "dark"}
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

#ex 04
import json
log = {"event": "login"}
f = open("log.json", "w")
json.dump(log, f)
f.close()

#ex 05
import json
with open("pretty.json", "w") as f:
    json.dump({"x": 1}, f, separators=(',', ':'))