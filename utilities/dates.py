import datetime
from server.database_utilities import *

days_name = [
    "Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"
]

months_name = [
    "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio",
    "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
]

def get_next_day(delta, year=True):
    date = datetime.datetime.now() + datetime.timedelta(days=delta)
    if not year:
        return date.strftime("%d/%m/%Y")
    else:
        return {
            "text": "{0} {1} {2}".format(days_name[date.weekday()], str(date.day), months_name[date.month - 1]),
            "value": date.strftime("%d/%m")
        }

def is_holiday(date):
    db = load_db(dates_file_path)
    day = datetime.datetime.strptime(date, "%d/%m/%Y")
    for date_db in db:
        date_parsed = datetime.datetime.strptime(date_db, "%d/%m/%y")
        if day == date_parsed:
            return True
    return False

def create_days_list():
    days = []
    delta = 0
    for day in range(8):
        day_value = get_next_day(day + delta)
        day_to_string = day_value["value"] + f"/{str(datetime.datetime.now().year)}"
        if days_name[datetime.datetime.strptime(day_to_string, "%d/%m/%Y").weekday()] == "Sab":
            delta += 1
        else:
            if not is_holiday(get_next_day(day + delta, year=False)):
                days.append(day_value)
    return days

def verify_date(date):
    d_list = create_days_list()
    print(d_list)
    for d in d_list:
        if d["value"] == date:
            return True
    return False

    