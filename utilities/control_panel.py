from utilities import prenotazioni
from datetime import datetime
import xlsxwriter

def create_xlsx_file():

    data = prenotazioni.get_day_list()

    workbook = xlsxwriter.Workbook('data/prev_tables/' + datetime.now().strftime("%d_%m") + "xmlx")
    titles = workbook.add_format({'bold': True, 'font_color': 'white', 'bg_color': 'red'})
    bold = workbook.add_format({'bold': True})

    worksheet = workbook.add_worksheet()

    worksheet.write(0, 4, 'Totale:')
    worksheet.write(0, 5, len(data), titles)

    worksheet.write(0, 0, 'Cognome', titles)
    worksheet.write(0, 1, 'Nome', titles)
    worksheet.write(0, 2, 'Email', titles)

    lastname_max_width = 0
    firstname_max_width = 0
    email_max_width = 0

    for i, user in enumerate(data):
        worksheet.write(i+1, 0, user["cognome"], bold)
        width = len(user["cognome"])
        if lastname_max_width < width:
            worksheet.set_column(0, 0, width)
            lastname_max_width = width

        worksheet.write(i+1, 1, user["nome"], bold)
        width = len(user["nome"])
        if firstname_max_width < width:
            worksheet.set_column(1, 1, width)
            firstname_max_width = width

        worksheet.write(i+1, 2, user["email"], bold)
        width = len(user["email"])
        if email_max_width < width:
            worksheet.set_column(2, 2, width)
            email_max_width = width

    workbook.close()