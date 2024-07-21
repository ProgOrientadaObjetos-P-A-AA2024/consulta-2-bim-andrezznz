class Empleado:
    def __init__(self, nombre, apellidos, identificacion, edad):
        self._nombre = nombre
        self._apellidos = apellidos
        self._identificacion = identificacion
        self._edad = edad

    # Métodos establecer
    def establecer_nombre(self, nombre):
        self._nombre = nombre

    def establecer_apellidos(self, apellidos):
        self._apellidos = apellidos

    def establecer_identificacion(self, identificacion):
        self._identificacion = identificacion

    def establecer_edad(self, edad):
        self._edad = edad

    # Métodos obtener
    def obtener_nombre(self):
        return self._nombre

    def obtener_apellidos(self):
        return self._apellidos

    def obtener_identificacion(self):
        return self._identificacion

    def obtener_edad(self):
        return self._edad

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellidos, identificacion, edad, salario):
        super().__init__(nombre, apellidos, identificacion, edad)
        self._salario = salario

    # Métodos establecer y obtener para salario
    def establecer_salario(self, salario):
        self._salario = salario

    def obtener_salario(self):
        return self._salario

    def __str__(self):
        return f"Nombre: {self.obtener_nombre()}\nApellidos: {self.obtener_apellidos()}\nIdentificación: {self.obtener_identificacion()}\nEdad: {self.obtener_edad()}\nSalario: {self.obtener_salario()}"

# Uso de las clases
empleado = EmpleadoTiempoCompleto("Juan", "Pérez", "123456789", 30, 50000)
print(empleado)