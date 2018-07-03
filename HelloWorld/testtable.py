from bottle import route, run, static_file, get, template
import os

@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/static')

@route('/table')
def login():
    return template('templates/index.html')

if __name__ == "__main__":
    port = os.environ.get('PORT', 8080)
    run(host='0.0.0.0', port=port, debug=True)