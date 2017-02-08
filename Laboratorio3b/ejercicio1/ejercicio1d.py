#Karla Ivonne Serrano Arevalo
#Ejerercicio 1.d
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np
import math

x=np.linspace(0,24,100)
y=math.e**(-1*x)
plt.plot(x,y,linewidth=2, color='g')
plt.legend()
plt.title('Laboratorio 3b ejercicio 1d')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid(True)
plt.show()
