#  Copyright (c) 2023. José Manuel Abelleira López.
#
import numpy as np

a = np.random.randint(1, 11, size=(3, 4))
suma = np.sum(a)
promedio = np.mean(a)
maximo = np.max(a)
minimo = np.min(a)
columnas = np.apply_along_axis(sum, 0, a)

print('La matriz original es:\n', a)
print('Las sumas de las columnas son: ', columnas)
print('La suma de todos los elementos de la matriz es: ', suma)
print('El promedio de todos los elementos de la matriz es: ', promedio)
print('El máximo de todos los elementos de la matriz es: ', maximo)
print('El mínimo de todos los elementos de la matriz es: ', minimo)

