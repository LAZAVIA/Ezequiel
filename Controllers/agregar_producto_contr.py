import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Connection import connection
from Models.Product import Product

class AgregarProductoController():
    def __init__(self, AgregarProducto):
        self.product = Product(connection())
        self.create_product = AgregarProducto
    
    def createProduct(self,cod,lote, nombre, detalle, cantidad, fecha_ing, fecha_venc, precio, AgregarProducto):
        if cod and lote and nombre and detalle and cantidad and fecha_ing and fecha_venc and precio:
            self.product.insertProduct(cod,lote, nombre, detalle, cantidad, fecha_ing, fecha_venc, precio)
            AgregarProducto.hide()