import flask

# Setup server
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Home
@app.route('/', methods=['GET'])
def home():
    with open("index.html") as f:
        return str(f.read())

# CSS
@app.route('/index.css', methods=['GET'])
def css():
    with open("index.css") as f:
        return str(f.read())

# JS
@app.route('/index.js', methods=['GET'])
def js():
    with open("index.js") as f:
        return str(f.read())

# Prenota
@app.route("/prenota", methods=['POST'])
def prenota():
    firstname = str(flask.request.form.get("firstname"))
    lastname = str(flask.request.form.get("lastname"))
    return {
        "result": "OK",
        "firstname": firstname,
        "lastname": lastname
    }

app.run()