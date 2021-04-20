import flask
import os
from server import database_utilities, server_utilities, responses
from utilities import dates

app: flask.Flask

def setup_routes(flask_app):
    global app
    app = flask_app

def run_routes():

    @app.route('/', methods=['GET'])
    def home():
        return open(f"resources/index.html").read()

    @app.route('/<resource>', methods=['GET'])
    def res(resource):
        if os.path.isfile(f"resources/{resource}"):
            return open(f"resources/{resource}").read()
        else:
            return {
                "result": "ERROR",
                "message": "Resource doesn't exist in the server"
            }

    # Prenota
    @app.route("/rest/prenota", methods=['POST'])
    def prenota():

        # Controllo se la richiesta soddisfa i requisiti
        if not server_utilities.verify_header_exist("firstname"):
            return responses.missingElementsResponse
        else:
            firstname = server_utilities.get_header("firstname")

        if not server_utilities.verify_header_exist("lastname"):
            return responses.missingElementsResponse
        else:
            lastname = server_utilities.get_header("lastname")

        if not server_utilities.verify_header_exist("date"):
            return responses.missingElementsResponse
        else:
            date = server_utilities.get_header("date")
            if not dates.verify_date(date):
                return responses.invalidDateResponse

        # Aggiungo al database la prenotazione
        database_utilities.append_user({
            "nome": firstname,
            "cognome": lastname,
            "date": date
        })

        # Ritorno OK al client
        return {
            "result": "OK",
            "firstname": firstname,
            "lastname": lastname
        }

    @app.route("/prenota/date", methods=['POST'])
    def date():
        dates_list = dates.create_days_list()
        print(dates_list)
        return {
            "number_of_dates": len(dates_list),
            "dates": dates_list
        } 

    @app.route("/login", methods=['POST'])
    def login():
        
        if not server_utilities.verify_header_exist("key"):
            return responses.missingElementsResponse
        else:
            key = server_utilities.get_header("key")

        if not server_utilities.verify_header_exist("email"):
            return responses.missingElementsResponse
        else:
            email = server_utilities.get_header("email")

    app.run()
        

