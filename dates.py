import datetime

days_name = [
    "Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"
]

months_name = [
    "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio",
    "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
]

def get_next_days(delta):
    date = datetime.datetime.today() + datetime.timedelta(days=delta)
    return "{0} {1} {2}".format(
        days_name[date.weekday()],
        str(date.day),
        months_name[date.month - 1]
    )

def create_days_list():
    list = []
    for day in range(8):
        list.append(get_next_days(day))
    return list