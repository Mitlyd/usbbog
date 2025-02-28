#!/usr/bin/env python3

"""
Título de práctica: Clase que modela un producto de la tienda

Descripción extendida del programa
Este programa permite gestionar un inventario básico para una tienda. El usuario podrá ingresar los datos de tres productos, incluyendo su nombre, precio y cantidad disponible. Al final, se mostrará un resumen con los productos registrados, indicando su nombre, la cantidad en stock y el precio en pesos.

El código está estructurado en tres partes principales:

1. **Clase Producto**: Representa cada producto con su nombre, precio y cantidad disponible.
   
2. **Función solicitar_producto**: Solicita los datos de un producto (nombre, precio y cantidad) al usuario y devuelve un objeto de tipo `Producto`.

3. **Función principal (main)**: Administra la recolección de los datos de tres productos y muestra un resumen con toda la información ingresada.

Es una manera sencilla de ingresar y mostrar información sobre productos en una tienda.
"""

Autor:MICHEEL FERNANDA QUINTERO <micheelfernandaquintero3012@gmail.com>
Fecha: 2025-02-27
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""

    # **** Poner el código ejecutable de su ejercicio aquí

    
class Producto:
    """Clase que modela un producto de la tienda."""
    
    def __init__(self, nombre: str, precio: int, cantidad: int):
        """
        Inicializa un producto con nombre, precio unitario y cantidad.
        
        :param nombre: Nombre del producto.
        :param precio: Precio unitario en COP.
        :param cantidad: Cantidad disponible en unidades.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        """Devuelve una representación en texto del producto."""
        return f"|{self.nombre:<10} |{self.cantidad:<12} unidades |{self.precio:<10} pesos |"


def solicitar_producto(numero: int) -> Producto:
    """Solicita los datos de un producto al usuario y devuelve un objeto Producto."""
    nombre = input(f"> Producto {numero}, ¿cuál es el nombre?\n< ")
    precio = int(input(f"> ¿Cuál es el precio de '{nombre}'?\n< "))
    cantidad = int(input(f"> ¿Qué cantidad hay de '{nombre}'?\n< "))
    return Producto(nombre, precio, cantidad)


def main():
    """Función principal que gestiona la recolección y visualización de los productos."""
    productos = [solicitar_producto(i) for i in range(1, 4)]

    print("\n> Resumen:")
    print("> |Producto  |Cantidad      |Precio      |")
    print("> |" + "-"*38 + "|")
    for producto in productos:
        print("> " + str(producto))


if __name__ == "__main__":
    main()

    


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
