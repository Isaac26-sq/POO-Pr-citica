import time 

def funcion(*args):  # Con *args podre guardar todos los argumentos que quiera pero dentro de una tupla 
    print (args)

funcion("hola", "hola", "hola" , 12, "hola")

def funcion(*args):  # Con *args podre guardar todos los argumentos que quiera, con el for hago que no lo muestre 
                     # como una tupla
    for i in args:
        print(i)

funcion("hola", "hola", "hola" , 12, "hola")



def total(*args):
    total = sum(args)
    print(f"Su total es de: {total}")

total(100, 200, 300, 400)


for i in range(10):
    print(i)


    

    