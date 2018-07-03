from bottle import run, route, template

# app = Bottle()
@route('/')
@route('/hello')
# @app.route('/hello')
def hello():
    return "Hello World!"

@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)


run(host='localhost', port=8080, debug=True)