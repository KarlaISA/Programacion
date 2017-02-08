#Karla Ivonne Serrano Arevalo
#Ejerercicio 3.a
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np
import math

x=np.linspace(0,2*math.pi,120)
y=np.cos(x)**3
z=np.sin(x)**3
plt.plot(x,y,linewidth=3, color='g',label='x=cos(t)^3')
plt.plot(x,z,linewidth=7, color='r',label='y=sen(t)^3')
plt.legend()
plt.title('Laboratorio 3b ejercicio 3a')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid(True)
plt.show()
