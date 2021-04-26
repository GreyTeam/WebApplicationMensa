from server.database_utilities import *
from datetime import datetime

def log(l_type, message, info):
    print("{0}: {1}", l_type, message)
    db = load_db(log_file_path)
    db.append({
        "type": l_type,
        "message": message,
        "info": info,
        "timestamp": datetime.now().timestamp()
    })
    save_db(db, log_file_path)
    