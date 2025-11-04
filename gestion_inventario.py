"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: _______________________________________
Fecha: __________________________________________

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self,codigo ,nombre, contacto):
        self.codigo = codigo
        self.nombre = nombre
        self.contacto = contacto
        # TODO: definir los atributos de la clase
        pass

    def __str__(self):
        # TODO: devolver una cadena legible con el nombre y el contacto del proveedor
        return f"{self.nombre} ({self.contacto})"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor
        # TODO: definir los atributos de la clase
        pass

    def __str__(self):
        # TODO: devolver una representación legible del producto
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"
        return f"[{self.codigo}] {self.nombre} - {self.precio} ({self.stock} uds.) | {self.proveedor})"


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero
        self.productos = []
        self.cargar()
        # TODO: definir los atributos e inicializar la lista de productos
        pass

    def cargar(self):
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """
        # TODO: implementar la lectura del fichero JSON y la creación de objetos
        with open(self.nombre_fichero, 'r') as fichero:
            datos = json.load(fichero)
            for i in datos:
                self.productos.append(Producto(i['codigo'], i['nombre'], i['precio'], i['stock'], Proveedor(i['proveedor']['codigo'], i['proveedor']['nombre'], i['proveedor']['contacto'])))
        pass 

    def guardar(self):
        """
        Guarda el inventario actual en el fichero JSON.
        Convierte los objetos Producto y Proveedor en diccionarios.
        """
        # TODO: recorrer self.productos y guardar los datos en formato JSON
        with open(self.nombre_fichero, 'w') as fichero:
            datos = []
            for i in self.productos:
                diccionario = {"codigo": i.codigo,
        "nombre": i.nombre,
        "precio": i.precio,
        "stock": i.stock,
        "proveedor": {
            "codigo": i.proveedor.codigo,
            "nombre": i.proveedor.nombre,
            "contacto": i.proveedor.contacto
        }}
                datos.append(diccionario)
            json.dump(datos, fichero ,indent= 4, ensure_ascii=False)
        pass

    def anadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario si el código no está repetido.
        """
        # TODO: comprobar si el código ya existe y, si no, añadirlo
        encontrado = False
        for i in self.productos:
            if i.codigo.lower() == producto.codigo.lower():
                encontrado = True
                break
        if encontrado == False:
            self.productos.append(producto)
        else:
            print("Producto con codigo repetido")
        pass

    def mostrar(self):
        """
        Muestra todos los productos del inventario.
        """
        # TODO: mostrar todos los productos almacenados
        for i in self.productos:
            print(i)
        pass

    def buscar(self, codigo):
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        # TODO: buscar un producto por código
        codigo_buscar = [i for i in self.productos if i.codigo.lower() == codigo.lower()]
        if codigo_buscar:
            return codigo_buscar[0]
        return None

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        """
        Permite modificar los datos de un producto existente.
        """
        # TODO: buscar el producto y actualizar sus atributos
        producto = self.buscar(codigo)
        if producto:
            if nombre:
                producto.nombre = nombre
            if precio:
                producto.precio = float(precio)
            if stock:
                producto.stock = int(stock)
        else:
            print("Producto no encontrado")
        pass

    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        # TODO: eliminar el producto de la lista
        for indice, producto in enumerate(self.productos):
            if codigo.lower() == producto.codigo.lower():
                del(self.productos[indice])
                print("Producto Eliminado")
                break
        pass

    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock
        resultado = 0
        for i in self.productos:
            resultado += i.precio * i.stock
        return resultado

    def mostrar_por_proveedor(self, nombre_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        lista = [i for i in self.productos if i.proveedor.nombre.lower() == nombre_proveedor.lower()]
        if lista:
            for i in lista:
                print(i)
        else:
            print("No se encontraron productos de ese proveedor.")
        pass


# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida
    oInventario = Inventario("inventario.json")
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                codigo = input("Codigo: ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))
                codigo_proveedor = input("Codigo Proveedor: ")
                nombre_proveedor = input("Nombre Proveedor: ")
                contacto = input("Contacto: ")
                
                oInventario.anadir_producto(Producto(codigo, nombre, precio, stock, Proveedor(codigo_proveedor, nombre_proveedor, contacto)))
            elif opcion == 2:
                oInventario.mostrar()
            elif opcion == 3:
                codigo = input("Introduzca el codigo a buscar: ")
                producto = oInventario.buscar(codigo)
                if producto:
                    print(producto)
                else:
                    print("Producto no encontrado")
            elif opcion == 4:
                codigo = input("Codigo: ")
                nombre = input("Nombre: ")
                precio = input("Precio: ")
                stock = input("Stock: ")
                oInventario.modificar(codigo, nombre, precio, stock)
            elif opcion == 5:
                codigo = input("Codigo: ")
                oInventario.eliminar(codigo)
            elif opcion == 6:
                valor = oInventario.valor_total()
                print(f"El valor del inventario es: {valor}")
            elif opcion == 7:
                nombre_proveedor = input("Nombre Proveedor: ")
                oInventario.mostrar_por_proveedor(nombre_proveedor)
            elif opcion == 8:
                oInventario.guardar()
                break
            else:
                print("Elije un numero entre el 1 y el 8")
        except:
            print("Tienes que meter un número")
        # TODO: implementar las acciones correspondientes a cada opción del menú

if __name__ == "__main__":
    main()
