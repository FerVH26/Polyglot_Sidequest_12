def getMinor(MatrixM,i,j):
    #eliminar fila
    MatrixM[i].clear()
    MatrixM.pop(i)
    #eliminar columna
    for c in range(0,len(MatrixM)):
        MatrixM[c].pop(j)