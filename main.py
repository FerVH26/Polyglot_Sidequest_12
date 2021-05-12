

from types import new_class
from math_tools import zeroesM, zeroesV
from tools import leerMallayCondiciones
from classes import mesh, sizes
from sel import applyDirichlet, calculate, crearSistemasLocales, ensamblaje,applyNeumann, showVector



localKs=[]
localbs=[]

k=[]
b=[]
t=[]

m:mesh=new_class

leerMallayCondiciones(m)
crearSistemasLocales(m,localKs,localbs)

zeroesM(k,m.getSize(sizes.NODES.value))
zeroesM(b,m.getSize(sizes.NODES.value))

ensamblaje(m,localKs,localbs,k,b)

applyNeumann(m,b)

applyDirichlet(m,k,b)

zeroesV(t,len(b))

calculate(k,b,t)

print("la respuesta es: ")
showVector(t)