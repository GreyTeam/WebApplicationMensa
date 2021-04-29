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

def search_user(key):
    db = load_db(login_file_path)
    for user in db["users"]:
        for user_key in user["keys"]:
            if user_key == key:
                return user
    return None

def user_exist(key):
    db = load_db(login_file_path)
    for user in db["users"]:
        for user_key in user["keys"]:
            if user_key == key:
                return True
    return False

def add_user(data):
    db = load_db(login_file_path)
    for i, user in enumerate(db["users"]):
        if user["email"] == data["email"]:
            if not data["key"] in user["keys"]:
                db["users"][i]["keys"].append(data["key"])
                save_db(db, login_file_path)
            return

    data["keys"] = [data["key"]]
    data.pop("key")

    db["users"].append(data)
    db["totale"] += 1
    save_db(db, login_file_path)

def add_info(key, classe):
    db = load_db(login_file_path)
    for user in db["users"]:
        for user_key in user["keys"]:
            if user_key == key:
                user["classe"] = classe
                save_db(db, login_file_path)
                return True
            
    return None