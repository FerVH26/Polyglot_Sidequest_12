from enum import Enum
class sizes(Enum):
    NODES=0
    ELEMENTS=1
    DIRICHLET=2
    NEUMANN=3

vector = []
matriz = []

def row(tam,value):
    v=[]
    for i in range(0,tam):
        v.append(value)
    return v

#Funcion para crear la matriz de 0
def zeroesM(Matrix,n):
    for i in range(0,n):
        Matrix.append(row(n, 0))

def getMinor(MatrixM,i,j):
    #eliminar fila
    MatrixM[i].clear()
    MatrixM.pop(i)
    #eliminar columna
    for c in range(0,len(MatrixM)):
        MatrixM[c].pop(j)

zeroesM(matriz, 3)
getMinor(matriz, 1, 1)

for i in range(0,len(matriz[0])):
    print("[\t")
    for j in range(0,len(matriz)):
        print(matriz[i][j])
    print("]\t")

print(matriz)