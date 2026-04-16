
#Clase constructora
class Personaje:
    #  inicialización
    def __init__(self, nombre, clase, nivel, salud, mana):
        # Atributos de instancia
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.salud = salud
        self.mana = mana
    
    # Métodos
    def atacar(self, objetivo):
        return f"{self.nombre} ataca a {objetivo}!"
    
    def curar(self, cantidad):
        self.salud += cantidad
        return f"{self.nombre} se cura {cantidad} puntos de salud."
    
    def restaurar_mana(self, cantidad):
        self.mana += cantidad
        return f"{self.nombre} aumento su mana un {cantidad}"
    
    def subir_nivel(self, cantidad ):
        self.nivel += cantidad 
        return f"{self.nombre} subió {cantidad} niveles! Ahora es nivel {self.nivel} "
 
Heroe = Personaje("Carlos", "Guardia", 30, 100, 40)
print(Heroe.atacar("Dragón"))
print(Heroe.curar(30))
print(Heroe.restaurar_mana(30))
print(Heroe.subir_nivel(30))
print("")




class Agente:
    def __init__(self, nombre, rol, habilidad, genero, creditos, vida):
        self.nombre = nombre
        self.rol = rol
        self.habilidad = habilidad
        self.genero = genero
        self.creditos = creditos
        self.vida = vida
        
    def atacar(self, enemigo):
        self.creditos += 300
        return f"{self.nombre} eliminó a {enemigo}! Ha obtenido {self.creditos} creditos"
    def curar(self, cantidad):
        self.vida += cantidad
        return f"{self.nombre} se cura {cantidad} puntos de salud! Vida actual: {self.vida}"
    def vandal(self, daño):
        self.vida -= daño
        if daño >= 150: 
            return f"{self.nombre} ha sido eliminado!!!"
        else:
            return f"{self.nombre} a recibido {daño} de daño por una vandal. Vida restante: {self.vida}" 
    
     
Personaje1 = Agente("Reyna", "Dualista", "Emperatriz", "Femenino", 3900, 100)
Personaje2 = Agente("Jett", "Dualista", "Tormenta de cuchillas", "Femenino", 3900, 100)
print()
print("======    Valorant    ======")
print()
print(Personaje1.atacar("Viper"))
print(Personaje1.curar(50))
print(Personaje1.vandal(150))
print(Personaje2.vandal(160))
print(f"{Personaje1.nombre} tiene las habilidades de {Personaje1.habilidad} y su rol es: {Personaje1.rol} ")




# Encapsulamiento

class Caballero:
    def __init__(self, nombre, clase, nivel, salud, xp):
       # atribtos de la clase (encapsulados)
        self.__nombre = nombre
        self.__clase = clase
        self.__nivel = nivel 
        self.__salud = salud
        self.__xp = xp 
    
    def atacar(self, enemigo):
        return f"{self.__nombre} ataca a {enemigo}"
    
    def curar(self, cantidad):
        self.__salud += cantidad
        return f"{self.__nombre} se curo {cantidad} puntos de salud"
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_salud(self):
        return self.__salud
    
    def set_nivel(self, nuevo_nivel):
        self.__nivel = nuevo_nivel
    
pers1 = Caballero("Arthur", "Guardia", 20, 100, 1000 )

print(pers1.obtener_nombre())
print(pers1.obtener_salud())
print(pers1.set_nivel())