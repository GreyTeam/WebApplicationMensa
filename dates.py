import datetime

days_name = [
    "Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"
]

months_name = [
    "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio",
    "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
]

def get_next_day(delta):
    date = datetime.datetime.today() + datetime.timedelta(days=delta)
    return {
        "text": "{0} {1} {2}".format(days_name[date.weekday()], str(date.day), months_name[date.month - 1]),
        "value": date.strftime("%d/%m")
    }

def create_days_list():
    list = []
    for day in range(8):
        list.append(get_next_day(day))
    return list

def verify_date(date):
    list = create_days_list()
    print(list)
    for d in list:
        if d["value"] == date:
            return True
    return False