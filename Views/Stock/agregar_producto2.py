import sys
import os
from Views.Stock.agregar_producto import AgregarProducto
from consultar_stock import *
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.agregar_producto_contr import AgregarProductoController

class MainWindow(QtWidgets.QMainWindow, Ui_ConsultarStock):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.ap_controller = AgregarProductoController(self)

        self.setupUi(self)
        
        #--------------------Events--------------------------------------
        self.x = self.btn_agregar.clicked.connect(lambda:self.ap_controller.agregar_producto(self.input_nombre.string, AgregarProducto))
        #cod,lote, nombre, detalle, cantidad, fecha_ing, fecha_venc, precio, AgregarProducto
        #--------------------End Events---------------------------------

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()