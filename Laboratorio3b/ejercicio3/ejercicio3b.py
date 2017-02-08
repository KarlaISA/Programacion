#Karla Ivonne Serrano Arevalo
#Ejerercicio 3.b
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np
import math

x=np.linspace(-2*math.pi,2*math.pi,80)
y=x+2*np.sin(2*x)
z=x+2*np.cos(5*x)
plt.plot(x,y,linewidth=2, color='y',label='x=t+2sen(2t)')
plt.plot(x,z,linewidth=3, color='g',label='y=t+2cos(5t)')
plt.legend()
plt.title('Laboratorio 3b ejercicio 3b')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid(True)
plt.show()
