from bottle import run, route, template, request

@route('/hello/<val>', method='PATCH')
def index(val=None):
    passw = 'secrete'
    request.method == 'PATCH'
    strBodyText = request.body.read()
    if strBodyText == passw:
        return template('<b> Hello {{name}}!</b>', name=val)
    else:
        return template('<b>Password is invalid!</b>')
run(host='localhost', port=8080, debug=True)