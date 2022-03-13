"""
https://github.com/Julian/jsonschema
https://python-jsonschema.readthedocs.io/en/stable/   
version 3.2
"""

import json
from jsonschema import validate

with open("model_example.json", "r") as f:
    schema = json.load(f)

with open("payload_example.json", "r") as f:
    payload = json.load(f)


print("json-schema")
print(json.dumps(schema, indent=4))

print("="*40, end="\n\n")

print("payload")
print(json.dumps(payload, indent=4))

print("="*40, end="\n\n")

try:
    validate(instance=payload, schema=schema)
    print("payload 1 : valide")
except:
    print("payload 1 : not valide")

try:
    validate(instance= {"dragonName" : 123}, schema=schema)
    print("payload 2 : valide")
except:
    print("payload 2 : not valide")