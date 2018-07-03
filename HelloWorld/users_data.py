#!/usr/bin/python

hostname = 'localhost'
username = 'test'
password = 'te5tpa55'
database = 'testdb'

#Simple routine to run a query on a database and print the results:
def doQuery1(conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (id, name, password, age, email, address, salary) "
                "VALUES (100,'trace1','tr4c3',23, 'trace1@enclave.vn', 'Danang', 8000)")
    cur.execute("SELECT name, age, email FROM users")
    for name, age, email in cur.fetchall():
        print(name, age, email)
    conn.commit()


def doQuery2(conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (id, name, password, age, email, address, salary) "
                "VALUES (101,'trace2','tr4c3',23, 'trace2@enclave.vn', 'Danang', 8000)")
    cur.execute("SELECT name, age, email FROM users")
    for name, age, email in cur.fetchall():
        print(name, age, email)
    conn.commit()

print("Using psycopg2...")
import psycopg2
myConnection = psycopg2.connect(host=hostname, dbname=database, user=username, password=password)
doQuery1(myConnection)
myConnection.close()

print("Using PyGreSQL...")
import pgdb
myConnection = pgdb.connect(host=hostname, user=username, password=password, database=database)
doQuery2(myConnection)
myConnection.close()


