
calificaciones = [60, 40, 50, 55, 45, 70, 80]

estudiantes = list(filter(lambda notas: notas < 60, calificaciones))

bono = list(map(lambda notas: notas + 5, estudiantes ))

print(bono)


palabras = ["sol", "luna", "mar", "estrella", "luz", "planeta"]

tres = list(filter(lambda palabra: len(palabra) > 3 , palabras))

extras = list(map(lambda p: p + " | Aprobdo", tres))

print(extras)
    






