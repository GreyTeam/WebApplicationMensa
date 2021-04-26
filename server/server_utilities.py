from server import responses
import flask

def header_exist(header):
    req = flask.request.headers.get(header)
    return False if req is None else True

def get_header(header):
    return flask.request.headers.get(header)

def get_headers_list():
    return dict(flask.request.headers)