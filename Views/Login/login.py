import sys
import os
from login_ui import *
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.login_controller import LoginController
from Views.Stock.consultar_stock import Ui_ConsultarStock

class MainWindow(QtWidgets.QMainWindow, Ui_login): 
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        
        self.login_controller = LoginController(self)
        
        self.setupUi(self)
#--------------------------------Events--------------------------------------------
        self.x = self.btn_ingresar.clicked.connect(lambda:self.login_controller.login(self.input_usuario.text(),self.input_Password.text(),Ui_ConsultarStock,login))
       
#------------------------------End Events-----------------------------------------------

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()