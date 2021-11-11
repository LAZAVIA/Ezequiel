import sys
import os

from agregar_producto3 import *
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.agregar_producto_contr import AgregarProductoController

class MainWindow(QtWidgets.QMainWindow, Ui_Ezequiel):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.ap_controller = AgregarProductoController(self)

        self.setupUi(self)
        
        #--------------------Events--------------------------------------
        self.x = self.btn_agregar.clicked.connect(lambda:self.ap_controller.agregar_producto(self.input_nombre.string, Ui_Ezequiel))
        #cod, nombre, cantidad, stock maximo, stock minimo, precio, AgregarProducto
        #--------------------End Events---------------------------------

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()