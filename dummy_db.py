import json


def load_all_items_from_file():
    db_json_file = open("json_db.json")
    return json.load(db_json_file)


db = load_all_items_from_file()
