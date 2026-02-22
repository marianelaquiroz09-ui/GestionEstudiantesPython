class Estudiante:
    
    def __init__(self, nombre, edad, calificacion1, calificacion2):
        self.nombre = nombre
        self.edad = edad
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2
    
    def calcular_promedio(self):
        return (self.calificacion1 + self.calificacion2) / 2
    
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Promedio:", self.calcular_promedio())


