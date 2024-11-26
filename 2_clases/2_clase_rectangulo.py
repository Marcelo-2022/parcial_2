class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


# Probando
rectangulo1 = Rectangulo(10, 8)
print(rectangulo1.area())        # Salida: 80
print(rectangulo1.perimetro())   # Salida: 36
