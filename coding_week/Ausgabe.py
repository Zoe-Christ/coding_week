import datenbank
import face_recognition



#Datensatz löschen:
#datenbank.delete(3)

#Datensatz einfügen
datenbank.insert((datenbank.givemaxID()+1), "trump_2.jpg")
#datenbank.insert(1, "Jonah_mB.jpeg")

#Datensätze ausgeben

#pic = "basti_1.jpg"
#unknown_image = face_recognition.load_image_file(pic)
#unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
#known_faces = datenbank.ausgeben()
#results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
#print(results)


#pic = "jason-derulo.jpg"
#unknown_image = face_recognition.load_image_file(pic)
#unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
#known_faces = datenbank.ausgeben()
#face_names = datenbank.giveName()
#results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
#print(results)

##Bild von Raspbery löschen
##os.remove('/home/pi/Desktop/unknownPerson.jpg')

##Namen zurückgeben
#try:
#    index = results.index(True)
#    print (face_names[index])
#except ValueError:
#    print ("I'm sorry, I don't know you yet. It's a pleasure to meet you though! Hi, I'm CowIT 18 :)")