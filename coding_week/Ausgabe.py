import datenbank

#Beispielanwendung der Datenbank Funktionen 

#datenbank.ausgeben()

#datenbank.insert(4, 'Schierding', 'Jonah')

#datenbank.delete(3)



import io
from io import BytesIO
from PIL import Image
with Image.open("jason-derulo.jpg") as img:
    byteIO = io.BytesIO()
    img.save(byteIO, format='PNG')
byteArr = byteIO.getvalue()
#print(byteArr)
#img = Image.open(io.BytesIO(byteArr))
#img.show()

datenbank.insert(2, byteArr)
#datenbank.ausgeben()

