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

print(Perfil["Estudiante1"]["Nombre"] + "\n" + Perfil["Estudiante1"]["Genero"])


with open("Perfil.json", "w") as archivo: 
    json.dump(Perfil, archivo)

print("estoy dentro!!")