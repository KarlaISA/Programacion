#Karla Ivonne Serrano Arevalo
#Ejerercicio 3.c
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np
import math

x=np.linspace(0,2*math.pi,80)
y=np.sin(3*x)
z=np.sin(4*x)
plt.plot(x,y,linewidth=7, color='b',label='x=sen(3t)')
plt.plot(x,z,linewidth=1, color='g',label='y=sen(4t)')
plt.legend()
plt.title('Laboratorio 3b ejercicio 3c')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid(True)
plt.show()
