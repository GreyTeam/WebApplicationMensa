import jwt 
from server import database
import string
import random

def __create_key():
    # choose from all lowercase letter
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(64))

SECRET_KEY: str = __create_key()
print(SECRET_KEY)

def generate_oauth_token(payload: {}):
    return jwt.encode(
        payload=payload,
        key=SECRET_KEY
    )

def verify_oauth_token(token: string, verify_only: bool = False):
    try:
        content = jwt.decode(token, key=SECRET_KEY, algorithms=["HS256"])
        return True if verify_only else content
    except jwt.exceptions.InvalidSignatureError:
        return False

##############################
# TODO Implementare con il codice fornito dall'autenticazione con google
##############################

def get_user(email):
    db = database.get_db()
    return db["users"].find_one({"email": email}, {"_id": 0})

def insert_user(user):
    db = database.get_db()
    db["users"].insert_one(user)