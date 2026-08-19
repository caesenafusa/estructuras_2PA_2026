from persona import persona
class docente(persona):
    def __init__(self, nombre, documento,asignatura):
        super().__init__(nombre, documento)
        self.asignatura=asignatura
        self.lista_recursos=[]

    def solicitar_recurso(self,recurso):
        self.lista_recursos.append(recurso)

    def recorrer_recursos(self):
        for x in self.lista_recursos:
            print(x.get_recurso())