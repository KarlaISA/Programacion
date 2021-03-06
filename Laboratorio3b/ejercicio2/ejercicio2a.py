#Karla Ivonne Serrano Arevalo
#Ejerercicio 2.a
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np
import math

x=np.linspace(0,4*math.pi,100)
y=np.cos(2*x)+np.sin(3*x)
z=-2*np.sin(2*x)+3*np.cos(3*x)
plt.plot(x,y,linewidth=5, color='g',label='s(x)=cos(2x)+sen(3x)')
plt.plot(x,z,linewidth=2, color='r',label='v(x)=-2sen(2x)+3cos(3x)')
plt.legend()
plt.title('Laboratorio 3b ejercicio 2a')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid(True)
plt.show()
