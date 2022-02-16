import mysql.connector

def dbConnector():
    myDb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            port='3306',
            database='cryptopricedb'
    )
    return myDb


