import datenbank
import face_recognition


#Datensatz löschen:
#datenbank.delete(3)

#Datensatz einfügen
#datenbank.insert((datenbank.givemaxID()+1), "Zoe.jpeg")

#Datensätze ausgeben

#pic = "basti_1.jpg"
#unknown_image = face_recognition.load_image_file(pic)
#unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
#known_faces = datenbank.ausgeben()
#results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
#print(results)
pic = "Sandra_oB.jpeg"
unknown_image = face_recognition.load_image_file(pic)
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
known_faces = datenbank.ausgeben()
face_names = datenbank.giveName()
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
print(results)

#Bild von Raspbery löschen
#os.remove('/home/pi/Desktop/unknownPerson.jpg')

#Namen zurückgeben
index = results.index(True)
#if index == none:
 #   print( "I'm sorry, I don't know you yet. It's a pleasure to meet you though! Hi, I'm CowIT 18 :)")
#else: 
print (face_names)

#datenbank.deleteTable()



