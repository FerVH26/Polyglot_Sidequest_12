
from classes import item
from classes import modes,mesh



def obtenerDatos(j,n,mode,item_list:item,lista):
    for i in range(0,n):
        if mode is modes.INT_FLOAT.value:
            e=lista[j+i][0]
            r=lista[j+i][1]
            item_list[i].setIntFloat(e,r)
        else:
            e1=lista[j+i][0]
            e2=lista[j+i][1]
            e3=lista[j+i][2]
            item_list[i].setIntIntInt(e1,e2,e3)

def leerMallayCondiciones(m:mesh):
    filename=input("ingrese el nombre del archivo que contiene los datos de la malla: ")
    datos = []
    with open(filename) as fname:
	    lineas = fname.readlines()
	    for linea in lineas:
		    datos.append(linea.strip('\n'))

    lista = []
    for i in range(0,len(datos)):
        sp=datos[i].split()
        lista.append(sp)
    for i in range(0,4):
        lista.remove([])

    l=float(lista[0][0])
    k=float(lista[0][1])
    q=float(lista[0][2])

    nnodes=int(lista[1][0])
    neltos=int(lista[1][1])
    ndirich=int(lista[1][2])
    nneu=int(lista[1][3])
    
    m.setParameters(l,k,q)
    m.setSizes(nnodes,neltos,ndirich,nneu)

    m.createData()

    obtenerDatos(3,nnodes,modes.INT_FLOAT.value,m.getNodes())
    obtenerDatos(3+2+nnodes,neltos,modes.INT_INT_INT.value,m.getElements())
    obtenerDatos(5+nnodes+neltos+2,ndirich,modes.INT_FLOAT.value,m.getDirichlet())
    obtenerDatos(7+2+nnodes+neltos+ndirich,nneu,modes.INT_FLOAT.value,m.getNeumann())

