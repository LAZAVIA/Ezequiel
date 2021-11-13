# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultar_stock_ultimo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsultarStock(object):
    def setupUi(self, ConsultarStock):
        ConsultarStock.setObjectName("ConsultarStock")
        ConsultarStock.resize(677, 512)
        self.centralwidget = QtWidgets.QWidget(ConsultarStock)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 21, 531, 421))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 5)
        self.btn_list = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_list.setFont(font)
        self.btn_list.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_list.setObjectName("btn_list")
        self.gridLayout.addWidget(self.btn_list, 2, 0, 1, 1)
        self.btn_update = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_update.setObjectName("btn_update")
        self.gridLayout.addWidget(self.btn_update, 2, 1, 1, 1)
        self.btn_create = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_create.setObjectName("btn_create")
        self.gridLayout.addWidget(self.btn_create, 2, 2, 1, 1)
        self.btn_read = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_read.setFont(font)
        self.btn_read.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_read.setObjectName("btn_read")
        self.gridLayout.addWidget(self.btn_read, 2, 3, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.widget)
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

    def retranslateUi(self, ConsultarStock):
        _translate = QtCore.QCoreApplication.translate
        ConsultarStock.setWindowTitle(_translate("ConsultarStock", "Ezequiel"))
        self.label.setText(_translate("ConsultarStock", "CONSULTAR STOCK"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ConsultarStock", "NOMBRE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ConsultarStock", "CANTIDAD"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ConsultarStock", "STOCK MINIMO"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ConsultarStock", "STOCK MÁXIMO"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ConsultarStock", "PRECIO"))
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
