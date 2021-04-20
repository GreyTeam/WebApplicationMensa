from server.database_utilities import *

"""
totale: int
prenotazioni: [
    {
        "nome": string
        "cognome": string
        "data": string
    }
]
"""

def get_day_list():
    p_list = []
    db = load_db(prenotazioni_file_path)
    today = datetime.datetime.now().strftime("%d/%m")
    for p in db["prenotazioni"]:
        if today == p["date"]:
            p_list.append(p)
    return p_list

def check_reservation(email, data):
    db = load_db(prenotazioni_file_path)
    for p in db["prenotazioni"]:
        if p["email"] == email and p["date"] == data:
            return True
    return False