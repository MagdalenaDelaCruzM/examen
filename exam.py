from datetime import datetime

# Base class (Herencia)
class Usuario:
    def __init__(self, nombre, direccion, telefono):
        self._nombre = nombre  # Encapsulamiento
        self._direccion = direccion  # Encapsulamiento
        self._telefono = telefono  # Encapsulamiento

    # Métodos getter y setter (Encapsulamiento)
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono


class Libro:
    def __init__(self, autor, titulo, editorial, genero, fecha_publicacion):
        self._autor = autor  # Encapsulamiento
        self._titulo = titulo  # Encapsulamiento
        self._editorial = editorial
        self._genero = genero
        self._fecha_publicacion = fecha_publicacion

    # Métodos getter y setter (Encapsulamiento)
    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor


class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None

    def registrar_devolucion(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion


# Clase Catálogo (Polimorfismo: misma interfaz para diferentes acciones)
class Catalogo:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.get_titulo().lower() == titulo.lower():
                return libro
        return None

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"Título: {libro.get_titulo()}, Autor: {libro.get_autor()}") 


# Clase Administrador (Herencia y Polimorfismo)
class Administrador(Usuario):
    def __init__(self, nombre, direccion, telefono):
        super().__init__(nombre, direccion, telefono)  # Herencia

    def actualizar_catalogo(self, catalogo, accion, libro=None):
        try:
            # Manejo de errores
            if accion == "agregar" and libro:
                catalogo.agregar_libro(libro)
                print("Libro agregado exitosamente.")
            elif accion == "mostrar":
                catalogo.mostrar_libros()
            else:
                raise ValueError("Acción inválida o libro no proporcionado.")  # Manejo de errores
        except ValueError as e:
            print(f"Error: {e}")  # Manejo de errores


# Ejemplo de uso
if __name__ == "__main__":
    # Crear usuarios
    usuario1 = Usuario("Juan Pérez", "Calle Falsa 123", 5551234567)

    # Crear libros
    libro1 = Libro("Carlos Cuahutemoc Sanchez", "Los ojos de mi princesa", "Diamante", "Novela", "2024-01-01")
    libro2 = Libro("Julio Verne", "De la tierra a la luna", "Pluton", "Novela", "2023-05-05")
    libro3 = Libro("Octavio paz", "Laberinto de la soledad", "porrua", "Novela", "2023-08-05")
    libro4 = Libro("Octavio paz", "20 poemas de amor y una rosa", "porrua", "romance", "2024-03-05")

    # Crear catálogo
    catalogo = Catalogo()

    # Crear administrador
    admin = Administrador("Admin", "Calle Admin 456", 5559876543)

    # Administrador agrega libros al catálogo
    admin.actualizar_catalogo(catalogo, "agregar", libro1)
    admin.actualizar_catalogo(catalogo, "agregar", libro2)

    # Mostrar catálogo
    admin.actualizar_catalogo(catalogo, "mostrar")

    # Opción para buscar libros desde la terminal
    while True:
        print("\nMenú de opciones:")
        print("1. Buscar un libro")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo_buscar = input("Introduce el título del libro que deseas buscar: ")
            libro_encontrado = catalogo.buscar_libro(titulo_buscar)
            if libro_encontrado:
                print(f"Libro encontrado: Título: {libro_encontrado.get_titulo()}, Autor: {libro_encontrado.get_autor()}")
            else:
                print("El libro no está disponible en el catálogo.")
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")
