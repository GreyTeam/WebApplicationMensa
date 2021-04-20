from server.database_utilities import *

"""
totale: int
users: [
    {
        nome: string
        cognome: string
        email: string
        keys: [
            string
        ]
    }
]

"""

def add_user(data):
    return {
        "email": data["email"],
        "nome": data["nome"],
        "cognome": data["cognome"],
        "keys": [data["key"]]
    }

def search_account(key):
    db = load_db(login_file_path)
    for user in db["users"]:
        for key in user["keys"]:
            return user
    return None

def get_account_information(key):
    db = load_db(login_file_path)
    for user in db["users"]:
        for key in user["keys"]:
            return True
    return None

def add_account(data):
    db = load_db(login_file_path)
    for i, user in enumerate(db["users"]):
        if user["email"] == data["email"]:
            if not data["key"] in user["keys"]:
                db["users"][i]["keys"].append(data["key"])
                save_db(db, login_file_path)
            return
    db["users"].append(add_user(data))
    db["totale"] += 1
    save_db(db, login_file_path)
