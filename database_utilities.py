import os.path
import json

def __load_db():
    if os.path.isfile('prenotazioni.json'):
        db = json.load("prenotazioni.json")
    
    else: 
        db = ""

    if db == "":
        db = {
            "totale": 0,
            "prenotazioni": []
        }
    return db

def __save_db(db):
    json.dump(db, open("prenotazioni.json", "w"), indent=4)

def append_user(data):
    db = __load_db()
    db["prenotazioni"].append(data)
    db["totale"] += 1
    __save_db(db)