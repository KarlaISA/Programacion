#Karla Ivonne Serrano Arevalo
#Ejerercicio 7
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np
import math

t=np.linspace(0,4*math.pi,100)
r=105+100*np.sin(4.5*t)
l=t-(np.cos(10*t)/10)
x=320+r*np.cos(l)
y=-240-r*np.sin(l)
plt.plot(x,y,linewidth=7, color='y',label='x=320+rcos(l) y y=-240-rsen(l)')
plt.legend()
plt.title('Laboratorio 3b ejercicio 7')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.fill_between(x,y,color='g')
plt.axis('equal')
plt.axis('off')
plt.grid(True)
plt.show()
