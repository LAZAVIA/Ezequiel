import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Usuario import Usuario

class LoginController():

    def __init__(self, login):
        self.usuario = Usuario(connection())
        self.login = login

    def login(self,usuario,contrasena, Ui_login, login):
        if usuario and contrasena:
            usuario = self.usuario.getUsuario(usuario, contrasena)
            if usuario:
                login.hide()
                self.login.Form = QtWidgets.QMainWindow()
                self.login.ui = Ui_login()
                self.login.ui.setupUi(self.login.Form)
                self.login.Form.show()
                print('Estás logueado')
            else:
                print('No estás logueado')
