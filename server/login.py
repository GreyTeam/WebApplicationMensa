from database_utilities import *

"""
totale: int
users: [
    {
        email: string
        keys: [
            string
        ]
    }
]

"""

def create_user(data):
    return {
        "email": data["email"],
        "keys": []
    }

def add_user(data):
    return {
        "email": data["email"],
        "keys": [data["key"]]
    }

def search_account(data):
    db = load_db(login_file_path)
    for user in db["users"]:
        if user["email"] == data["email"]:
            return data["key"] in user["keys"]
    return False

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

add_account({
    "email": "devid@gmail.com",
    "key": "key4"
})

add_account({
    "email": "lorenzo@gmail.com",
    "key": "key5"
})

print(search_account({
    "email": "lorenzo@gmail.com",
    "key": "key5"
}))