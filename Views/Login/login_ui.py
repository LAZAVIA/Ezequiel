import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(720, 449)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        login.setFont(font)
        login.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.btnEnter = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnter.setGeometry(QtCore.QRect(240, 340, 111, 41))
        self.btnEnter.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 14pt \"Calibri\"; color: #000000;\n"
"border-color: rgb(0, 0, 255);")
        self.btnEnter.setObjectName("btnEnter")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 190, 521, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblUsername = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lblUsername.setFont(font)
        self.lblUsername.setObjectName("lblUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblUsername)
        self.txtBoxUsername = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.txtBoxUsername.setFont(font)
        self.txtBoxUsername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtBoxUsername.setObjectName("txtBoxUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtBoxUsername)
        self.lblPassword = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblPassword)
        self.txtBoxPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.txtBoxPassword.setFont(font)
        self.txtBoxPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtBoxPassword.setObjectName("txtBoxPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtBoxPassword)
        self.lblUsername_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblUsername_2.setGeometry(QtCore.QRect(140, 80, 471, 32))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(26)
        self.lblUsername_2.setFont(font)
        self.lblUsername_2.setObjectName("lblUsername_2")
        self.btnEnter_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnter_2.setGeometry(QtCore.QRect(380, 340, 111, 41))
        self.btnEnter_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 14pt \"Calibri\"; color: #000000;\n"
"border-color: rgb(0, 0, 255);")
        self.btnEnter_2.setObjectName("btnEnter_2")
        login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.btnEnter.setText(_translate("login", "Ingresar"))
        self.lblUsername.setText(_translate("login", "Nombre de usuario"))
        self.lblPassword.setText(_translate("login", "Contraseña"))
        self.lblUsername_2.setText(_translate("login", "Bienvenido a EZEQUIEL"))
        self.btnEnter_2.setText(_translate("login", "Registrarse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
