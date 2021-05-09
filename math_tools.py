import math

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

def zeroesV(Vector,n):
    for i in range(0,n):
        Vector.append(0)

def copyMatrix(MatrixA,MatrixC):

    zeroesM(MatrixC, len(MatrixA))

    for i in range(0,len(MatrixA)):
        for j in range(0,len(MatrixA[0])):
            MatrixC[i][j]=MatrixA[i][j]

def productMatrixVector(MatrixA,VectorP,VectorR):
    
    for i in range(0,len(MatrixA)):
        cell = 0
        for j in range(0,len(VectorP)):
            cell+= MatrixA[i][j]*VectorP[j]
        VectorR[i] += cell

def productRealMatrix(real,MatrixM,MatrixR):
    zeroesM(MatrixR, len(MatrixM))

    for i in  range(0,len(MatrixM)):
        for j in range(0,len(MatrixM[0])):
            MatrixR[i][j]=real*MatrixM[i][j]

def getMinor(MatrixM,i,j):
    #eliminar fila
    MatrixM[i].clear()
    MatrixM.pop(i)
    #eliminar columna
    for c in range(0,len(MatrixM)):
        MatrixM[c].pop(j)


def determinant(MatrixM):
    if(len(MatrixM)==1):
        return MatrixM[0][0]
    else:
        det=0
        for i in range(0,len(MatrixM[0])):
            minor = []
            copyMatrix(MatrixM, minor)
            getMinor(minor, 0, i)

            det += (-1**i)*MatrixM[0][i]*determinant(minor)

        return det

def cofactors(MatrixM,MatrixCof):
    zeroesM(MatrixCof, len(MatrixM))

    for i in range(o,len(MatrixM)):
        for j in range(0,len(MatrixM[0])):
            minor=[]

            copyMatrix(MatrixM, minor)
            getMinor(minor, i, j)

            MatrixCof[i][j] = (-1**(i+j))*determinant(minor)

def transpose(MatrixM,MatrixT):
    zeroesM(MatrixT, len(MatrixM))
    for i in range(0,len(MatrixM)):
        for j in range(0,len(MatrixM[0])):
            MatrixT[j][i]=MatrixM[i][j]


def inverseMatrix(MatrixM,MatrixInv):
    cof = []
    adj = []

    det = determinant(MatrixM)
    if(det==0):
        exit(EXIT_FAILURE)
    cofactors(MatrixM, cof)
    transpose(cof, adj)
    productRealMatrix(1/det, adj, MatrixInv)

