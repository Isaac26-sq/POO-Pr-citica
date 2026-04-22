 # MAP = Recibir una lista, donde le vamos aplicar diferente operaciones 
 # matemáticas o de texto a todo los elementos por igual usando un lambda y 
 # este te devuelve una lista nueva con los elementos transformado . 

valores = [3, 4 , 4 , 10]

dobles = list(map(lambda num: num * 2, valores))

print(dobles)


resta = list(map(lambda n1: n1 - 4, valores))

print(resta)


nombres = ["juan", "ana", "pedro", "luisa"]

Mayuscula = list(map(lambda nom: nom.upper(), nombres))

print(Mayuscula)