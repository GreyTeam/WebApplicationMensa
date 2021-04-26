import os
import json
import shutil

if os.path.isdir("data"):
    shutil.rmtree("data")
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

json.dump([], open("log.json", "w"), indent=4)