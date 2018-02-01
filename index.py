from bottle import *


@route("/")
def index():
    return template("index.tpl")

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='css')

@route('/js/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root='js')

@route('/images/<filename>')
def server_static(filename):
    return static_file(filename, root="images")

run(host="localhost", port="8080", debug=True)