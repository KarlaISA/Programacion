#Karla Ivonne Serrano Arevalo
#Ejerercicio 5.c
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np
import math

t=np.linspace(0,2*math.pi,80)
r=2-2*np.sin(t)+np.sin(t)*(np.sqrt(np.absolute(np.cos(t))))/(np.sin(t)+1.4)
x=r*np.cos(t)
y=r*np.sin(t)
plt.plot(x,y,linewidth=5, color='r',label='Cora')
plt.legend()
plt.title('Laboratorio 3b ejercicio 5c')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.fill_between(x,y,color='b')
plt.axis('equal')
plt.axis('off')
plt.grid(True)
plt.show()
