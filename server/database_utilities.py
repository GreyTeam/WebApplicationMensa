import os.path
import json
import datetime

prenotazioni_file_path = 'data/prenotazioni.json'
login_file_path = 'data/users.json'
log_file_path = 'data/log.json'
dates_file_path = 'data/dates.json'

def load_db(db_filename):
    return json.load(open(db_filename, "r")) if os.path.isfile(db_filename) else {}

def save_db(db, db_filename):
    json.dump(db, open(db_filename, "w"), indent=4)

def append_user(data):
    db = load_db(prenotazioni_file_path)
    db["prenotazioni"].append(data)
    db["totale"] += 1
    save_db(db, prenotazioni_file_path)


