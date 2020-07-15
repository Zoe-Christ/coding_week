from picamera import PiCamera
from time import sleep
import datenbank
import face_recognition
import os
from person import person

class raspCam:
    """description of class"""
    

    def __init__(self): 
        self.camera = PiCamera()
        try:
            self.camera.start_preview()
            sleep(5)
            self.camera.capture('/home/pi/Desktop/unknownPerson.jpeg')
        finally:
            self.camera.stop_preview()
            self.camera.close()
            self.pics = datenbank.ausgeben()
            
        
    def recognize(self):
        img = '/home/pi/Desktop/unknownPerson.jpeg' #ggf. Anführungszeichen statt Apostrophe
        #pic = "Zoe.jpeg"
        unknown_image = face_recognition.load_image_file(img)
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        names = []
        known_faces = []
        for i in range(len(self.pics)):
            known_faces.append(face_recognition.face_encodings(self.pics[i].pic)[0])
        results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
        print(results)

        #Namen zurückgeben
        try:
            index = results.index(True)
            face = person(self.pics[index].name, self.pics[index].pic)
            return face
        except ValueError:
            return "I'm sorry, I don't know you yet. It's really nice to meet you though! Hi, I'm CowIt18 :)"

    def sadOrHappy(self, face):
        #standard = face_recognition.load_image_file(face.pic)
        landmarks = face_recognition.face_landmarks(face.pic)

        flex = face_recognition.load_image_file("/home/pi/Desktop/unknownPerson.jpeg")
        lm1 = face_recognition.face_landmarks(flex)

        xs1 = []
        ys1 = []

        xs2 = []
        ys2 = []

        for landmark1 in landmarks:
            for k, v in landmark1.items():
              xs1 += [x[0] for x in v]
              ys1 += [x[1] for x in v]

        for landmark2 in lm1:
            for k, v in landmark2.items():
                xs2 += [x[0] for x in v]
                ys2 += [x[1] for x in v]

        durchschnitt    = xs1[55]-xs1[49]
        varWert         = xs2[55]-xs2[49]

        print("Standard:", durchschnitt)
        print("Variable:", varWert)

        if varWert>durchschnitt:
            return "lächelt"
        else:
            return "ist traurig"

    def deletePic(self):
        #Bild von Raspbery löschen
        os.remove('/home/pi/Desktop/unknownPerson.jpeg')