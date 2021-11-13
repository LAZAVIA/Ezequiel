import sys
import os
from consultar_stock import *
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.consultar_stock_contr import ConsultarStockController
from Views.Stock.agregar_producto import Ui_AgregarProducto

class MainWindow(QtWidgets.QMainWindow, Ui_ConsultarStock):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.cs_controller = ConsultarStockController(self)
        self.setupUi(self)
        
        #--------------------Events--------------------------------------
        self.l = self.btn_list.clicked.connect(lambda:self.cs_controller.listProducts())
        self.c = self.btn_create.clicked.connect(lambda:self.cs_controller.openCreate(Ui_AgregarProducto))
        self.r = self.btn_read.clicked.connect(lambda:self.cs_controller.showProduct())
        self.d = self.btn_delete.clicked.connect(lambda:self.cs_controller.deleteProduct())
        #--------------------End Events---------------------------------

if __name__ == "__main__":
   app = QtWidgets.QApplication([])
   window = MainWindow()
   window.show()
   app.exec_()