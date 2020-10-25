# Estudiante: Jorge Luis Jácome Domínguez
# Librerias
import sys
import math
import pandas

# Cargar datos
df_dificultad = pandas.read_csv(sys.argv[1], delimiter=';')
df_scores = pandas.read_csv(sys.argv[2], delimiter=';')

#df_dificultad = pandas.read_csv("equivalenciaracional_dificultad.csv", delimiter=';')
#df_scores = pandas.read_csv("equivalenciaracional_scores.csv", delimiter=';')

# Variables
output = 0.0 # Resultado
var_K = 0 # Número de items
var_VarianzaTotal = 0 # Varianza total de los items
var_sumDificultadI = 0 # Suma de dificultad del item i

# SCORES
# Variables de apoyo
aryCols = df_scores.columns
numCols = len(aryCols)

# Recorrer los valores del último item "SCORE" y calcular la varianza total
nomCol = aryCols[numCols - 1]
aryValsItem = df_scores[nomCol].array
numValsItem = len(aryValsItem)
sumValsItem = 0
# Recorrer los valores del items i
for x in range(numValsItem):
    valItem = aryValsItem[x]
    sumValsItem += valItem
# Calcular promedio
promValsItem = sumValsItem/numValsItem
sumDiferencia = 0
# Recorrer los valores del items i
for x in range(numValsItem):
    valItem = aryValsItem[x]
    # Suma del cuadrado del "Valor i menos el promedio de Valores"
    sumDiferencia += math.pow(valItem - promValsItem, 2)
# Sumar el calculo de la varianza del item i  # Se usa la versión para una muestra que resta 1 al tamaño
var_VarianzaTotal = sumDiferencia/(numValsItem - 1)

# DIFICULTAD
# Variables de apoyo
aryCols = df_dificultad.columns
numCols = len(aryCols)
# Recorrer los valores del último item "P" y calcular la dificultad total
nomCol = aryCols[numCols - 1]
aryValsItem = df_dificultad[nomCol].array
numValsItem = len(aryValsItem)
# Recorrer los valores del items i
for x in range(numValsItem):
    valItem = aryValsItem[x]
    var_sumDificultadI += (valItem * (1 - valItem))

# Número de items = Total de columnas menos la columna participante y score
var_K = len(df_dificultad[aryCols[0]].array)

# Calcular Equivalencia racional
output = (var_K / (var_K - 1)) * (1 - (var_sumDificultadI / var_VarianzaTotal))

# CODE HERE
print(round(output, 3))