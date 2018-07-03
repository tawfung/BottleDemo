from bottle import template, run, route
import psycopg2
hostname = 'localhost'
username = 'test'
password = 'te5tpa55'
database = 'testdb'
@route('/user')
def show():
    myConnection = psycopg2.connect(host=hostname, dbname=database, user=username, password=password)
    # create a psycopg2 cursor that can execute queries
    cursor = myConnection.cursor()
    # run a SELECT statement
    cursor.execute("""SELECT id,name,age,address,salary FROM users""")
    data = cursor.fetchall()
    output = template('bring_to_picnic', rows=data)
    return output

run(host="localhost", port=8080, debug=True)