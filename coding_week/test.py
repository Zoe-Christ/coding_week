from raspCam import raspCam
from camera import *

cam = raspCam()
#print(cam.recognize())
s = cam.recognize()
print(s)