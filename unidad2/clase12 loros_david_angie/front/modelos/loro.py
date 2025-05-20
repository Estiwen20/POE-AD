class Loro:
    def __init__(self, nombre, edad, color, tamaño, tamaño_alas):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.tamaño = tamaño
        self.tamaño_alas = tamaño_alas

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, color {self.color}, tamaño {self.tamaño}, alas {self.tamaño_alas} cm"
