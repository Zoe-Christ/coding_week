
from time import sleep
import datenbank
import face_recognition
import os
from person import person

class raspCam:
    """description of class"""
    

    def __init__(self, camer): 
        self.camera = camer
        self.pics = datenbank.ausgeben()
            
    def takePicture(self):
        try:
            print("pic")
            sleep(5)
            self.camera.capture('/home/pi/Desktop/unknownPerson.jpeg')
            print("picDone")
            
        finally:
            self.camera.stop_preview()

    def recognize(self):
        self.takePicture()
        img = '/home/pi/Desktop/unknownPerson.jpeg' #ggf. Anführungszeichen statt Apostrophe
        #pic = "Zoe.jpeg"
        print("start loading")
        unknown_image = face_recognition.load_image_file(img)
        print("startEncoding")
        try:
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        except IndexError:
            return "Kein Gesicht erkannt!"
        print("doneEncoding")
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
            return self.sadOrHappy(face)
        except ValueError:
            return "I'm sorry, I don't know you yet. It's really nice to meet you though! Hi, I'm CowIt18 :)"

    def sadOrHappy(self, face):
        #Vergleichsbild von DB laden und anschließend Landmarks setzen
        #standard = face_recognition.load_image_file(face.pic)
        print("sadorhappy")
        lm1 = face_recognition.face_landmarks(face.pic)
        
        #Aufgenommenes Bild von Raspberry Pi laden und anschließend Landmarks setzen
        flex = face_recognition.load_image_file("/home/pi/Desktop/unknownPerson.jpeg")
        lm2 = face_recognition.face_landmarks(flex)

        #Arrays des Vergleichbilds zum Speichern der Koordinaten der Landmarks
        xs1 = []
        ys1 = []

        #Arrays des Raspberry-Bilds zum Speichern der Koordinaten der Landmarks
        xs2 = []
        ys2 = []

        #Eintragung der Koordinatenpunkte des gesamten Vergleichsbilds in Arrays (68)
        for landmark1 in lm1:
            for k, v in landmark1.items():
              xs1 += [x[0] for x in v]
              ys1 += [x[1] for x in v]

        #Eintragung der Koordinatenpunkte des gesamten Raspberry-Bilds in Arrays (68)
        for landmark2 in lm2:
            for k, v in landmark2.items():
                xs2 += [x[0] for x in v]
                ys2 += [x[1] for x in v]

        #Statische Werte Kopfbreite auf Augenhöhe bei Vergleichsbilds
        statDB = xs1[16] - xs1[0]

        #Statische Werte Kopfbreite auf Augenhöhe bei Raspberry-Bild
        statRasp = xs2[16] - xs2[0]

        #Ermittlung der Breite des Mundes im Vergleichsbilds
        breiteDB    = xs1[54]-xs1[48]

        #Ermittlung der Breite des Mundes im Raspberry-Bilds
        breiteRasp        = xs2[54]-xs2[48]

        #Ermittlung der Höhe des Mundes im Vergleichsbilds
        hoeheDB = ys1[54]- ys1[48]

        #Ermittlung der Höhe des Mundes im Raspberry-Bilds
        hoeheRasp = ys2[54] -ys2[48]

        #Testausgabe der Werte der Kopfbreite
        ##print("Kopbreite-DB:",statDB,"Kopfbreite-Rasp:",statRasp)

        #Testausgabe der Werte der Breiten
        ##print("Standard-Breite:", breiteDB)
        ##print("Variable-Breite:", breiteRasp)

        #Testausgave der Werte der Höhe
        ##print("Standard-Höhe:", hoeheDB)
        ##print("Variable-Höhe:", hoeheRasp)
        ##print(ys1[54],ys1[48],ys2[54],ys2[48])

        #Vergleich der Mundbreiten, um auf die Emotionslage zu schließen --> noch Test
        ##if breiteRasp>=breiteDB:
        ##    print("Lächeln")
        ##else:
        ##    print("Normal")

        #Vergleich der Mundhöhen, um auf die Emotionslage zu schließen --> noch Test
        ##if hoeheRasp >= hoeheDB:
        ##    print("Lächeln")
        ##else:
        ##    print("Normal")    

        #Verhältnis Kopfbreite zu Mundbreite
        verhaeltDB      = breiteDB / statDB         #Datenbank-Bild (Vergleichsbild)
        verhaeltRasp    = breiteRasp / statRasp     #Raspberry-Bild

        #Testausgabe von Breitenverhältnissen, um auf die Emotion zu schließen
        if verhaeltRasp > verhaeltDB:
            print("l")
            return face.name + " smiles :)"
        elif verhaeltRasp == verhaeltDB:
            print("n")
            return face.name +" looks neutral!"
        else:
            print("t")
            return face.name + " is sad :/"
        #Testausgabe von Landmarks und bestimmten Mundkoordinaten
        ##print(xs1[48], xs1[54])
        ##print(xs2[48], xs2[54])
        ##print(lm1)
        ##print(lm2)

    def addPerson(self, name):
        try:
            os.rename('/home/pi/Desktop/unknownPerson.jpeg', '/home/pi/Desktop/'+ name + '_.jpeg')
            datenbank.insert(datenbank.givemaxID()+1, name + '_.jpeg')
            return "Success!"
        except:
            return "Failed!"
    
    def deletePic(self):
        #Bild von Raspbery löschen
        os.remove('/home/pi/Desktop/unknownPerson.jpeg')