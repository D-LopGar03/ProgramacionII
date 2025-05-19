# 1

from enum import Enum
import sys
from typing import List, Dict, Optional, Tuple

class Clase(Enum):
    ECONOMICA = 1
    EJECUTIVA = 2
    PREMIUM = 3

class Genero(Enum):
    MASCULINO = 'M'
    FEMENINO = 'F'
    OTRO = 'O'

class Estrato(Enum):
    UNO = 1
    DOS = 2
    TRES = 3
    CUATRO = 4
    CINCO = 5
    SEIS = 6

class TipoCarga(Enum):
    BICICLETA = 1
    MASCOTA = 2

class TipoMascota(Enum):
    PERRO = 1
    GATO = 2

class Ciudad:
    def __init__(self, nombre: str, pais: str):
        self.nombre = nombre
        self.pais = pais
    
    def __str__(self):
        return f"{self.nombre}, {self.pais}"

class Vuelo:
    def __init__(self, origen: Ciudad, destino: Ciudad, fecha: str, codigo: str):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.codigo = codigo
        self.tiquetes: List['Tiquete'] = []
    
    def __str__(self):
        return f"Vuelo {self.codigo}: {self.origen} -> {self.destino} ({self.fecha})"

class Equipaje:
    def __init__(self, peso: float):
        self.peso = peso
    
    def calcular_costo(self, tiquete: 'Tiquete') -> float:
        pass

class EquipajeAdicional(Equipaje):
    def calcular_costo(self, tiquete: 'Tiquete') -> float:
        if not hasattr(tiquete, 'clase'):
            return 0.0
        
        peso_permitido = {
            Clase.ECONOMICA: 10,
            Clase.EJECUTIVA: 20,
            Clase.PREMIUM: 30
        }.get(tiquete.clase, 0)
        
        exceso = self.peso - peso_permitido
        if exceso <= 0:
            return 0.0
        
        costo_por_kilo = {
            Clase.ECONOMICA: 5000,
            Clase.EJECUTIVA: 10000,
            Clase.PREMIUM: tiquete.costo_base * 0.01
        }.get(tiquete.clase, 0)
        
        return exceso * costo_por_kilo

class Bicicleta(Equipaje):
    def __init__(self, peso: float, costo_por_kilo: float):
        super().__init__(peso)
        self.costo_por_kilo = costo_por_kilo
    
    def calcular_costo(self, tiquete: 'Tiquete') -> float:
        return self.peso * self.costo_por_kilo

class Mascota(Equipaje):
    def __init__(self, peso: float, tipo: TipoMascota):
        super().__init__(peso)
        self.tipo = tipo
    
    def calcular_costo(self, tiquete: 'Tiquete') -> float:
        porcentaje = {
            TipoMascota.PERRO: 0.05,
            TipoMascota.GATO: 0.02
        }.get(self.tipo, 0)
        
        return tiquete.costo_base * porcentaje

class Tiquete:
    def __init__(self, vuelo: Vuelo, pasajero: 'Pasajero', costo_base: float):
        self.vuelo = vuelo
        self.pasajero = pasajero
        self.costo_base = costo_base
        self.equipajes: List[Equipaje] = []
        vuelo.tiquetes.append(self)
    
    def agregar_equipaje(self, equipaje: Equipaje):
        self.equipajes.append(equipaje)
    
    def calcular_costo_equipaje(self) -> float:
        return sum(e.calcular_costo(self) for e in self.equipajes)
    
    def calcular_total(self) -> float:
        costo_equipaje = self.calcular_costo_equipaje()

        
        
        return self.pasajero.aplicar_descuentos(self.costo_base + costo_equipaje)
    
    def __str__(self):
        return f"Tiquete para {self.pasajero.nombre} en {self.vuelo}"

class TiqueteNormal(Tiquete):
    def __init__(self, vuelo: Vuelo, pasajero: 'Pasajero', costo_base: float, clase: Clase):
        super().__init__(vuelo, pasajero, costo_base)
        self.clase = clase
    
    def __str__(self):
        return f"{super().__str__()} (Clase: {self.clase.name})"

class PaqueteTuristico(Tiquete):
    def __init__(self, vuelo: Vuelo, pasajero: 'Pasajero', costo_base: float, descuento: float):
        super().__init__(vuelo, pasajero, costo_base)
        self.descuento = descuento
    
    def calcular_total(self) -> float:
        costo_equipaje = self.calcular_costo_equipaje()
        subtotal = self.costo_base * (1 - self.descuento) + costo_equipaje
        return self.pasajero.aplicar_descuentos(subtotal)
    
    def __str__(self):
        return f"{super().__str__()} (Paquete con {self.descuento*100:.0f}% descuento)"

