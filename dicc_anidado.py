# Como importar un diccionario a un backup 


import json 
Perfil = {
    "Estudiante" : {
        "Nombre":"Jose Caizedo",
        "Genero":"Masculino",
        "edad":"34",
        "Serie_Fav":"Malcolm in the middle",
    },
    "Estudiante1":{
        "Nombre":"Elian",
        "Genero":"Masculino",
        "edad":"20",
        "Serie_Fav":"The Chosen",
    }
}


for key, value in Perfil.items():
    print(f"{key} :")
    for i, j in value.items():
        print(f"{i} : {j}")



with open("Perfil.json", "w") as archivo: 
    json.dump(Perfil, archivo, indent=4) # indent=4 : 

print("Archivo Creado!!")