import face_recognition as fr

standard = fr.load_image_file("/Users/mauricegeisen/Documents/coding_week/coding_week/Maurice_.jpeg")
lm1 = fr.face_landmarks(standard)

flex = fr.load_image_file("/Users/mauricegeisen/Documents/coding_week/coding_week/Maurice_oB.jpeg")
lm2 = fr.face_landmarks(flex)

xs1 = []
ys1 = []

xs2 = []
ys2 = []

for landmark1 in lm1:
    for k, v in landmark1.items():
      xs1 += [x[0] for x in v]
      ys1 += [x[1] for x in v]

for landmark2 in lm2:
    for k, v in landmark2.items():
        xs2 += [x[0] for x in v]
        ys2 += [x[1] for x in v]

durchschnitt    = xs1[54]-xs1[48]
varWert         = xs2[54]-xs2[48]

print("Standard:", durchschnitt)
print("Variable:", varWert)

if varWert>durchschnitt:
    print("Lächeln")
else:
    print("Traurig")
    