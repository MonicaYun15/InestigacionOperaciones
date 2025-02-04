import itertools
import matplotlib.pyplot as plt
from collections import defaultdict


dado = range(1, 21) #cARAS DEL DADO 
espacio_muestral = list(itertools.product(dado, repeat=3))  

# variable aleatoria
X = [sum(resultado) for resultado in espacio_muestral]

frecuencia_X = defaultdict(int)
for valor in X:
    frecuencia_X[valor] += 1

# Grafico
print("Valor de X | Frecuencia")
print("-----------------------")
for valor in sorted(frecuencia_X.keys()):
    print(f"{valor:^10} | {frecuencia_X[valor]:^9}")

# Paso 5: Graficar la distribución de X
plt.bar(frecuencia_X.keys(), frecuencia_X.values(), color='blue')
plt.xlabel('Valor de X (Suma de los dados)')
plt.ylabel('Frecuencia')
plt.title('Distribución de la variable aleatoria X')
plt.show()