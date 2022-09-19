import sqlite3

#from chartdata.index import app


def create_connection(db_file):

    conn = None
    try:
        #with app.app_context():
            #cur = mysql.connection.cursor()
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)

    return conn
