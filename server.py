import flask
import responses
import database_utilities
import server_utilities
import dates

# Setup server
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Home
@app.route('/', methods=['GET'])
def home():
    return open("index.html").read()

# CSS
@app.route('/index.css', methods=['GET'])
def css():
    print("CSS")
    return open("index.css").read()

# JS
@app.route('/index.js', methods=['GET'])
def js():
    return open("index.js").read()

# Prenota
@app.route("/prenota", methods=['POST'])
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