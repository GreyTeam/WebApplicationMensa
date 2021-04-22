import os
import json

os.mkdir("data")
os.chdir("data")
os.mkdir("prev_tables")

json.dump({
    "totale": 0,
    "users": []
}, open("users.json", "w"), indent=4)

json.dump({
    "totale": 0,
    "prenotazioni": []
}, open("prenotazioni.json", "w"), indent=4)