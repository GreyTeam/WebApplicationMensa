import flask
from server import server_routes, database_utilities, server_utilities, responses
from utilities import dates, control_panel

# Setup serve

def run():
    app = flask.Flask(__name__)

    server_routes.setup_routes(app)
    server_routes.run_routes()