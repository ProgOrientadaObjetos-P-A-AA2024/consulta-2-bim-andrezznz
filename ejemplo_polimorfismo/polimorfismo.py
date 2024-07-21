from abc import ABC, abstractmethod

class Estudiante(ABC):
    def __init__(self, nombres, apellidos, identificacion, edad):
        self._nombres = nombres
        self._apellidos = apellidos
        self._identificacion = identificacion
        self._edad = edad
        self._matricula = 0.0

    # Métodos establecer
    def establecer_nombres(self, nombres):
        self._nombres = nombres

    def establecer_apellidos(self, apellidos):
        self._apellidos = apellidos

    def establecer_identificacion(self, identificacion):
        self._identificacion = identificacion

    def establecer_edad(self, edad):
        self._edad = edad

    # Métodos obtener
    def obtener_nombres(self):
        return self._nombres

    def obtener_apellidos(self):
        return self._apellidos

    def obtener_identificacion(self):
        return self._identificacion

    def obtener_edad(self):
        return self._edad

    def obtener_matricula(self):
        return self._matricula

    # Método abstracto
    @abstractmethod
    def calcular_matricula(self):
        pass


class EstudianteDistancia(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad, numero_asignaturas, costo_asignatura):
        super().__init__(nombres, apellidos, identificacion, edad)
        self._numero_asignaturas = numero_asignaturas
        self._costo_asignatura = costo_asignatura

    # Métodos establecer
    def establecer_numero_asignaturas(self, numero):
        self._numero_asignaturas = numero

    def establecer_costo_asignatura(self, costo):
        self._costo_asignatura = costo

    # Métodos obtener
    def obtener_numero_asignaturas(self):
        return self._numero_asignaturas

    def obtener_costo_asignatura(self):
        return self._costo_asignatura

    # Sobrescribir el método abstracto
    def calcular_matricula(self):
        self._matricula = self._numero_asignaturas * self._costo_asignatura

    def __str__(self):
        return (f"Nombres: {self.obtener_nombres()}\n"
                f"Apellidos: {self.obtener_apellidos()}\n"
                f"Identificación: {self.obtener_identificacion()}\n"
                f"Edad: {self.obtener_edad()}\n"
                f"Matrícula: {self.obtener_matricula()}")


# Uso de las clases
estudiante = EstudianteDistancia("Juan", "Pérez", "123456789", 30, 5, 100)
estudiante.calcular_matricula()
print(estudiante)