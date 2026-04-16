""""
import time 

def calcular_tiempo(funcion):

    def funcion_modificada(n):
        inicio = time.time()
        funcion(n)
        final = time.time()
        print(f"Su tiempo final es de: {final - inicio} segundos")
    return funcion_modificada
 


@calcular_tiempo
def imprimir_numeros(n):
    for i in range(n):
        print(i)
    
@calcular_tiempo
def resta(a):
    return a - 100

imprimir_numeros(100)
resta(2000)
"""""

"""
-- DECORADOR -- >  Modifcar una función ya existente

a(b) -> c         la funcion a recibe como argumento la funcion b (La cual vamos a decorar) y como resultado tendremos 
                  a la funcion c (La cual es la que va a decorar nuestro argumento (funcion b))

def fun_a(fun_b):
   
   def fun_c()
   print("Antes de la ejecucion")
   fun_b()
   print("Despues de la ejecucion")

   return fun_c

"""

def func_a(fun_b): # fun_b = saludar()
    
    def fun_c(*args, **kwargs):
        
        return fun_b(*args, **kwargs)
       

    return fun_c


@func_a
def suma(a, b):
    return a + b
print(suma(10, 30))

@func_a
def resta(a, b):
    return a - b
print(resta(50, 20))