class Pasajero:
    def __init__(self, identificacion: str, nombre: str, edad: int, genero: Genero, embarazada: bool = False, estrato: str = ""):
        self.identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.embarazada = embarazada
        self.estrato = estrato


    def es_estrato_uno(self) -> bool:
        return self.estrato == Estrato.UNO
    
    def es_infante(self) -> bool:
        return 0 <= self.edad <= 13
    
    def es_adulto_mayor(self) -> bool:
        return self.edad >= 65
    
    def aplicar_descuentos(self, costo_base: float) -> float:
        descuento = 0.0
        
        if self.es_estrato_uno():
            descuento += 0.10

        if self.es_infante():
            descuento += 0.07
        
        if self.es_adulto_mayor():
            descuento += 0.05
        
        if self.genero == Genero.FEMENINO and self.embarazada:
            descuento += 0.10
        
        return costo_base * (1 - min(descuento, 0.22))
    
    def __str__(self):
        embarazo_info = ", embarazada" if self.embarazada else ""
        return f"{self.nombre} ({self.edad} años, {self.genero.name}{embarazo_info})"

class Aerolinea:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.vuelos: List[Vuelo] = []
        self.ciudades: List[Ciudad] = []
        self.tiquetes_vendidos: List[Tiquete] = []
    
    def agregar_ciudad(self, ciudad: Ciudad):
        if ciudad not in self.ciudades:
            self.ciudades.append(ciudad)
    
    def crear_vuelo(self, origen: Ciudad, destino: Ciudad, fecha: str, codigo: str) -> Vuelo:
        vuelo = Vuelo(origen, destino, fecha, codigo)
        self.vuelos.append(vuelo)
        return vuelo
    
    def vender_tiquete(self, vuelo: Vuelo, pasajero: Pasajero, costo_base: float, clase: Optional[Clase] = None, descuento_paquete: float = None) -> Tiquete:
        if clase:
            tiquete = TiqueteNormal(vuelo, pasajero, costo_base, clase)
        else:
            tiquete = PaqueteTuristico(vuelo, pasajero, costo_base, descuento_paquete or 0.0)
        
        self.tiquetes_vendidos.append(tiquete)
        return tiquete
    
    def hacer_checkin(self, tiquete: Tiquete, equipajes: List[Equipaje]) -> float:
        for equipaje in equipajes:
            tiquete.agregar_equipaje(equipaje)
            
        return tiquete.calcular_costo_equipaje()
    
    def devolver_tiquete(self, tiquete: Tiquete) -> bool:
        if tiquete in self.tiquetes_vendidos:
            self.tiquetes_vendidos.remove(tiquete)
            tiquete.vuelo.tiquetes.remove(tiquete)
            return True
        return False
    
    def trayecto_mas_recaudado(self) -> Tuple[Optional[Vuelo], float]:
        if not self.vuelos:
            return None, 0.0
        
        vuelo_recaudo = [(v, sum(t.calcular_total() for t in v.tiquetes)) for v in self.vuelos]
        return max(vuelo_recaudo, key=lambda x: x[1])
    
    def genero_mas_viajero(self, destino: Ciudad) -> Optional[Genero]:
        conteo = {g: 0 for g in Genero}
        
        for t in self.tiquetes_vendidos:
            if t.vuelo.destino == destino:
                conteo[t.pasajero.genero] += 1
        
        if sum(conteo.values()) == 0:
            return None
        
        return max(conteo.items(), key=lambda x: x[1])[0]
    
    def costo_promedio_trayecto(self, origen: Ciudad, destino: Ciudad) -> float:
        tiquetes_trayecto = [
            t for t in self.tiquetes_vendidos
            if t.vuelo.origen == origen and t.vuelo.destino == destino
        ]
        
        if not tiquetes_trayecto:
            return 0.0
        
        return sum(t.calcular_total() for t in tiquetes_trayecto) / len(tiquetes_trayecto)
    
    def recaudo_total_tiquetes(self) -> float:
        return sum(t.calcular_total() for t in self.tiquetes_vendidos)
    
    def recaudo_total_equipaje(self) -> float:
        return sum(t.calcular_costo_equipaje() for t in self.tiquetes_vendidos)

