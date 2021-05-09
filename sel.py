from classes import mesh

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
        showVector(bs[i])
        print("*************************************\n")

def createLocalK(element,m:mesh):
    K=[]
    row1=[]
    row2=[]

    k=m.getParameter(THERMAL_CONDUCTIVITY)
    l=m.getParameter(ELEMENT_LENGHT)

    row1.append(k/l)
    row1.append(-k/l)

    row2.append(-k/l)
    row2.append(k/l)

    K.append(row1)
    K.append(row2)

    return K