import time 
def contador_numeros(funcion):
  
    def wapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        print(f"Su tiempo final es de: {time.time() - inicio:4f} s")
        return resultado
    return wapper

@contador_numeros
def numeros(n):
    for i in range(n):
        print(i)
numeros(600)


@contador_numeros
def suma(n1, n2):
    return n1 + n2
    
print(suma(10, 30))