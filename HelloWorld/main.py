from bottle import run, route, jinja2_view, TEMPLATE_PATH

TEMPLATE_PATH[:] = ['templates']
HOST = 'localhost'

@route('/', name='home')
@jinja2_view('index.html')
def server_hompage():
    return {'title': 'Hello'}

run(host=HOST, port=8080, debug=True)