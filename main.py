# Clase que representa a un estudiante
class Estudiante:
    
    # Constructor
    def __init__(self, nombre, edad, calificacion1, calificacion2):
        self.nombre = nombre
        self.edad = edad
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2
    
    # Método para calcular el promedio
    def calcular_promedio(self):
        return (self.calificacion1 + self.calificacion2) / 2
    
    # Método para mostrar información
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Promedio:", self.calcular_promedio())

# Instanciación de objetos
estudiante1 = Estudiante("Carlos", 20, 85.5, 90.0)
estudiante2 = Estudiante("Ana", 22, 78.0, 88.5)

# Uso de métodos
estudiante1.mostrar_informacion()
print("----------------------")
estudiante2.mostrar_informacion()
