python

class Player:


    def __init__(self, name):
        self.name =name
        self.via = 1

        self.armadura = 0
        self.escudo = 0
        self.voluntad = 0

        self.nivel = 0
        self.experiencia = 0 


    def speak(self):
        print(f"Hola, me llamo {self.name}")

    def check_vida(self):
        print(f"La vida actual es {self.vida}")

    def check_armadura(self):
        print(f"La vida actual es {self.vida}")

    def check_escudo(self):
        print(f"La vida actual es {self.vida}")

    def check_voluntad(self):
        print(f"La vida actual es {self.vida}")

    def check_nivel(self):
        print(f"La vida actual es {self.vida}")

    def check_xp(self):
        print(f"La vida actual es {self.vida}")

    def check_inventario(self):
        if self.inventario == {}:
            print(f"El inventario esta vacio :(")
        else:
            for objeto, cantidad in self.inventario.items():
                


  # Ahora creamos a un jugarod, designando una variable

  player_1 = Player("Pablo")
  player_1.speak()

  # El () es para llamar funciones
  # Para acceder a los atributos del objeto lo hago sin ()

  player_1 = Player()
  player_2 = Player()
  Player_3 = Player()