def mostrar_menu_principal():
    print("\n" + "="*50)
    print("SISTEMA DE AEROLÍNEA".center(50))
    print("="*50)
    print("1. Gestión de Ciudades")
    print("2. Gestión de Vuelos")
    print("3. Gestión de Pasajeros")
    print("4. Venta de Tiquetes")
    print("5. Proceso de Check-in")
    print("6. Devolución de Tiquetes")
    print("7. Reportes y Estadísticas")
    print("8. Salir")
    print("="*50)

def gestion_ciudades(aerolinea: Aerolinea):
    while True:
        print("\n" + "="*50)
        print("GESTIÓN DE CIUDADES".center(50))
        print("="*50)
        print("1. Agregar Ciudad")
        print("2. Listar Ciudades")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la ciudad: ")
            pais = input("País: ")
            aerolinea.agregar_ciudad(Ciudad(nombre, pais))
            print(f"Ciudad {nombre} agregada exitosamente!")
        
        elif opcion == "2":
            print("\nCiudades disponibles:")
            for i, ciudad in enumerate(aerolinea.ciudades, 1):
                print(f"{i}. {ciudad}")
        
        elif opcion == "3":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def gestion_vuelos(aerolinea: Aerolinea):
    while True:
        print("\n" + "="*50)
        print("GESTIÓN DE VUELOS".center(50))
        print("="*50)
        print("1. Crear Vuelo")
        print("2. Listar Vuelos")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if len(aerolinea.ciudades) < 2:
                print("Necesita al menos 2 ciudades para crear un vuelo.")
                continue
            
            print("\nCiudades disponibles:")
            for i, ciudad in enumerate(aerolinea.ciudades, 1):
                print(f"{i}. {ciudad}")
            
            try:
                origen_idx = int(input("Seleccione ciudad origen (número): ")) - 1
                destino_idx = int(input("Seleccione ciudad destino (número): ")) - 1
                
                if origen_idx == destino_idx:
                    print("Origen y destino deben ser diferentes.")
                    continue
                
                fecha = input("Fecha del vuelo (YYYY-MM-DD): ")
                codigo = input("Código del vuelo (ej. AV123): ")
                
                vuelo = aerolinea.crear_vuelo(
                    aerolinea.ciudades[origen_idx],
                    aerolinea.ciudades[destino_idx],
                    fecha,
                    codigo
                )
                print(f"Vuelo creado exitosamente: {vuelo}")
            
            except (ValueError, IndexError):
                print("Selección no válida. Intente nuevamente.")
        
        elif opcion == "2":
            print("\nVuelos disponibles:")
            for i, vuelo in enumerate(aerolinea.vuelos, 1):
                print(f"{i}. {vuelo}")
        
        elif opcion == "3":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def gestion_pasajeros() -> Pasajero:
    print("\n" + "="*50)
    print("REGISTRO DE PASAJERO".center(50))
    print("="*50)
    
    identificacion = input("Identificación: ")
    nombre = input("Nombre completo: ")
    
    try:
        edad = int(input("Edad: "))
        if edad < 0 or edad > 120:
            print("Edad debe estar entre 0 y 120.")
            return None
    except ValueError:
        print("Edad debe ser un número válido.")
        return None
    
    print("Género:")
    print("1. Masculino")
    print("2. Femenino")
    print("3. Otro")
    
    genero_opcion = input("Seleccione (1-3): ")
    genero_map = {"1": Genero.MASCULINO, "2": Genero.FEMENINO, "3": Genero.OTRO}
    
    if genero_opcion not in genero_map:
        print("Opción no válida.")
        return None
    
    genero = genero_map[genero_opcion]
    embarazada = False
    estrato_opcion = input("Estrato (UNO-SEIS): ").upper()
    estrato_map = {"UNO": Estrato(1), "DOS": Estrato(2), "TRES": Estrato(3), "CUATRO": Estrato(4), "CINCO": Estrato(5), "SEIS": Estrato(6)}
    if estrato_opcion not in estrato_map:
        print("Opción no válida.")
        return None
    estrato = estrato_map[estrato_opcion]
    
    if genero == Genero.FEMENINO:
        embarazada = input("¿Está embarazada? (s/n): ").lower() == 's'
    
    return Pasajero(identificacion, nombre, edad, genero, embarazada, estrato)

