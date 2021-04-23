import flask
import os
from server import database_utilities, server_utilities, responses, users
from utilities import dates, prenotazioni, log

app: flask.Flask

def setup_routes(flask_app):
    global app
    app = flask_app

def run_routes():

    @app.route('/', methods=['GET'])
    def home():
        return open(f"resources/index_login.html").read()

    # Prenota
    @app.route("/prenota", methods=['POST'])
    def prenota():

        # Controllo se la richiesta soddisfa i requisiti
        if not server_utilities.header_exist("key"):
            response = responses.missing_element_response("key")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            key = server_utilities.get_header("key")

        if not server_utilities.header_exist("x-date"):
            response = responses.missing_element_response("x-date")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            date = server_utilities.get_header("x-date")
            if not dates.verify_date(date):
                response = responses.invalid_date_response()
                log.log("DATE", response["message"], server_utilities.get_headers_list())
                return response

        # Aggiungo al database la prenotazione
        user = users.search_user(key)

        if user is not None:
            if prenotazioni.check_date_reservations(user["email"], date):
                response = responses.reservation_already_registered(date)
                log.log("REGISTERED", response["message"], server_utilities.get_headers_list())
                return response
            else:
                database_utilities.append_user({
                    "nome": user["nome"],
                    "cognome": user["cognome"],
                    "date": date,
                    "email": user["email"]
                })
        else:
            response = responses.key_doesnt_exist()
            log.log("KEY", response["message"], server_utilities.get_headers_list())
            return response

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

    @app.route("/registration", methods=['POST'])
    def register():
        if not server_utilities.header_exist("nome"):
            response = responses.missing_element_response("nome")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            nome = server_utilities.get_header("nome")

        if not server_utilities.header_exist("cognome"):
            response = responses.missing_element_response("cognome")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            cognome = server_utilities.get_header("cognome")

        if not server_utilities.header_exist("key"):
            response = responses.missing_element_response("key")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            key = server_utilities.get_header("key")

        if not server_utilities.header_exist("email"):
            response = responses.missing_element_response("email")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            email = server_utilities.get_header("email")

        if not server_utilities.header_exist("profile_pic"):
            response = responses.missing_element_response("profile_pic")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            profile_pic = server_utilities.get_header("profile_pic")

        users.add_user({
            "nome": nome,
            "cognome": cognome,
            "key": key,
            "profile_pic": profile_pic,
            "email": email
        })

        return {
            "result": "OK"
        }
    
    @app.route('/user/info', methods=["POST"])
    def userinfo():
        if not server_utilities.header_exist("key"):
            response = responses.missing_element_response("key")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            key = server_utilities.get_header("key")

        user = users.search_user(key)

        print(user)

        if user is None:
            response = responses.key_doesnt_exist()
            log.log("KEY", response["message"], server_utilities.get_headers_list())
            return response

        return {
            "result": "OK",
            "fullname": "{0} {1}".format(user["nome"], user["cognome"]),
            "profile_pic": user["profile_pic"]
        }

    @app.route('/chronology', methods=['POST'])
    def chronology():
        if not server_utilities.header_exist("key"):
            response = responses.missing_element_response("key")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            key = server_utilities.get_header("key")

        user = users.search_user(key)

        if user is None:
            response = responses.key_doesnt_exist()
            log.log("KEY", response["message"], server_utilities.get_headers_list())
            return response

        return {
            "result": "OK",
            "chronology": prenotazioni.check_user_reservations(user["email"])
        }

    @app.route('/<resource>', methods=['GET'])
    def res(resource):
        if os.path.isfile(f"resources/{str(resource)}"):
            if ".html" in resource or ".css" in resource or ".js" in resource:
                return open(f"resources/{resource}").read()
            else:
                return open(f"resources/{resource}", "rb").read()
        else:
            return {
                "result": "ERROR",
                "message": "Resource doesn't exist in the server"
            }

    app.run(host="0.0.0.0")
        

