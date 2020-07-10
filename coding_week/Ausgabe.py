import datenbank
import face_recognition


#Datensatz löschen:
#datenbank.delete(3)

#Datensatz einfügen

#datenbank.insert(5, "basti_2.jpg")

#Datensätze ausgeben


pic = "basti_1.jpg"
unknown_image = face_recognition.load_image_file(pic)
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
known_faces = datenbank.ausgeben()
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
print(results)


