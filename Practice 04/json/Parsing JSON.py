#ex 01
import json
data = '{"city": "Almaty", "temp": 25}'
print(json.loads(data)["city"])

#ex 02
import json
list_data = '[1, 2, 3]'
print(json.loads(list_data)[0])

#ex 03
import json
val = 'true'
print(json.loads(val) is True)

#ex 04
import json
complex_data = '{"items": [10, 20]}'
print(json.loads(complex_data)["items"][1])

#ex 05
import json
raw = 'null'
print(json.loads(raw))