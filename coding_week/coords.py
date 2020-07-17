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

#Statische Werte Kopfhöhe auf Augenhöhe bei Vergleichsbild aus Datenbank
stathDB = ys1[1] - ys1[0]

#Statische Werte Kopfhöhe auf Augenhöhe bei Raspberry-Bild
stathRasp = ys2[1] - ys2[0]

#Statische Werte von Kinn bis Augen bei Vergleichsbild
##statKMdb = ys1[8] - ys1[27]

#Statische Werte von Kinn bis Augen bei Raspberry-Bild
##statKMRasp = ys2[8] - ys2[27]

#Ermittlung der Breite des Mundes im Vergleichsbilds
breiteDB    = xs1[54]-xs1[48]

#Ermittlung der Breite des Mundes im Raspberry-Bilds
breiteRasp  = xs2[54]-xs2[48]

#Ermittlung der Höhe des Mundes im Vergleichsbilds
hoeheDB = ys1[57] - ys1[48]

#Ermittlung der Höhe des Mundes im Raspberry-Bilds
hoeheRasp = ys2[57] - ys2[48]

#Ermittlung der Höhe, ob Mund geöffnet ist im Vergleichsbild
lachenDB = ys1[62] - ys1[66] 

#Ermittlung der Höhe, ob Mund geöffnet ist im Raspberry-Bild
lachenRasp = ys2[62] - ys2[66] 

#Ermittlung der Höhe von Kinn bis Mund im Vergleichsbild
    #

#Ermittlung der Höhe von Kinn bis Mund im Raspberry-Bild
    #

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
verhaeltBDB      = breiteDB / statDB         #Datenbank-Bild (Vergleichsbild)
verhaeltBRasp    = breiteRasp / statRasp     #Raspberry-Bild

#Verhältnis Kopfhöhe zu Mundhöhe
verhaeltHDB     = hoeheDB / stathDB
verhaeltHRasp   = hoeheRasp / stathRasp

#Verhältnis Mundhöhe (Lippen) zu Kopfhöhe
verhaeltLachDB      = lachenDB / stathDB
verhaeltLachRasp    = lachenRasp / stathRasp

#Testausgabe von Breitenverhältnissen, um auf die Emotion zu schließen
if verhaeltBRasp > verhaeltBDB:
    print("Lächelt, da Raspberry(",verhaeltBRasp,") größer als Datenbank(",verhaeltBDB,") ist.")
elif verhaeltBRasp == verhaeltBDB:
    print("Neutral, da Raspberry(",verhaeltBRasp,") gleich Datenbank(",verhaeltBDB,") ist.") 
else:
    print("Traurig, da Raspberry(",verhaeltBRasp,") kleiner als Datenbank(",verhaeltBDB,") ist.")

#Testausgabe von Höhenverhältnissen, um auf die Emotion zu schließen
#if verhaeltHRasp > verhaeltHDB:
#   print("Lächelt, da Raspberry(",verhaeltHRasp,") größer als Datenbank(",verhaeltHDB,") ist.")
#elif verhaeltHRasp == verhaeltHDB:
#    print("Neutral, da Raspberry(",verhaeltHRasp,") gleich Datenbank(",verhaeltHDB,") ist.") 
#else:
#    print("Traurig, da Raspberry(",verhaeltHRasp,") kleiner als Datenbank(",verhaeltHDB,") ist.")

#Testausgabe von Mundverhältnissen, um auf ein Lachen zu schließen
if verhaeltBRasp > verhaeltBDB and verhaeltLachRasp > verhaeltLachDB:
    print("Lächelt mit Mund offen, da Raspberry(",verhaeltLachRasp,") größer als Datenbank(",verhaeltLachDB,") ist.")
else:
    print("Traurig, da Raspberry(",verhaeltLachRasp,") kleiner als Datenbank(",verhaeltLachDB,") ist.")

###Testausgabe von Landmarks und bestimmten Mundkoordinaten
##print(xs1[48], xs1[54])
##print(xs2[48], xs2[54])
##print(lm1)
##print(lm2)
##print(xs1[27], xs1[30], ys1[27], ys1[30], ys1[48], ys1[54])
    