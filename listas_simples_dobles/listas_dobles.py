class nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

class lista_doble:
    def __init__(self):
        self.cabeza=None
        self.cola=None
    def append(self,dato):
        nuevo=nodo(dato)
        if self.cabeza==None:
            self.cabeza=nuevo
            self.cola=nuevo
        else:
            self.cola.siguiente=nuevo
            nuevo.anterior=self.cola
            self.cola=nuevo
    def forward(self):
        actual=self.cabeza
        while actual:
            print(actual.dato)
            actual=actual.siguiente

milista=lista_doble()
milista.append(100)
milista.append(120)
milista.append(80)
milista.append(9)
milista.forward()

