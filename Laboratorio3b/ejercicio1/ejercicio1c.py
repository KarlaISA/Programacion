#Karla Ivonne Serrano Arevalo
#Ejerercicio 1.c
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np
import math

x=np.linspace(-1,5,80)
y=x*math.e**(-2*x)
plt.plot(x,y,linewidth=8, color='b')
plt.legend()
plt.title('Laboratorio 3b ejercicio 1c')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid(True)
plt.show()
