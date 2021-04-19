import flask
import responses
import database_utilities
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
    firstname = flask.request.headers.get("firstname")
    print(firstname)
    if firstname is None:
        # Ritorno l'errore
        return responses.missingElementsResponse

    lastname = flask.request.headers.get("lastname")
    print(lastname)
    if lastname is None:
        # Ritorno l'errore
        return responses.missingElementsResponse

    # Aggiungo al database la prenotazione
    database_utilities.append_user({
        "nome": firstname,
        "cognome": lastname
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


app.run()