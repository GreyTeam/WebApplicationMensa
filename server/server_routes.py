import flask
import os
from server import database_utilities, server_utilities, responses, users
from utilities import dates, prenotazioni

app: flask.Flask

def setup_routes(flask_app):
    global app
    app = flask_app

def run_routes():

    @app.route('/', methods=['GET'])
    def home():
        return open(f"resources/index.html").read()

    # Prenota
    @app.route("/prenota", methods=['POST'])
    def prenota():

        # Controllo se la richiesta soddisfa i requisiti
        print("Arrivato")
        if not server_utilities.header_exist("key"):
            return responses.missing_element_response("key")
        else:
            key = server_utilities.get_header("key")

        if not server_utilities.header_exist("date"):
            return responses.missing_element_response("date")
        else:
            date = server_utilities.get_header("date")
            if not dates.verify_date(date):
                return responses.invalid_date_response()

        # Aggiungo al database la prenotazione
        user = users.search_user(key)

        if user is not None:
            if prenotazioni.check_reservation(user["email"], date):
                return responses.reservation_already_registered(date)
            else:
                database_utilities.append_user({
                    "nome": user["nome"],
                    "cognome": user["cognome"],
                    "date": date,
                    "email": user["email"]
                })
        else:
            return responses.key_doesnt_exist()

        # Ritorno OK al client
        return {
            "result": "OK"
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
        
        if not server_utilities.header_exist("key"):
            return responses.missing_element_response("key")
        else:
            key = server_utilities.get_header("key")
            
            user = users.search_user(key)
            if user is not None:
                user["result"] = "OK"
                return user
            else:
                return responses.key_doesnt_exist()

    @app.route("/registration", methods=['POST'])
    def register():
        if not server_utilities.header_exist("nome"):
            return responses.missing_element_response("nome")
        else:
            nome = server_utilities.get_header("nome")

        if not server_utilities.header_exist("cognome"):
            return responses.missing_element_response("cognome")
        else:
            cognome = server_utilities.get_header("cognome")

        if not server_utilities.header_exist("key"):
            return responses.missing_element_response()
        else:
            key = server_utilities.get_header("key")

        if not server_utilities.header_exist("email"):
            return responses.missing_element_response("email")
        else:
            email = server_utilities.get_header("email")

        users.add_user({
            "nome": nome,
            "cognome": cognome,
            "key": key,
            "email": email
        })

        return {
            "result": "OK"
        }

    @app.route('/chronology', methods=['POST'])
    def chronology():
        if not server_utilities.header_exist("key"):
            return responses.missing_element_response("key")
        else:
            key = server_utilities.get_header("key")

        user = users.search_user(key)

        if user is None:
            return responses.key_doesnt_exist()

        return {
            "result": "OK",
            "chronology": prenotazioni.check_user_reservations(user["email"])
        }

    @app.route('/resource/<resource>', methods=['GET'])
    def res(resource):
        if os.path.isfile(f"resources/{resource}"):
            return open(f"resources/{resource}").read()
        else:
            return {
                "result": "ERROR",
                "message": "Resource doesn't exist in the server"
            }

    app.run()
        

