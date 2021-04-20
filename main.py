import flask
from server import server_routes, database_utilities, server_utilities, responses
from utilities import dates

# Setup server
app = flask.Flask(__name__)
app.config["DEBUG"] = True

server_routes.setup_routes(app)
server_routes.run_routes()