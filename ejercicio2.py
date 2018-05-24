# Escriba el codigo necesario para que al ejecutar python ejercicio2.py
# se cree una grafica con una funcion sinusoidal entre 0 y 2pi.
import matplotlib
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x=np.linspace(0,2*pi,100)
y=np.sin(x)
plt.plot(x,y)
plt.show()
