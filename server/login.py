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

def search_account_exist(data):
    db = load_db(login_file_path)
    for user in db["users"]:
        if user["email"] == data["email"]:
            return data["key"] in user["keys"]
    return False

def get_account_information():
    pass

def add_account(data):
    db = load_db(login_file_path)
    for i, user in enumerate(db["users"]):
        print(f"Data: {data}")
        print(f"User: {user}")
        if user["email"] == data["email"]:
            if not data["key"] in user["keys"]:
                db["users"][i]["keys"].append(data["key"])
                save_db(db, login_file_path)
            return
    db["users"].append(add_user(data))
    db["totale"] += 1
    save_db(db, login_file_path)
