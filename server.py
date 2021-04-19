import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    with open("index.html") as f:
        return str(f.read())
    
@app.route('/index.css', methods=['GET'])
def css():
    with open("index.css") as f:
        return str(f.read())

@app.route('/index.js', methods=['GET'])
def js():
    with open("index.js") as f:
        return str(f.read())

@app.route("/prenota", methods=['POST'])
def prenota():
    print("Arrived")
    return "Prenotato"

app.run()