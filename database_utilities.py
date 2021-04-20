import os.path
import json

prenotazioni_file_path = 'prenotazioni.json'

def __load_db():
    if os.path.isfile(prenotazioni_file_path):
        db = json.load(open(prenotazioni_file_path, "r"))
    
    else: 
        db = ""

    if db == "":
        db = {
            "totale": 0,
            "prenotazioni": []
        }
    return db

def __save_db(db):
    json.dump(db, open(prenotazioni_file_path, "w"), indent=4)

def append_user(data):
    db = __load_db()
    db["prenotazioni"].append(data)
    db["totale"] += 1
    __save_db(db)