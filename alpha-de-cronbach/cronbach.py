# Estudiante: Jorge Luis Jácome Domínguez
# Librerias
import sys
import math
import pandas

# Cargar datos
df = pandas.read_csv(sys.argv[1], delimiter=';')
#df = pandas.read_csv("cronbach.csv", delimiter=';')

# Variables
output = 0.0 # Resultado
var_K = 0 # Número de items
var_sumVarianzasI = 0 # Varianza del item i
var_VarianzaTotal = 0 # Varianza total de los items

# Variables de apoyo
aryCols = df.columns
numCols = len(aryCols)

# Número de items = Total de columnas menos la columna participante y score
var_K = numCols - 2

# Recorrer columnas desde [ , segunda, ..., penultima, ] para calcular suma de la varianza de los items
for i in range(1, numCols - 1):
    nomCol = aryCols[i]
    aryValsItem = df[nomCol].array
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
    # Sumar el calculo de la varianza del item i
    var_sumVarianzasI += sumDiferencia/numValsItem

# Recorrer los valores del último item "SCORE o suma" y calcular la varianza total
nomCol = aryCols[numCols - 1]
aryValsItem = df[nomCol].array
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
# Sumar el calculo de la varianza del item i
var_VarianzaTotal = sumDiferencia/numValsItem

# Calcular Alfa de Cronbach
output = (var_K / (var_K - 1)) * (1 - (var_sumVarianzasI / var_VarianzaTotal))

# CODE HERE
print(round(output, 3))