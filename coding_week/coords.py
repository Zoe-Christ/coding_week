import face_recognition as fr

standard = fr.load_image_file("/Users/mauricegeisen/Documents/coding_week/coding_week/trump_2.jpg")
lm1 = fr.face_landmarks(standard)

flex = fr.load_image_file("/Users/mauricegeisen/Documents/coding_week/coding_week/trump_1.jpg")
lm2 = fr.face_landmarks(flex)

xs1 = []
ys1 = []

xs2 = []
ys2 = []

for landmark1 in lm1:
    for k, v in lm1.items():
      xs1 += [x[0] for x in v]
      ys1 += [x[1] for x in v]

for landmark2 in lm2:
    for k, v in lm2.items():
        xs2 += [x[0] for x in v]
        ys2 += [x[1] for x in v]

durchschnitt    = xs1[55]-xs1[49]
varWert         = xs2[55]-xs2[49]

print("Standard:", durchschnitt)
print("Variable:", varWert)

if varWert>durchschnitt:
    print("Lächeln")
else:
    print("Traurig")
    