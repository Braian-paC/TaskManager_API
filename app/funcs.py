import json

file_json = "database.json"

def read_data():
    try:
        with open(file_json, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(file_json, "w") as file:
        json.dump(data, file, indent=4)
