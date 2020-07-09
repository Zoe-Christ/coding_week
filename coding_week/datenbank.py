import sqlite3

# Datenbank erstellen

"""
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

"""

# Tabelle erstellen


"""
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    sqlite_create_table_query = '''CREATE TABLE testTable (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                vorname text NOT NULL);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")

"""

# Datensatz einfügen
"""

db=sqlite3.connect('SQLite_Python.db')
qry="insert into testTable (id, name, vorname) values(3, 'Dieterich', 'Antonia');"
try:
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
    print ("one record added successfully")
except:
    print ("error in operation")
    db.rollback()
db.close()
"""

# Datensätze ausgeben 
"""
db=sqlite3.connect('SQLite_Python.db')
sql="SELECT * from testTable;"
cur=db.cursor()
cur.execute(sql)
while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)
db.close()
"""
# Datensatz löschen

"""
db=sqlite3.connect('SQLite_Python.db')
qry="DELETE from testTable where id=3;"
try:
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
    print("record deleted successfully")
except:
    print("error in operation")
    db.rollback()
db.close()
"""
