#Karla Ivonne Serrano Arevalo
#Ejerercicio 2.d
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np
import math

x=np.linspace(0,2*math.pi,80)
y=(1+2*np.sin(x))*np.cos(x)
z=(1+2*np.sin(x))*np.sin(x)
plt.plot(x,y,linewidth=4, color='y',label='x(t)=(1+2sen(t))cos(t)')
plt.plot(x,z,linewidth=2, color='b',label='y(t)=(1+2sen(t))sen(t)')
plt.legend()
plt.title('Laboratorio 3b ejercicio 2d')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid(True)
plt.show()
