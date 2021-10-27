import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.consultar_stock import ConsultarStockController
from Views.Stock.Agregar_Producto_Ezequiel_ui import Ui_AgregarProducto
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsultarStock(object):

    def __init__(self):
        self.consultarstock_controller = ConsultarStockController(self)

    def setupUi(self, ConsultarStock):
        ConsultarStock.setObjectName("ConsultarStock")
        ConsultarStock.resize(677, 512)
        self.centralwidget = QtWidgets.QWidget(ConsultarStock)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 20, 451, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)
        self.table_product = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_product.setRowCount(10)
        self.table_product.setObjectName("table_product")
        self.table_product.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.table_product, 1, 0, 1, 5)
        self.btn_list = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_list.setFont(font)
        self.btn_list.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_list.setObjectName("btn_list")
        self.gridLayout.addWidget(self.btn_list, 2, 0, 1, 1)
        self.btn_update = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_update.setObjectName("btn_update")
        self.gridLayout.addWidget(self.btn_update, 2, 1, 1, 1)
        self.btn_create = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_create.setObjectName("btn_create")
        self.gridLayout.addWidget(self.btn_create, 2, 2, 1, 1)
        self.btn_read = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_read.setFont(font)
        self.btn_read.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_read.setObjectName("btn_read")
        self.gridLayout.addWidget(self.btn_read, 2, 3, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 2, 4, 1, 1)
        ConsultarStock.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ConsultarStock)
        self.statusbar.setObjectName("statusbar")
        ConsultarStock.setStatusBar(self.statusbar)

        self.retranslateUi(ConsultarStock)
        QtCore.QMetaObject.connectSlotsByName(ConsultarStock)
        #--------------------Events--------------------------------------
        self.l = self.btn_list.clicked.connect(lambda:self.principal_controller.listProducts())
        self.c = self.btn_create.clicked.connect(lambda:self.principal_controller.openCreate(Ui_AgregarProducto))
        self.r = self.btn_read.clicked.connect(lambda:self.principal_controller.showProduct())
        self.u = self.btn_update.clicked.connect(lambda:self.principal_controller.updateProducs())
        self.d = self.btn_delete.clicked.connect(lambda:self.principal_controller.deleteProduct())
        #--------------------End Events---------------------------------

    def retranslateUi(self, ConsultarStock):
        _translate = QtCore.QCoreApplication.translate
        Ui_AgregarProducto.setWindowTitle(_translate("ConsultarStock", "MainWindow"))
        self.label.setText(_translate("ConsultarStock", "Ventana Principal"))
        item = self.table_product.horizontalHeaderItem(0)
        item.setText(_translate("ConsultarStock", "CODIGO"))
        item = self.table_product.horizontalHeaderItem(1)
        item.setText(_translate("ConsultarStock", "NOMBRE"))
        item = self.table_product.horizontalHeaderItem(2)
        item.setText(_translate("ConsultarStock", "PRECIO"))
        item = self.table_product.horizontalHeaderItem(3)
        item.setText(_translate("ConsultarStock", "CATEGORIA"))
        self.btn_list.setText(_translate("ConsultarStock", "Listar"))
        self.btn_update.setText(_translate("ConsultarStock", "Actualizar"))
        self.btn_create.setText(_translate("ConsultarStock", "Crear"))
        self.btn_read.setText(_translate("ConsultarStock", "Seleccionar"))
        self.btn_delete.setText(_translate("ConsultarStock", "Eliminar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConsultarStock = QtWidgets.QMainWindow()
    ui = Ui_ConsultarStock()
    ui.setupUi(ConsultarStock)
    ConsultarStock.show()
    sys.exit(app.exec_())