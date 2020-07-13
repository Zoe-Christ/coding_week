import sqlite3
import face_recognition

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

def insert(id, fileName):
    import io
    from io import BytesIO
    from PIL import Image
    with Image.open(fileName) as img:
        byteIO = io.BytesIO()
        img.save(byteIO, format='PNG')
    byteArr = byteIO.getvalue()
    db=sqlite3.connect('SQLite_Python.db')
    qry="""insert into FaceImages (foto_id, byteArr, name) values(?, ?, ?);"""
    try:
        cur=db.cursor()
        recordTuple = (id, byteArr, fileName)
        cur.execute(qry, recordTuple)
        db.commit()
        print ("one record added successfully")
    except:
        print ("error in operation")
        db.rollback()
    db.close()
    return


# Datensätze ausgeben 

def ausgeben():
    import io
    from io import BytesIO
    from PIL import Image
    db=sqlite3.connect('SQLite_Python.db')
    sql="SELECT * from FaceImages;"
    cur=db.cursor()
    cur.execute(sql)
    known_faces = []
    while True:
        record=cur.fetchone()
        if record==None:
            break
        img2 = face_recognition.load_image_file(io.BytesIO(record[1]))
        uf = face_recognition.face_encodings(img2)[0]
        known_faces.append(uf)
    db.close()
    return known_faces

#Max id ausgeben
def givemaxID():
    db=sqlite3.connect('SQLite_Python.db')
    qry="""SELECT MAX(foto_id) FROM FaceImages;"""
    maxID=1
    try:
        cur=db.cursor()
        cur.execute(qry)
        record = cur.fetchone()
        #db.commit()
        
        maxID = record[0]
        #print(maxID)
    except:
        print("error in operation")
    db.close()
    return maxID

# Namen ausgeben 
def giveName():
    db=sqlite3.connect('SQLite_Python.db')
    qry="SELECT * FROM FaceImages;"
    cur = db.cursor()
    cur.execute(qry)
    names = []
    while True:
        record = cur.fetchone()
        if record==None:
            break
        names.append(record[2])
    db.close
    return names

# Datensatz löschen


def delete():
    db=sqlite3.connect('SQLite_Python.db')
    qry="DELETE from FaceImages where foto_id=11;"
    try:
        cur=db.cursor()
        
        cur.execute(qry)
        db.commit()
        print("record deleted successfully")
    except:
        print("error in operation")
        db.rollback()
    db.close()
    return

"""
import sqlite3
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    sqlite_create_table_query = '''CREATE TABLE FaceImages (
                                    foto_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    byteArr BLOB, name TEXT);'''

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

def deleteTable():
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    dropTableStatement = "DROP TABLE FaceImages"
    cursor.execute(dropTableStatement)
    sqliteConnection.close()

