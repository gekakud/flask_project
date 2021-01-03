import json


def load_all_items():
    db_json_file = open("json_db.json")
    return json.load(db_json_file)


db = load_all_items()
