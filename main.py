import flask
from server import server_routes, database_utilities, server_utilities, responses
from utilities import dates, control_panel

control_panel.create_xlsx_file()

# Setup server
app = flask.Flask(__name__)
app.config["DEBUG"] = True

server_routes.setup_routes(app)
server_routes.run_routes()