def venta_tiquetes(aerolinea: Aerolinea):
    if not aerolinea.vuelos:
        print("No hay vuelos disponibles. Cree vuelos primero.")
        return
    
    print("\nVuelos disponibles:")
    for i, vuelo in enumerate(aerolinea.vuelos, 1):
        print(f"{i}. {vuelo}")
    
    try:
        vuelo_idx = int(input("Seleccione vuelo (número): ")) - 1
        vuelo = aerolinea.vuelos[vuelo_idx]
    except (ValueError, IndexError):
        print("Selección no válida.")
        return
    
    pasajero = gestion_pasajeros()
    if not pasajero:
        return
    
    print("\nTipo de tiquete:")
    print("1. Tiquete Normal")
    print("2. Paquete Turístico")
    
    tipo_opcion = input("Seleccione (1-2): ")
    
    try:
        costo_base = float(input("Costo base del tiquete: "))
        if costo_base <= 0:
            print("El costo debe ser positivo.")
            return
    except ValueError:
        print("Costo debe ser un número válido.")
        return
    
    if tipo_opcion == "1":
        print("\nClase del tiquete:")
        print("1. Económica")
        print("2. Ejecutiva")
        print("3. Premium")
        
        clase_opcion = input("Seleccione (1-3): ")
        clase_map = {"1": Clase.ECONOMICA, "2": Clase.EJECUTIVA, "3": Clase.PREMIUM}
        
        if clase_opcion not in clase_map:
            print("Opción no válida.")
            return
        
        tiquete = aerolinea.vender_tiquete(vuelo, pasajero, costo_base, clase_map[clase_opcion])
    
    elif tipo_opcion == "2":
        try:
            descuento = float(input("Descuento del paquete (ej. 0.15 para 15%): "))
            if descuento <= 0 or descuento >= 1:
                print("Descuento debe estar entre 0 y 1.")
                return
        except ValueError:
            print("Descuento debe ser un número válido.")
            return
        
        tiquete = aerolinea.vender_tiquete(vuelo, pasajero, costo_base, None, descuento)
    
    else:
        print("Opción no válida.")
        return
    
    print(f"\nTiquete vendido exitosamente:")
    print(tiquete)
    print(f"Total a pagar: ${tiquete.calcular_total():,.2f}")

def proceso_checkin(aerolinea: Aerolinea):
    if not aerolinea.tiquetes_vendidos:
        print("No hay tiquetes vendidos.")
        return
    
    print("\nTiquetes vendidos:")
    for i, tiquete in enumerate(aerolinea.tiquetes_vendidos, 1):
        print(f"{i}. {tiquete}")
    
    try:
        tiquete_idx = int(input("Seleccione tiquete (número): ")) - 1
        tiquete = aerolinea.tiquetes_vendidos[tiquete_idx]
    except (ValueError, IndexError):
        print("Selección no válida.")
        return
    
    equipajes = []
    while True:
        print("\nTipos de equipaje:")
        print("1. Equipaje normal (verificar exceso)")
        print("2. Bicicleta")
        print("3. Mascota")
        print("4. Finalizar check-in")
        
        opcion = input("Seleccione tipo de equipaje (1-4): ")
        
        if opcion == "4":
            break
        
        try:
            peso = float(input("Peso del equipaje (kg): "))
            if peso <= 0 or peso > 100:
                print("Peso debe estar entre 0 y 100 kg.")
                continue
        except ValueError:
            print("Peso debe ser un número válido.")
            continue
        
        if opcion == "1":
            equipajes.append(EquipajeAdicional(peso))
        
        elif opcion == "2":
            try:
                costo_por_kilo = float(input("Costo por kilo de la bicicleta: "))
                equipajes.append(Bicicleta(peso, costo_por_kilo))
            except ValueError:
                print("Costo debe ser un número válido.")
                continue
        
        elif opcion == "3":
            print("Tipo de mascota:")
            print("1. Perro")
            print("2. Gato")
            
            mascota_opcion = input("Seleccione (1-2): ")
            if mascota_opcion == "1":
                equipajes.append(Mascota(peso, TipoMascota.PERRO))
            elif mascota_opcion == "2":
                equipajes.append(Mascota(peso, TipoMascota.GATO))
            else:
                print("Opción no válida.")
                continue
        
        else:
            print("Opción no válida.")
            continue
        
        print("Equipaje agregado exitosamente!")
    
    if equipajes:
        costo_equipaje = aerolinea.hacer_checkin(tiquete, equipajes)
        print(f"\nCheck-in completado para {tiquete.pasajero.nombre}")
        print(f"Costo total de equipaje: ${costo_equipaje:,.2f}")
        print(f"Nuevo total a pagar: ${tiquete.calcular_total():,.2f}")
    else:
        print("No se agregó ningún equipaje.")

