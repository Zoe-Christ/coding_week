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
    qry="""insert into FaceImages (foto_id, byteArr) values(?, ?);"""
    try:
        cur=db.cursor()
        recordTuple = (id, byteArr)
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
        #print (record)
        #image.open(io.BytesIO(record[1]), mode = 'r')
        img2 = face_recognition.load_image_file(io.BytesIO(record[1]))
        uf = face_recognition.face_encodings(img2)[0]
        known_faces.append(uf)
        #img.show(record)
    db.close()
    return known_faces
  

# Datensatz löschen


def delete(id):
    db=sqlite3.connect('SQLite_Python.db')
    qry="""DELETE from FaceImages where face_id= ?;"""
    try:
        cur=db.cursor()
        
        cur.execute(qry, (id, ))
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
                                    byteArr BLOB);'''

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