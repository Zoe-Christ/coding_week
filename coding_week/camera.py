from picamera import PiCamera
from time import sleep
import datenbank
import face_recognition
import os

class raspCam:
    """description of class"""
    

    def __init__(self, camera): 
        self.camera = picamera.PiCamera()
        try:
            self.camera.start_preview()
            sleep(5)
            self.camera.capture('/home/pi/Desktop/unknownPerson.jpeg')
        finally:
            self.camera.stop_preview()
            self.camera.close()
        

    def recognize ():
        #sleep(5)
        #self.camera.capture('/home/pi/Desktop/unknownPerson.jpeg')
        #self.camera.stop_preview()

        #pic = '/home/pi/Desktop/unknownPerson.jpg' #ggf. Anführungszeichen statt Apostrophe
        #pic = "Zoe.jpeg"
        #unknown_image = face_recognition.load_image_file(pic)
        #unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        #known_faces = datenbank.ausgeben()
        #face_names = datenbank.giveName()
        #results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
        #print(results)

        #Bild von Raspbery löschen
        #os.remove('/home/pi/Desktop/unknownPerson.jpg')

        #Namen zurückgeben
        #try:
           #index = results.index(True)
           #return face_names[index]
        #except ValueError:
           #return "I'm sorry, I don't know you yet. It's a pleasure to meet you though! Hi, I'm CowIT 18 :)"