from classes import mesh,sizes,parameters,element,condition
from math_tools import inverseMatrix, productMatrixVector


def showMatrix(matrix):
    for i in range(0,len(matrix[0])):
        print("[\t")
    for j in range(0,len(matrix)):
        print(matrix[i][j])
    print("]\t")

def showKs(Ks):
    for i in range(0,len(Ks)):
        print("K del elemento "+str(i+1)+":\n")
        showMatrix(Ks[i])
        print("*************************************\n")

def showVector(b):
    print("[\t")
    for i in range(0,len(b)):
        print(b[i])
    print("]\n")

def showBs(Bs):
    for i in range(0,len(Bs)):
        print("b del elemento "+str(i+1)+":\n")
        showVector(Bs[i])
        print("*************************************\n")

def createLocalK(element,m:mesh):
    K=[]
    row1=[]
    row2=[]

    k=m.getParameter(parameters.THERMAL_CONDUCTIVITY.value)
    l=m.getParameter(parameters.ELEMENT_LENGHT.value)

    row1.append(k/l)
    row1.append(-k/l)

    row2.append(-k/l)
    row2.append(k/l)

    K.append(row1)
    K.append(row2)

    return K

def createLocalb(element,m:mesh):
    b=[]

    Q=m.getParameter(parameters.HEAT_SOURCE.value)
    l=m.getParameter(parameters.ELEMENT_LENGHT.value)

    b.append(Q*(l/2))
    b.append(Q*(l/2))

    return b

def crearSistemasLocales(m:mesh,localKs,localbs):
    for i in range(0,m.getSize(sizes.ELEMENTS.value)):
        localKs.append(createLocalK(i, m))
        localbs.append(createLocalb(i, m))

def assemblyK(e:element,localK,K):
    index1 = e.getNode1()-1
    index2 = e.getNode2()-1

    K[index1][index1]+=localK[0][0]
    K[index1][index2]+=localK[0][1]
    K[index2][index1]+=localK[1][0]
    K[index2][index2]+=localK[1][1]

def assemblyb(e:element,localb,b):
    index1=e.getNode1()-1
    index2=e.getNode2()-1

    b[index1]+=localb[0]
    b[index2]+=localb[1]

def ensamblaje(m:mesh,localKs,localbs,K,b):
    for i in range(0,m.getSize(sizes.ELEMENTS.value)):
        e:element=m.getElement(i)
        assemblyK(e, localKs[i], K)
        assemblyb(e, localbs[i], b)

def applyNeumann(m:mesh,b):
    for i in range(0,m.getSize(sizes.NEUMANN.value)):
        c:condition = m.getCondition(i,sizes.NEUMANN.value)

        b[c.getNode1()-1]+=c.getValue()

def applyDirichlet(m:mesh,K,b):
    for i in range(0,m.getSize(sizes.DIRICHLET.value)):
        c:condition = m.getCondition(i, sizes.DIRICHLET.value)
        index = c.getNode1()-1
##eliminando la fila
        K[index].clear()
        K.pop(index)
##eliminando del vector
        b.pop(index)

        for row in range(0,len(K)):
            cell=K[row][index]
            for c in range(0,len(K)):
                K[c].pop(index)
            
            b[row]+= -1*c.getValue()*cell

def calculate(K,b,T):

    Kinv=[]
    inverseMatrix(K, Kinv)
    productMatrixVector(Kinv, b, T)