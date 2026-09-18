class AgenteAspiradora:

    def __init__(self):
        self.posicion = "A"

        self.habitaciones = {
            "A": "Sucia",
            "B": "Sucia"
        }

    def percibir(self):
        return self.habitaciones[self.posicion]

    def actuar(self):
        estado = self.percibir()

        print(f"Está en la habitación {self.posicion}")
        print(f"Estado: {estado}")

        if estado == "Sucia":
            print("Acción: Aspirar")
            self.habitaciones[self.posicion] = "Limpia"

        else:
            if self.posicion == "A":
                print("Acción: Moverse a B")
                self.posicion = "B"
            else:
                print("Acción: Moverse a A")
                self.posicion = "A"

        print("----------------------")

aspiradora = AgenteAspiradora()

for i in range(6):
    aspiradora.actuar()

print("Estado final:")
print(aspiradora.habitaciones)
