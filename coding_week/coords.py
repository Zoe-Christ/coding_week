#Importieren von Face-Recognition, MG
import face_recognition as fr

#Vergleichsbild von DB laden und anschließend Landmarks setzen
standard = fr.load_image_file("/Users/mauricegeisen/Documents/coding_week/coding_week/Maurice_.jpeg")
lm1 = fr.face_landmarks(standard)

#Aufgenommenes Bild von Raspberry Pi laden und anschließend Landmarks setzen
flex = fr.load_image_file("/Users/mauricegeisen/Documents/coding_week/coding_week/Maurice_oB.jpeg")
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

#Ermittlung der Breite des Mundes im Vergleichsbilds
breiteDB    = xs1[54]-xs1[48]

#Ermittlung der Breite des Mundes im Raspberry-Bilds
breiteRasp        = xs2[54]-xs2[48]

#Ermittlung der Höhe des Mundes im Vergleichsbilds
hoeheDB = ys1[54]- ys1[48]

#Ermittlung der Höhe des Mundes im Raspberry-Bilds
hoeheRasp = ys2[54] -ys2[48]

#Testausgabe der Werte der Breiten
print("Standard:", breiteDB)
print("Variable:", breiteRasp)

#Vergleich der Mundbreiten, um auf die Emotionslage zu schließen --> noch Test
#if breiteRasp>=breiteDB:
#    print("Lächeln")
#else:
#    print("Traurig")

#Vergleich der Mundhöhen, um auf die Emotionslage zu schließen --> noch Test
if hoeheRasp >= hoeheDB:
    print("Lächeln")
else:
    print("Normal")    
    
#Testausgabe von Landmarks und bestimmten Mundkoordinaten
#print(xs1[48], xs1[54])
#print(xs2[48], xs2[54])
#print(lm1)
#print(lm2)
    