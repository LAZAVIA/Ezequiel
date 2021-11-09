import sys
import os
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
        self.x = self.btn_create.clicked.connect(lambda:self.ap_controller.createProduct(self.input_cod.text(),self.input_name.text(),self.input_price.text(),self.input_category.text(),AgregarProducto))
        #--------------------End Events---------------------------------

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
#--------------------Events--------------------------------------
        
        #--------------------End Events---------------------------------
