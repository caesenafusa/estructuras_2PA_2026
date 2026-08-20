from recurso import recurso
from docente import docente

r1=recurso('video beam')
r2=recurso('portatiles')
r3=recurso('marcadores')

d1=docente('Maria Falki',123456,'quimica')
d1.solicitar_recurso(r1)
d1.solicitar_recurso(r2)
d1.solicitar_recurso(r3)

d1.recorrer_recursos()
d1.asignar_estudio("pregrado","ingenieria de sistemas")
d1.asignar_estudio("postgrado","inteligencia artificial")
print(d1.estudios)
del d1
