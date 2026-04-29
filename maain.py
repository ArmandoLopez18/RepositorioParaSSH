from funcion_n import suma, resta, multiplicacion
import os 
import matplotlib.pyplot as plt
import numpy as np
N_FOLDER= "ResultadosdeGraficasGIT"
os.makedirs(N_FOLDER,exist_ok = True)

x = np.linspace(0,10,100)
y = np.sin(x)
r1 = suma(4,4)
r2 = resta(10,5)
r3 = multiplicacion(20,2)
print("La suma resultante es:", r1)
print("La resta resultante es:", r2)
print("La multiplicacion resultante es:", r3)

plt.figure(1)
plt.plot(x, y, color = 'blue', label = 'y = sin(x)')
plt.title("Onda Senoidal")
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(N_FOLDER, "Graficaseno.eps"))

plt.figure(2)
plt.plot(x, np.cos(x), color='red', label = 'y2 = cos(x)')
plt.title("Onda Cosenoidal")
plt.grid(True)
plt.savefig(os.path.join(N_FOLDER, "Graficacoseno.eps"))
plt.show()
