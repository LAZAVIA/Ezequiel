import sys
import os
from agregar_producto3 import*
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.agregar_producto_contr import AgregarProductoController
from Views.Stock.consultar_stock import Ui_ConsultarStock

class MainWindow(QtWidgets.QMainWindow, Ui_AgregarProducto): 
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        
        self.Principal_Controller = AgregarProductoController(self)
        
        self.setupUi(self)
#--------------------------------Events--------------------------------------------
        self.l = self.btn_list.clicked.connect(lambda:self.principal_controller.listProducts())
        self.c = self.btn_create.clicked.connect(lambda:self.principal_controller.openCreate(Ui_ConsultarStock))
        self.r = self.btn_read.clicked.connect(lambda:self.principal_controller.showProduct())
        self.u = self.btn_update.clicked.connect(lambda:self.principal_controller.updateProducs())
        self.d = self.btn_delete.clicked.connect(lambda:self.principal_controller.deleteProduct())
#------------------------------End Events-----------------------------------------------

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()