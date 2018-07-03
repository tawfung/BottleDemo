from bottle import request, run, route, template, static_file, post, get
import os
import psycopg2

hostname = 'localhost'
username = 'test'
password = 'te5tpa55'
database = 'testdb'

# Static Routes
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@get("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="static/fonts")

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/images")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@get("/static/vendor/<filepath:re:.*\.vendor>")
def js(filepath):
    return static_file(filepath, root="static/vendor")

@route('/login')
def login():
    return template('templates/login.html')

@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    # print(check_login(username, password))
    if check_login(username, password):
        return "<p>Congrats!</p>"
    else:
        return "<p>Failed!</p>"

def check_login(user, pwd):
    myConnection = psycopg2.connect(host=hostname, dbname=database, user=username, password=password)
    # create a psycopg2 cursor that can execute queries
    cursor = myConnection.cursor()
    # run a SELECT statement
    cursor.execute("SELECT COUNT(1) FROM users WHERE name= '{0}';".format(user))
    if cursor.fetchone()[0]:
        cursor.execute("SELECT password FROM users WHERE name='{0}';".format(user))
        for row in cursor.fetchall():
            # print(row[0].strip(), 'and', pwd)
            if pwd == row[0].strip():
                return True
            else:
                return False
    # else:
    #     return False
    # data = cursor.fetchall()
    # if user in data['name']:
    #     if pwd == data[user]['password']:
    #         return True
    # return False


if __name__ == "__main__":
    port = os.environ.get('PORT', 8080)
    run(host=hostname, port=port, debug=True)