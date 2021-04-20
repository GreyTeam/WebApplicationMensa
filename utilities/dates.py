from datetime import datetime, timedelta

days_name = [
    "Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"
]

months_name = [
    "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio",
    "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
]

def get_next_day(delta):
    date = datetime.today() + timedelta(days=delta)
    return {
        "text": "{0} {1} {2}".format(days_name[date.weekday()], str(date.day), months_name[date.month - 1]),
        "value": date.strftime("%d/%m")
    }

def create_days_list():
    days = []
    delta = 0
    for day in range(8):
        day_value = get_next_day(day + delta)
        day_to_string = day_value["value"] + f"/{str(datetime.now().year)}"
        if days_name[datetime.strptime(day_to_string, "%d/%m/%Y").weekday()] == "Sab":
            delta += 1
        else:
            days.append(get_next_day(day + delta))
    return days

def verify_date(date):
    list = create_days_list()
    print(list)
    for d in list:
        if d["value"] == date:
            return True
    return False

    