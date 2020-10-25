# Estudiante: Jorge Luis Jácome Domínguez
# Librerias
import sys
import math
import pandas

# Cargar datos
df = pandas.read_csv(sys.argv[1], delimiter=';')
# df = pandas.read_csv("kappa_data.csv", delimiter=';')

# Variables
output = 0.0 # Resultado
# Variables para sumas totales
var_N = 0
var_PO = 0
var_PE = 0
# Variables para categorias: bueno, regular y malo
var_Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Variables de apoyo
aryCols = df.columns
numCols = len(aryCols)

# Total de observaciones
var_N = len(df[aryCols[0]].array)

# Recorrer - NONES y PARES
aryVals_E1 = df[aryCols[numCols - 2]].array
aryVals_E2 = df[aryCols[numCols - 1]].array
# Recorrer los valores del items i
for i in range(var_N):
    val_itemE1 = aryVals_E1[i].lower()
    val_itemE2 = aryVals_E2[i].lower()
    # Validar valor de items
    if val_itemE1 == val_itemE2:
        if val_itemE1 == "bueno":
            var_Matriz[0][0] += 1
        elif val_itemE1 == "regular":
            var_Matriz[1][1] += 1
        elif val_itemE1 == "malo":
            var_Matriz[2][2] += 1
    else:
        if val_itemE1 == "bueno" and val_itemE2 == "regular":
            var_Matriz[0][1] += 1
        elif val_itemE1 == "bueno" and val_itemE2 == "malo":
            var_Matriz[0][2] += 1
        elif val_itemE1 == "regular" and val_itemE2 == "bueno":
            var_Matriz[1][0] += 1
        elif val_itemE1 == "regular" and val_itemE2 == "malo":
            var_Matriz[1][2] += 1
        elif val_itemE1 == "malo" and val_itemE2 == "bueno":
            var_Matriz[2][0] += 1
        elif val_itemE1 == "malo" and val_itemE2 == "regular":
            var_Matriz[2][1] += 1
# Calcular Suma de productos PE
var_sumF1_0a2 = var_Matriz[0][0] + var_Matriz[0][1] + var_Matriz[0][2]
var_sumF2_0a2 = var_Matriz[1][0] + var_Matriz[1][1] + var_Matriz[1][2]
var_sumF3_0a2 = var_Matriz[2][0] + var_Matriz[2][1] + var_Matriz[2][2]
var_sumC1_0a2 = var_Matriz[0][0] + var_Matriz[1][0] + var_Matriz[2][0]
var_sumC2_0a2 = var_Matriz[0][1] + var_Matriz[1][1] + var_Matriz[2][1]
var_sumC3_0a2 = var_Matriz[0][2] + var_Matriz[1][2] + var_Matriz[2][2]


# Calcular k de Cohen
var_PO = (var_Matriz[0][0] + var_Matriz[1][1] + var_Matriz[2][2]) / var_N
var_PE = ((var_sumF1_0a2 * var_sumC1_0a2) + (var_sumF2_0a2 * var_sumC2_0a2) + (var_sumF3_0a2 * var_sumC3_0a2)) / math.pow(var_N, 2)
output = (var_PO - var_PE) / (1 - var_PE)

# CODE HERE
print(round(output, 3))