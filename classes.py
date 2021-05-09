from enum import Enum
from dataclasses import dataclass
class lines(Enum):
    NOLINE=0
    SINGLELINE=1
    DOUBLELINE=2
class modes(Enum):
    NOMODE=0
    INT_FLOAT=1
    INT_INT_INT=2
class parameters(Enum):
    ELEMENT_LENGHT=0
    THERMAL_CONDUCTIVITY=1
    HEAT_SOURCE=2
class sizes(Enum):
    NODES=0
    ELEMENTS=1
    DIRICHLET=2
    NEUMANN=3

@dataclass
class item:

    id:int
    x:float
    node1:int
    node2:int
    value:float

    def getId(self):
        return self.id
    def getX(self):
        return self.x
    def getNode1(self):
        return self.node1
    def getNode2(self):
        return self.node2
    def getValue(self):
        return self.value

@dataclass
class node(item):
    def setIntFloat(self,identifie:int,x_coordinate:float):
        self.id=identifie
        self.x=x_coordinate

@dataclass
class element(item):
    def setIntIntInt(self,identifier:int,firstnode:int,secondnode:int):
        self.id = identifier
        self.node1 = firstnode
        self.node2 = secondnode

@dataclass
class condition(item):
    def setIntFloat(self,node_to_apply,prescribed_value):
        self.node1=node_to_apply
        self.value=prescribed_value

@dataclass
class mesh:
    parameter:float
    size:int
    node_list:node
    element_list:element
    dirichlet_list:condition
    neumann_list:condition

    def setParameters(self,l:float,k:float,q:float):
        self.parameter[parameters.ELEMENT_LENGHT.value]=l
        self.parameter[parameters.THERMAL_CONDUCTIVITY.value]=k
        self.parameter[parameters.HEAT_SOURCE.value]=q

    def setSizes(self,nnodes:int,neltos:int,ndirich:int,nneu:int):
        self.size[sizes.NODES.value]=nnodes
        self.size[sizes.ELEMENTS.value]=neltos
        self.size[sizes.DIRICHLET.value]=ndirich
        self.size[sizes.NEUMANN.value]=nneu

    def getSize(self,s):
        return self.size[s]
    
    def getParameter(self,s):
        return self.parameter[s]

    def createData(self):
        self.node_list = []
        self.element_list=[]
        self.dirichlet_list=[]
        self.neumann_list=[]

    def getNodes(self):
        return self.node_list
    
    def getElements(self):
        self.element_list

    def getDirichlet(self):
        return self.dirichlet_list

    def getNeumann(self):
        return self.neumann_list

    def getNode(self,i):
        return self.element_list[i]

    def getElement(self,i):
        return self.element_list[i]

    def getCondition(self,i,type):
        if(type==sizes.DIRICHLET.value):
            return self.dirichlet_list[i]
        else:
            return self.neumann_list[i]