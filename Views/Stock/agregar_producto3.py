# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar_producto.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ezequiel(object):
    def setupUi(self, Ezequiel):
        Ezequiel.setObjectName("Ezequiel")
        Ezequiel.resize(589, 593)
        self.centralwidget = QtWidgets.QWidget(Ezequiel)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 71, 339, 351))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_agregarProducto = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_agregarProducto.setFont(font)
        self.lbl_agregarProducto.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_agregarProducto.setObjectName("lbl_agregarProducto")
        self.gridLayout.addWidget(self.lbl_agregarProducto, 0, 0, 1, 2)
        self.lbl_codigo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_codigo.setFont(font)
        self.lbl_codigo.setObjectName("lbl_codigo")
        self.gridLayout.addWidget(self.lbl_codigo, 1, 0, 1, 1)
        self.input_codigo = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_codigo.setFont(font)
        self.input_codigo.setObjectName("input_codigo")
        self.gridLayout.addWidget(self.input_codigo, 1, 1, 1, 1)
        self.lbl_nombre = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.gridLayout.addWidget(self.lbl_nombre, 2, 0, 1, 1)
        self.input_nombre = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_nombre.setFont(font)
        self.input_nombre.setObjectName("input_nombre")
        self.gridLayout.addWidget(self.input_nombre, 2, 1, 1, 1)
        self.lbl_stockMaximo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_stockMaximo.setFont(font)
        self.lbl_stockMaximo.setObjectName("lbl_stockMaximo")
        self.gridLayout.addWidget(self.lbl_stockMaximo, 3, 0, 1, 1)
        self.input_stockMaximo = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_stockMaximo.setFont(font)
        self.input_stockMaximo.setText("")
        self.input_stockMaximo.setObjectName("input_stockMaximo")
        self.gridLayout.addWidget(self.input_stockMaximo, 3, 1, 1, 1)
        self.lbl_stockMinimo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_stockMinimo.setFont(font)
        self.lbl_stockMinimo.setObjectName("lbl_stockMinimo")
        self.gridLayout.addWidget(self.lbl_stockMinimo, 4, 0, 1, 1)
        self.input_stockMinimo = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_stockMinimo.setFont(font)
        self.input_stockMinimo.setObjectName("input_stockMinimo")
        self.gridLayout.addWidget(self.input_stockMinimo, 4, 1, 1, 1)
        self.lbl_cantidad = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cantidad.setFont(font)
        self.lbl_cantidad.setObjectName("lbl_cantidad")
        self.gridLayout.addWidget(self.lbl_cantidad, 5, 0, 1, 1)
        self.input_cantidad = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_cantidad.setFont(font)
        self.input_cantidad.setObjectName("input_cantidad")
        self.gridLayout.addWidget(self.input_cantidad, 5, 1, 1, 1)
        self.lbl_fecha_ingreso = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_fecha_ingreso.setFont(font)
        self.lbl_fecha_ingreso.setObjectName("lbl_fecha_ingreso")
        self.gridLayout.addWidget(self.lbl_fecha_ingreso, 6, 0, 1, 1)
        self.input_fecha_ingreso = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_fecha_ingreso.setFont(font)
        self.input_fecha_ingreso.setObjectName("input_fecha_ingreso")
        self.gridLayout.addWidget(self.input_fecha_ingreso, 6, 1, 1, 1)
        self.lbl_fecha_egreso = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_fecha_egreso.setFont(font)
        self.lbl_fecha_egreso.setObjectName("lbl_fecha_egreso")
        self.gridLayout.addWidget(self.lbl_fecha_egreso, 7, 0, 1, 1)
        self.input_fecha_egreso = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_fecha_egreso.setFont(font)
        self.input_fecha_egreso.setObjectName("input_fecha_egreso")
        self.gridLayout.addWidget(self.input_fecha_egreso, 7, 1, 1, 1)
        self.lbl_fecha_vencimiento = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_fecha_vencimiento.setFont(font)
        self.lbl_fecha_vencimiento.setObjectName("lbl_fecha_vencimiento")
        self.gridLayout.addWidget(self.lbl_fecha_vencimiento, 8, 0, 1, 1)
        self.input_fecha_vencimiento = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_fecha_vencimiento.setFont(font)
        self.input_fecha_vencimiento.setObjectName("input_fecha_vencimiento")
        self.gridLayout.addWidget(self.input_fecha_vencimiento, 8, 1, 1, 1)
        self.lbl_precio = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio.setFont(font)
        self.lbl_precio.setObjectName("lbl_precio")
        self.gridLayout.addWidget(self.lbl_precio, 9, 0, 1, 1)
        self.input_precio = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_precio.setFont(font)
        self.input_precio.setObjectName("input_precio")
        self.gridLayout.addWidget(self.input_precio, 9, 1, 1, 1)
        self.btn_agregar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setObjectName("btn_agregar")
        self.gridLayout.addWidget(self.btn_agregar, 10, 0, 1, 1)
        self.btn_borrar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_borrar.setFont(font)
        self.btn_borrar.setObjectName("btn_borrar")
        self.gridLayout.addWidget(self.btn_borrar, 10, 1, 1, 1)
        Ezequiel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ezequiel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 21))
        self.menubar.setObjectName("menubar")
        Ezequiel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ezequiel)
        self.statusbar.setObjectName("statusbar")
        Ezequiel.setStatusBar(self.statusbar)

        self.retranslateUi(Ezequiel)
        QtCore.QMetaObject.connectSlotsByName(Ezequiel)

    def retranslateUi(self, Ezequiel):
        _translate = QtCore.QCoreApplication.translate
        Ezequiel.setWindowTitle(_translate("Ezequiel", "Ezequiel"))
        self.lbl_agregarProducto.setText(_translate("Ezequiel", "Agregar Producto "))
        self.lbl_codigo.setText(_translate("Ezequiel", "Código: "))
        self.input_codigo.setPlaceholderText(_translate("Ezequiel", "código"))
        self.lbl_nombre.setText(_translate("Ezequiel", "Nombre: "))
        self.input_nombre.setPlaceholderText(_translate("Ezequiel", "nombre"))
        self.lbl_stockMaximo.setText(_translate("Ezequiel", "Stock Máximo: "))
        self.input_stockMaximo.setPlaceholderText(_translate("Ezequiel", "stockMaximo"))
        self.lbl_stockMinimo.setText(_translate("Ezequiel", "Stock Mínimo: "))
        self.input_stockMinimo.setPlaceholderText(_translate("Ezequiel", "stockMinimo"))
        self.lbl_cantidad.setText(_translate("Ezequiel", "Cantidad: "))
        self.input_cantidad.setPlaceholderText(_translate("Ezequiel", "cantidad"))
        self.lbl_fecha_ingreso.setText(_translate("Ezequiel", "Fecha Ingreso:"))
        self.input_fecha_ingreso.setPlaceholderText(_translate("Ezequiel", "fecha_ingreso"))
        self.lbl_fecha_egreso.setText(_translate("Ezequiel", "Fecha Egreso:"))
        self.input_fecha_egreso.setPlaceholderText(_translate("Ezequiel", "fecha_egreso"))
        self.lbl_fecha_vencimiento.setText(_translate("Ezequiel", "Fecha Vencimiento: "))
        self.input_fecha_vencimiento.setPlaceholderText(_translate("Ezequiel", "fecha_vencimiento"))
        self.lbl_precio.setText(_translate("Ezequiel", "Precio: "))
        self.input_precio.setPlaceholderText(_translate("Ezequiel", "precio"))
        self.btn_agregar.setText(_translate("Ezequiel", "AGREGAR"))
        self.btn_borrar.setText(_translate("Ezequiel", "BORRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ezequiel = QtWidgets.QMainWindow()
    ui = Ui_Ezequiel()
    ui.setupUi(Ezequiel)
    Ezequiel.show()
    sys.exit(app.exec_())
