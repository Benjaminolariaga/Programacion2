caramelos=0
alumnos=0
resto=0
division=0

print("cuantos caramelos tiene  tu profesor")
caramelos=int(input())

print("en cuantos estudiantes los tiene que repartir")
alumnos=int(input())

resto=caramelos%alumnos
division=caramelos//alumnos

print("el profe le va a dar cada alumno: ",division," caramelos")
print("sobraron ",resto," caramelos en la bolsa")

