#Karla Ivonne Serrano Arevalo
#Ejerercicio 1.b
#Diciembre 2016

import matplotlib.pyplot as plt 
import numpy as np

x=np.linspace(-1,5,100)
y=2*x**2-8*x-11
plt.plot(x,y,linewidth=5, color='r')
plt.legend()
plt.title('Laboratorio 3b ejercicio 1b')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.grid(True)
plt.show()
