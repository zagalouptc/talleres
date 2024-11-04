#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------- Creación de un constructor tipo Biblioteca ---------------------------------
#---------------------------------------------------------------------------------------------------------------------
#Programa que realiza las transacciones en una biblioteca: 
#1. Crea la clas biblioteca la palabra clave self se refiere a la instancia actual de la clase 
# y se usa para acceder a las variables y métodos de esa instancia
# self.inventario={}, un conjunto vacio
# self.libros_prestados={}, conjuos vacío
# se crean las funciones: agregar libro,
import os                           #Libreria borrar pantalla
os.system('cls')                    #orden para borrar la pantalla
class Biblioteca:
    def __init__(self):
        # Inicializar estructuras de datos para almacenar información
        self.inventario = {}
        self.libros_prestados = set()

    def agregar_libro(self, titulo, autor):
        # Añadir un libro al inventario
        if titulo in self.inventario: #si titulo esta en el conjunto inventario 
            print(f"El libro '{titulo}' ya está en el inventario.") #mensaje de existente
        else: # sino
            self.inventario[titulo] = autor #agrega el libro y el autor al conjunto inventario
            print(f"Libro '{titulo}' de {autor} agregado al inventario.") # imprime registros

    def prestar_libro(self, titulo):
        # Prestar un libro y actualizar el estado de la biblioteca
        if titulo in self.inventario:   #revisa si el titulo está en el conjuto inventario
            if titulo not in self.libros_prestados:  #revisa si el titulo no está prestado
                self.libros_prestados.add(titulo)  # si no está prestado lo adiciona al conunto de prestados
                print(f"Libro '{titulo}' prestado exitosamente.") #mensaje de exito
            else:
                print(f"El libro '{titulo}' ya está prestado.") #Mensaje, si el libro está prestado
        else:
            print(f"El libro '{titulo}' no está en el inventario.") # Mensaje si libro no esta en el invetaro

    def devolver_libro(self, titulo):
        # Devolver un libro y actualizar el estado de la biblioteca
        if titulo in self.inventario:  #si título está en el inventario
            if titulo in self.libros_prestados: #Sí el título estaba prestado
                self.libros_prestados.remove(titulo) #eliminar del conjunto de prestados
                print(f"Libro '{titulo}' devuelto correctamente.") #mensaje de éxito en los devueltos
            else:
                print(f"El libro '{titulo}' no estaba prestado.") #Mensaje del libro no estaba prestado 
        else:
            print(f"El libro '{titulo}' no está en el inventario.") #mensaje, libro no se encuentra en el inventario

    def estado_biblioteca(self):
        # Mostrar el estado actual de la biblioteca
        print("\nEstado actual de la biblioteca:")
        print("Inventario:")
        print(self.inventario) #Mostrar el conjunto de libros 
        for libro, autor in self.inventario.items(): #Recorre el conjunto de libros y carga los campos libro y autor
            print(f"{libro} - {autor}") #Imprime registros

        print("\nLibros Prestados:")
        if self.libros_prestados:
            for libro_prestado in self.libros_prestados:
                print(libro_prestado)
        else:
            print("Ningún libro prestado.")




# Implementación del constructor

# ----Inicialización del constructor----
print('*'*20)
print('Creamos nuestra Biblioteca"')
print('*'*20)

biblioteca = Biblioteca()
# ----Agregamos regístros a nuestra "base de datos"----
print('*'*20)
print("Agregamos los siguientes regístros para poblar nuestra base de datos tipo biblioteca")
print('*'*20)

biblioteca.agregar_libro("El señor de los anillos", "J.R.R. Tolkien")
biblioteca.agregar_libro("1984", "George Orwell")
biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez")
biblioteca.agregar_libro("Revelión de las ratas", "Fernando Soto aparicio") #se inserto uno nuevo
biblioteca.agregar_libro("Revelión de las ratas", "Fernando Soto aparicio") #se inserto uno repetido
# ----Consultamos el estado de nuestra "base de datos"----
print('*'*20)
print("Estado de nuestra 'base de datos' después de agregar regístros")
print('*'*20)

biblioteca.estado_biblioteca()  #imprime los registros de los libros y los prestados

# ----Cambiamos el estado de uno de nuestros regístros----
print('*'*20)
print("Realizamos el préstamo de dos libros")
print('*'*20)

biblioteca.prestar_libro("1984")
biblioteca.prestar_libro("Cien años de soledad")
biblioteca.prestar_libro("Revelión de las ratas")   #se probó el préstmo de un nuevo libro

# ----Consultamos el estado de nuestra "base de datos" despues de un préstamo----
print('*'*20)
print("Consultamos el estado de nuestra 'base de datos' después el préstamo")
print('*'*20)

biblioteca.estado_biblioteca()

# ----Volvemos a cambiar el estado de uno de nuestros regístros----
print('*'*20)
print("Regresamos uno de los libros prestados al inventario")
print('*'*20)

biblioteca.devolver_libro("Revelión de las ratas")
biblioteca.estado_biblioteca()

# ----Consultamos el estado final de nuestra "base de datos"----
print('*'*20)
print("Consutamos el estado de nuestra 'base de datos' después del préstamo")
print('*'*20)

class BuscarYMenu(Biblioteca):
    # Llamada al constructor de la clase base
    def __init__(self):
     super().__init__()


    def buscar_libros_por_autor(self, autor):
        # Buscar libros por autor en el inventario
        libros_encontrados = []

        for titulo, autor_libro in self.inventario.items():
            if autor_libro == autor:
                libros_encontrados.append(titulo)

        if libros_encontrados:
            print(f"\nLibros encontrados de {autor}:")
            for libro_encontrado in libros_encontrados:
                print(libro_encontrado)
        else:
            print(f"No se encontraron libros de {autor} en el inventario.")

    def menu_principal(self):
        # Menú principal con un ciclo while para las transacciones en la biblioteca
        while True:
            print("\n=== Menú Principal ===")
            print("1. Agregar Libro")
            print("2. Prestar Libro")
            print("3. Devolver Libro")
            print("4. Buscar Libros por Autor")
            print("5. Estado de la Biblioteca")
            print("6. Salir")

            opcion = input("Seleccione una opción (1-6): ")

            if opcion == "1":
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                self.agregar_libro(titulo, autor)
            elif opcion == "2":
                titulo = input("Ingrese el título del libro que desea prestar: ")
                self.prestar_libro(titulo)
            elif opcion == "3":
                titulo = input("Ingrese el título del libro que desea devolver: ")
                self.devolver_libro(titulo)
            elif opcion == "4":
                autor = input("Ingrese el autor para buscar libros: ")
                self.buscar_libros_por_autor(autor)
            elif opcion == "5":
                self.estado_biblioteca()
            elif opcion == "6":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejemplo de uso del nuevo menú
biblioteca = BuscarYMenu()
biblioteca.menu_principal()
