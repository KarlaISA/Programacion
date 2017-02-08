#Karla Ivonne Serrano Arevalo
#Ejerercicio 1
#25 noviembre 2016

from PIL import Image, ImageDraw
import random
import math
 
def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
 
def midPointAdjust(p1, p2, r, size):
    return ( int((p1[0] + p2[0])/r) + size[0]//6 , int((p1[1] + p2[1])/r) + size[1]//6 )
 
def midPoint(p1, p2, r, size):
    return ( int((p1[0] + p2[0])/r), int((p1[1] + p2[1])/r))
 

n = 9
r = 3
base = 800
points = 1000000
 

white = (255, 255, 255)
color = (255, 0, 0)
 

if n == 3:
    size = base, int(3**.5 / 2 * base)
    redCorner = (size[0]//2, 5)
    blueCorner = (5, size[1]-5)
    greenCorner = (size[0]-5, size[1]-5)
    corners = (redCorner, blueCorner, greenCorner)
 
elif n >= 4:
 
    size = base, base
    radious = base
    angle = 2 * math.pi / n
    corners = [ ( int(size[0]//2 + radious * math.sin(i * angle)), int(size[1]//2 + radious * math.cos(i * angle)) ) for i in range(n) ]
 

polygonImg = Image.new('RGB', size, (0,0,0))
draw = ImageDraw.Draw(polygonImg)
 

current = corners[ random.randint(0,len(corners)-1) ]
for i in range(points):
    randCorner = corners[ random.randint(0,len(corners)-1) ]
    if n == 3:
        current = midPoint(current, randCorner, r, size)
    else:
        current = midPointAdjust(current, randCorner, r, size)
    draw.point(current, color)
 
polygonImg.show()
#polygonImg.save("fractal.png")
