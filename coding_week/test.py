from raspCam import raspCam
from camera import *
from person import person
#import sqlite3
#import datenbank  #delete
#import face_recognition

cam = raspCam()
#print(cam.recognize())
s = cam.recognize()
t = cam.sadOrHappy(s)
print(s.name, t)
cam.deletePic()

#delete below
#pics = datenbank.ausgeben()

#pic = "ZoeS.jpeg"
#unknown_image = face_recognition.load_image_file(pic)
#unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
#names = []
#known_faces = []
#for i in range(len(pics)):
#    known_faces.append(face_recognition.face_encodings(pics[i].pic)[0])
#results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
#print(results)

##Namen zurückgeben
#try:
#    index = results.index(True)
#    face = person(pics[index].name, pics[index].pic)
#    print(face.name, face.pic)
#except ValueError:
#    print("I'm sorry, I don't know you yet. It's really nice to meet you though! Hi, I'm CowIt18 :)")