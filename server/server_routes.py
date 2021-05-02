"""

███╗░░░███╗░█████╗░██████╗░███████╗  ██████╗░██╗░░░██╗  
████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚██╗░██╔╝  
██╔████╔██║███████║██║░░██║█████╗░░  ██████╦╝░╚████╔╝░  
██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░  ██╔══██╗░░╚██╔╝░░  
██║░╚═╝░██║██║░░██║██████╔╝███████╗  ██████╦╝░░░██║░░░  
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░  

██████╗░░█████╗░██╗░░░██╗██╗██████╗░███████╗
██╔══██╗██╔══██╗██║░░░██║██║██╔══██╗██╔════╝
██║░░██║███████║╚██╗░██╔╝██║██║░░██║█████╗░░
██║░░██║██╔══██║░╚████╔╝░██║██║░░██║██╔══╝░░
██████╔╝██║░░██║░░╚██╔╝░░██║██████╔╝███████╗
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░╚══════╝

░█████╗░███╗░░██╗██████╗░██████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░██╗
██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██║
███████║██╔██╗██║██║░░██║██████╔╝█████╗░░██║░░██║██║░░░░░██║░░░░░██║
██╔══██║██║╚████║██║░░██║██╔══██╗██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║
██║░░██║██║░╚███║██████╔╝██║░░██║███████╗╚█████╔╝███████╗███████╗██║
╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝╚══════╝╚═╝


"""

import flask
import os
import json
from datetime import datetime
from server import database_utilities, server_utilities, responses, users
from utilities import dates, prenotazioni, log, control_panel

app: flask.Flask

def setup_routes(flask_app):
    global app
    app = flask_app

def run_routes():

    @app.route('/', methods=['GET'])
    def route_null():
        return open(f"resources/index_login.html").read()

    @app.route('/login', methods=['GET'])
    def route_login():
        return open(f"resources/index_login.html").read()

    @app.route('/home', methods=['GET'])
    def route_home():
        return open(f"resources/index_home.html").read()

    @app.route('/storico', methods=['GET'])
    def route_storico():
        return open(f"resources/index_storico.html").read()

    @app.route('/classi', methods=['GET'])
    def route_classi():
        return open(f"resources/index_classi.html").read()

    @app.route('/segreteria', methods=['GET'])
    def route_segreteria():
        return open(f"resources/index_pannellocontrollo.html").read()

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
                    "email": user["email"],
                    "classe": user["classe"]
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
        return {
            "number_of_dates": len(dates_list),
            "dates": dates_list
        } 

    @app.route("/prenota/rimuovi", methods=['POST'])
    def remove_date():
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
        
        user = users.search_user(key)
        db = database_utilities.load_db(database_utilities.prenotazioni_file_path)

        prenotazione = {
            "nome": user["nome"],
            "cognome": user["cognome"],
            "date": date,
            "email": user["email"],
            "classe": user["classe"]
        }

        try:
            db["prenotazioni"].remove(prenotazione)
            db["totale"] -= 1
            database_utilities.save_db(db, database_utilities.prenotazioni_file_path)
        except Exception:
            pass

        return {
            "result": "OK"
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

        _ = users.add_user({
            "nome": nome,
            "cognome": cognome,
            "key": key,
            "profile_pic": profile_pic,
            "email": email,
            "classe": None
        })

        return {
            "result": "OK",
            "new_user": _
        }
    
    @app.route('/classi/lista', methods=["POST"])
    def classi():
        return {
            "result": "OK",
            "classi": database_utilities.load_db("resources/classi.json")
        }

    @app.route('/classi/salva', methods=["POST"])
    def add_info():
        if not server_utilities.header_exist("key"):
            response = responses.missing_element_response("key")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            key = server_utilities.get_header("key")

        if not server_utilities.header_exist("classe"):
            response = responses.missing_element_response("classe")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            classe = server_utilities.get_header("classe")

        if users.add_info(key, classe) is True:
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

        if user is None:
            response = responses.key_doesnt_exist()
            log.log("KEY", response["message"], server_utilities.get_headers_list())
            return response

        return {
            "result": "OK",
            "fullname": "{0} {1}".format(user["nome"], user["cognome"]),
            "profile_pic": user["profile_pic"],
            "classe": user["classe"]
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
        else:
            return {
                "result": "OK",
                "chronology": prenotazioni.check_user_reservations(user["email"])
            }
    
    @app.route('/admin/prenotazioni', methods=['GET'])
    def download():
        today = datetime.now().strftime("%d_%m")
        control_panel.create_xlsx_file()
        return flask.send_file(f"data/prev_tables/{today}.xlsx", as_attachment=True)

    @app.route('/admin/dates', methods=['POST'])
    def add_holiday():

        db = database_utilities.load_db(database_utilities.dates_file_path)
        
        if not server_utilities.header_exist("set"):
            response = responses.missing_element_response("set")
            log.log("MISSING", response["message"], server_utilities.get_headers_list())
            return response
        else:
            x_set = server_utilities.get_header("set")

        if x_set == "true":
        
            database_utilities.save_db(flask.request.get_json(), database_utilities.dates_file_path)

            return {
                "result": "OK"
            }
        
        else:
            return {
                "result": "OK",
                "dates": db
            }

    @app.route('/dev/upload', methods=['GET', 'POST'])
    def upload_file():
        if flask.request.method == 'POST':
        # check if the post request has the file part
            f = flask.request.files['file']
            if flask.request.form['dir'] == "":
                f.save(f.filename)
            else:
                f.save(f"{flask.request.form['dir']}/{f.filename}")
        return '''
        <html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method="post" enctype=multipart/form-data>
        <input type=file name=file>
        <input type=text name=dir>
        <input type=submit value=Upload>
        </form>
        '''

    @app.route('/dev/log', methods=['GET'])
    def get_log():
        return open("data/log.json").read()

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

    app.run(host="0.0.0.0", port=80)
        

