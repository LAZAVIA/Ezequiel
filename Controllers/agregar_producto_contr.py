import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Connection import connection
from Models.Product import Product

class AgregarProductoController():
    def __init__(self, AgregarProducto):
        self.product = Product(connection())
        self.agregar_producto = AgregarProducto
    
    def agregar_producto(self, nombre, cantidad, stockmax, stockmin, precio, AgregarProducto):
        if nombre and cantidad and stockmax and stockmin and precio:
            self.product.insertProduct(nombre, cantidad, stockmax, stockmin, precio)
            AgregarProducto.hide()