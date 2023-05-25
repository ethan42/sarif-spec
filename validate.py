import json
import requests
from jsonschema import validate, ValidationError

def load_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
        print("JSON file is valid!")
    except ValidationError as e:
        print("Validation Error!")
        print(e)
        raise

def main():
    json_data = load_json('Schemata/sarif-schema-2.1.0.json')
    json_schema = json.loads(requests.get(json_data['$schema']).text)
    validate_json(json_data, json_schema)

if __name__ == "__main__":
    main()
