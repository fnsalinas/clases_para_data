
class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = 0
    
    def describir(self):
        return f"Automóvil {self.marca} {self.modelo} de color {self.color}"

    def conducir(self, km):
        self.kilometraje += km
        return f"Conduciendo {km} km. Kilometraje total: {self.kilometraje} km."
    
    def devolver_toda_la_informacion(self):
        return f"Automóvil {self.marca} {self.modelo} de color {self.color}. Kilometraje: {self.kilometraje} km."

# Creando una instancia de Automovil
auto_brayan = Automovil("Toyota", "Corolla", "Azul")
auto_david = Automovil("Renault", "Logan", "Gris")
auto_andres = Automovil("Renault", "4", "Azul")
auto_fabio = Automovil("Mazda", "3", "Rojo")

auto_david.describir()
auto_david.conducir(km=100)

auto_david.conducir(km=50)
auto_david.conducir(km=5000)

auto_andres.conducir(km=285)


auto_david.kilometraje
auto_david.devolver_toda_la_informacion()

######### Clases ára datos

import datetime

# Mis datos son de una tabla que se llama sise_generales_pv_header
# process_id: string
# process_dt: datetime.datetime
# id_day: datetime.date
# id_pv: int

class FilaPvHeader:
    def __init__(self, process_id, process_dt, id_day, id_pv):
        self.process_id = process_id
        self.process_dt = process_dt
        self.id_day = id_day
        self.id_pv = id_pv

    def devolver_toda_la_informacion(self):
        return f"process_id: {self.process_id}, process_dt: {self.process_dt}, id_day: {self.id_day}, id_pv: {self.id_pv}"
    
    def modificar_process_id(self, nuevo_process_id):
        self.process_id = nuevo_process_id
        return f"Nuevo process_id: {self.process_id}"

fila1 = FilaPvHeader("1", datetime.datetime.now(), datetime.date(2021, 1, 1), 1)

fila1.devolver_toda_la_informacion()

fila1.modificar_process_id("1000")

fila1.process_id

