from raspCam import raspCam
from camera import *

cam = raspCam()
#print(cam.recognize())
s = cam.recognize()
t = cam.sadOrHappy(s)
print(s.name, t)
cam.deletePic()