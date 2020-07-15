#Importieren von Face-Recognition, MG
import face_recognition as fr

#Vergleichsbild von DB laden und anschließend Landmarks setzen
standard = fr.load_image_file("/Users/mauricegeisen/Documents/coding_week/coding_week/basti_2.jpg")
lm1 = fr.face_landmarks(standard)

#Aufgenommenes Bild von Raspberry Pi laden und anschließend Landmarks setzen
flex = fr.load_image_file("/Users/mauricegeisen/Documents/coding_week/coding_week/basti_1.jpg")
lm2 = fr.face_landmarks(flex)

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
    print("Lächelt, da Raspberry(",verhaeltRasp,") größer als Datenbank(",verhaeltDB,") ist.")
elif verhaeltRasp == verhaeltDB:
    print("Neutral, da Raspberry(",verhaeltRasp,") gleich Datenbank(",verhaeltDB,") ist.") 
else:
    print("Traurig, da Raspberry(",verhaeltRasp,") kleiner als Datenbank(",verhaeltDB,") ist.")       
#Testausgabe von Landmarks und bestimmten Mundkoordinaten
##print(xs1[48], xs1[54])
##print(xs2[48], xs2[54])
##print(lm1)
##print(lm2)
    