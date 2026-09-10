class vehiculo:
    def __init__(self,nombre):
        self.nombre=nombre
        self.carga=100
    def cargar(self,combustile):
        return f"recargar {combustile}"
    def gastar(self,combustible):
        if self.carga>combustible:
            return "combustible insuficiente"
        else:
            self.carga-=combustible#x=x-10  ... x-=10
    def mostrar_carga(self):
        return f"{self.carga} {self.nombre}"        

    def __str__(self):
        return self.nombre


x=vehiculo("auto")
print(x)