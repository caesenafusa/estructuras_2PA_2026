from vehiculo import vehiculo
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

class lista:
    def __init__(self):
        self.primero=None
            
    def adicionar(self,dato):
        nuevo=Nodo(dato)
        if self.primero==None:
            self.primero=nuevo
            nuevo.siguiente=self.primero            
        else:
           actual=self.primero
           while actual.siguiente !=self.primero:
               actual=actual.siguiente
           actual.siguiente=nuevo
           nuevo.siguiente=self.primero
    
    def mostrar(self,repeticiones=10):
        actual=self.primero
        cont=0
        while actual and cont<repeticiones:
            print(actual.dato.mostrar_carga(),end='-')
            actual=actual.siguiente      
            cont+=1

v1=vehiculo("moto")
v2=vehiculo("lancha")
v3=vehiculo("bicicleta")
v4=vehiculo("tractomula")

milista=lista()
milista.adicionar(v1)
milista.adicionar(v2)
milista.adicionar(v4)
milista.adicionar(v3)
milista.mostrar()

v4.__st