#Karla Ivonne Serrano Arevalo
#Ejerercicio 2.b
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np
import math

x=np.linspace(0,2,80)
y=x*math.e**(-3*x)
z=math.e**(-3*x)*(1-3*x)
plt.plot(x,y,linewidth=4, color='g',label='f(x)=x*exp(-3x)')
plt.plot(x,z,linewidth=2, color='b',label='g(x)=exp(-3x)(1-3x)')
plt.legend()
plt.title('Laboratorio 3b ejercicio 2b')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid(True)
plt.show()
