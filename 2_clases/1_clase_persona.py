class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


persona1 = Persona("Kay", 99)
persona1.saludar()  # Salida: Hola, mi nombre es Kay y tengo 99 años.
