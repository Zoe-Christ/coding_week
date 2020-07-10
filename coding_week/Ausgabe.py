"""import datenbank

#Beispielanwendung der Datenbank Funktionen 

datenbank.ausgeben()

datenbank.insert(4, 'Schierding', 'Jonah')"""

#datenbank.delete(3)

"""
import io

with io.BytesIO() as output:
    from PIL import Image
    with Image.open("michelle-obama.jpg") as img:
        img.convert('RGB').save(output, 'BMP')
    data=output.getvalue()[14:]
    print(data)
"""


import io
from io import BytesIO
from PIL import Image

with Image.open("michelle-obama.jpg") as img:
    byteIO = io.BytesIO()
    img.save(byteIO, format='PNG')
byteArr = byteIO.getvalue()
print(byteArr)
img = Image.open(io.BytesIO(byteArr))
img.show()


