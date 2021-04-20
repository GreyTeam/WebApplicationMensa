import server.responses
import flask

def verify_header_exist(header):
    req = flask.request.headers.get(header)
    return False if req is None else True

def get_header(header):
    return flask.request.headers.get(header)