def devolucion_tiquetes(aerolinea: Aerolinea):
    if not aerolinea.tiquetes_vendidos:
        print("No hay tiquetes vendidos.")
        return
    
    print("\nTiquetes vendidos:")
    for i, tiquete in enumerate(aerolinea.tiquetes_vendidos, 1):
        print(f"{i}. {tiquete}")
    
    try:
        tiquete_idx = int(input("Seleccione tiquete a devolver (número): ")) - 1
        tiquete = aerolinea.tiquetes_vendidos[tiquete_idx]
    except (ValueError, IndexError):
        print("Selección no válida.")
        return
    
    if aerolinea.devolver_tiquete(tiquete):
        print(f"Tiquete de {tiquete.pasajero.nombre} devuelto exitosamente.")
    else:
        print("Error al devolver el tiquete.")

def mostrar_reportes(aerolinea: Aerolinea):
    while True:
        print("\n" + "="*50)
        print("REPORTES Y ESTADÍSTICAS".center(50))
        print("="*50)
        print("1. Trayecto que más dinero recaudó")
        print("2. Género que más viaja a un destino")
        print("3. Costo promedio del tiquete por trayecto")
        print("4. Recaudo total por tiquetes")
        print("5. Recaudo total por equipaje")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            vuelo, recaudo = aerolinea.trayecto_mas_recaudado()
            if vuelo:
                print(f"\nTrayecto más recaudado: {vuelo}")
                print(f"Recaudo total: ${recaudo:,.2f}")
            else:
                print("No hay datos disponibles.")
        
        elif opcion == "2":
            if not aerolinea.ciudades:
                print("No hay ciudades registradas.")
                continue
            
            print("\nDestinos disponibles:")
            destinos = list({v.destino for v in aerolinea.vuelos})
            for i, destino in enumerate(destinos, 1):
                print(f"{i}. {destino}")
            
            try:
                destino_idx = int(input("Seleccione destino (número): ")) - 1
                destino = destinos[destino_idx]
            except (ValueError, IndexError):
                print("Selección no válida.")
                continue
            
            genero = aerolinea.genero_mas_viajero(destino)
            if genero:
                print(f"\nEl género que más viaja a {destino} es: {genero.name}")
            else:
                print(f"No hay viajeros registrados a {destino}.")
        
        elif opcion == "3":
            if len(aerolinea.ciudades) < 2:
                print("Necesita al menos 2 ciudades.")
                continue
            
            print("\nTrayectos disponibles:")
            trayectos = {(v.origen, v.destino) for v in aerolinea.vuelos}
            for i, (origen, destino) in enumerate(trayectos, 1):
                print(f"{i}. {origen} -> {destino}")
            
            try:
                trayecto_idx = int(input("Seleccione trayecto (número): ")) - 1
                origen, destino = list(trayectos)[trayecto_idx]
            except (ValueError, IndexError):
                print("Selección no válida.")
                continue
            
            promedio = aerolinea.costo_promedio_trayecto(origen, destino)
            print(f"\nCosto promedio para {origen} -> {destino}: ${promedio:,.2f}")
        
        elif opcion == "4":
            total = aerolinea.recaudo_total_tiquetes()
            print(f"\nRecaudo total por tiquetes: ${total:,.2f}")
        
        elif opcion == "5":
            total = aerolinea.recaudo_total_equipaje()
            print(f"\nRecaudo total por equipaje: ${total:,.2f}")
        
        elif opcion == "6":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def main():
    aerolinea = Aerolinea("Avianca")
    
    aerolinea.agregar_ciudad(Ciudad("Bogotá", "Colombia"))
    aerolinea.agregar_ciudad(Ciudad("Medellín", "Colombia"))
    aerolinea.agregar_ciudad(Ciudad("Madrid", "España"))
    aerolinea.agregar_ciudad(Ciudad("París", "Francia"))
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-8): ")
        
        if opcion == "1":
            gestion_ciudades(aerolinea)
        elif opcion == "2":
            gestion_vuelos(aerolinea)
        elif opcion == "3":
            pasajero = gestion_pasajeros()
            if pasajero:
                print(f"\nPasajero registrado: {pasajero}")
        elif opcion == "4":
            venta_tiquetes(aerolinea)
        elif opcion == "5":
            proceso_checkin(aerolinea)
        elif opcion == "6":
            devolucion_tiquetes(aerolinea)
        elif opcion == "7":
            mostrar_reportes(aerolinea)
        elif opcion == "8":
            print("\nGracias por usar el sistema de la aerolínea. ¡Hasta luego!")
            sys.exit(0)
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    try:
         main()
    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario.")
