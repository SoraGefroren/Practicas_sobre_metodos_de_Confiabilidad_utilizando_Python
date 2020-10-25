# Estudiante: Jorge Luis Jácome Domínguez
# Librerias
import sys
import math
import pandas

# Cargar datos
df = pandas.read_csv(sys.argv[1], delimiter=';')
#df = pandas.read_csv("splithalf.csv", delimiter=';')

# Variables
output = 0.0 # Resultado
var_N = 0 # Número total de observaciones (participantes)
# Variables para sumas totales
var_SumTotal_XY = 0
var_SumTotal_X = 0
var_SumTotal_Y = 0
var_SumTotal_X2 = 0
var_SumTotal_Y2 = 0

# Variables de apoyo
aryCols = df.columns
numCols = len(aryCols)

# Número observaciones (participantes)
var_N = len(df[aryCols[0]].array)

# Recorrer - NONES y PARES
nomCol_X = aryCols[numCols - 2]
nomCol_Y = aryCols[numCols - 1]
aryVals_X = df[nomCol_X].array
aryVals_Y = df[nomCol_Y].array
numVals_X = len(aryVals_X)
numVals_Y = len(aryVals_Y)
# Validar número de observaciones
if (numVals_X == numVals_Y):
    # Recorrer los valores del items i
    for i in range(numVals_X):
        val_X = aryVals_X[i]
        val_Y = aryVals_Y[i]
        # Sumar totales
        var_SumTotal_XY += (val_X * val_Y)
        var_SumTotal_X += val_X
        var_SumTotal_Y += val_Y
        var_SumTotal_X2 += math.pow(val_X, 2)
        var_SumTotal_Y2 += math.pow(val_Y, 2)

# Calcular fiabiliodad de dos mitades
output = ((var_N * var_SumTotal_XY) - (var_SumTotal_X * var_SumTotal_Y)) / math.sqrt( ((var_N * var_SumTotal_X2) - math.pow(var_SumTotal_X, 2)) * ((var_N * var_SumTotal_Y2) - math.pow(var_SumTotal_Y, 2)) )
output = (2 * output) / (1 + output)

# CODE HERE
print(round(output, 3))