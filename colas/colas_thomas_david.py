class nodo:
    def _init_(self,dato):
        self.dato=dato
        self.siguiente=None

class lista:
    def _init_(self):
        self.primero=None

    def append(self,dato): #encolar
        nuevo=nodo(dato)
        if self.primero==None:
            self.primero=nuevo
        else:
            actual=self.primero
            while actual.siguiente:
                actual=actual.siguiente
            actual.siguiente=nuevo
    def mostrar(self):
        actual=self.primero
        while actual:
            print(actual.dato)
            actual=actual.siguiente
    def desencolar(self): #desencolar
        if self.primero==None:
            print("La lista esta vacia")
        else:
            self.primero=self.primero.siguiente
            
#encolar


milista=lista()
milista.append(100)
milista.append(50)
milista.append(1000)
milista.append(25)
milista.mostrar()
milista.desencolar()

print("Despues de desencolar")
milista.append(67)
milista.mostrar()
milista.mostrar()