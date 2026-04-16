""""
# Forma tradicional sin usar kwargs.
def empleado(nombre, puesto, lenguaje):
    print(nombre)
    print(puesto)
    print(lenguaje)

empleado("Jose", "Supervisor", "python")
"""""
# Usando kwargs 

def empleados(**kwargs):

    for key, Value in kwargs.items(): # toma todo los argumentos que se entregan dentro de la funcion (key : value)
        print(f" {key} : {Value}")

empleados(nombre="Jose", puesto="Programador", lenguaje="JS")
        #   key   valor 


