from bottle import route, run, static_file, get, template
import os
import psycopg2

hostname = 'localhost'
username = 'test'
password = 'te5tpa55'
database = 'testdb'

@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/static')

@route('/table')
def table():
    myConnection = psycopg2.connect(host=hostname, dbname=database, user=username, password=password)
    # create a psycopg2 cursor that can execute queries
    cursor = myConnection.cursor()
    # run a SELECT statement
    cursor.execute("SELECT * FROM students;")
    result = cursor.fetchall()
    cursor.close()
    return template('templates/table.html', rows=result)

if __name__ == "__main__":
    port = os.environ.get('PORT', 8080)
    run(host='0.0.0.0', port=port, debug=True)