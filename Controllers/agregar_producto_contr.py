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
    
    def agregarProducto(self, cod, nombre, cantidad, stockmax, stockmin, fecha_ing, fecha_egr, fecha_vto, precio, AgregarProducto):
        if cod and nombre and cantidad and stockmax and stockmin and fecha_ing and fecha_egr and fecha_vto and precio:
            self.product.insertProduct(cod, nombre, cantidad, stockmax, stockmin, fecha_ing, fecha_egr, fecha_vto, precio)
            AgregarProducto.hide()