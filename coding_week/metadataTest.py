import face_recognition

derulo_image = face_recognition.load_image_file("/Users/mauricegeisen/Documents/coding_week/coding_week/ZoeH.jpeg")

try:
    derulo_face_encoding = face_recognition.face_encodings(derulo_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

print(derulo_face_encoding)