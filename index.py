from sys import argv
from bottle import *


@route("/")
def index():
    return template("index.tpl")

@route("/generic")
def generic():
    return template("generic.tpl")

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

@route('/js/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root='js')

@route('/images/<filename>')
def server_static(filename):
    return static_file(filename, root="images")

run(host='0.0.0.0', port=argv[1])
