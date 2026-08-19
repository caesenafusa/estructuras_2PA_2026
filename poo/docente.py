from persona import persona
class docente(persona):
    def __init__(self, nombre, documento,asignatura):
        super().__init__(nombre, documento)
        self.asignatura=asignatura
