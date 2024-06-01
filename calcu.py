# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtCore import Qt
import pickle
import os

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(982, 486)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout.addWidget(self.toolButton_3, 0, 2, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_2.addWidget(self.saveButton)

        # Database for item labels
        self.item_labels = {}

        MainWindow1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

        self.toolButton_2.clicked.connect(self.add_item)
        self.toolButton_3.clicked.connect(self.remove_item)
        self.listWidget.itemClicked.connect(self.on_item_clicked)

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.lineEdit.textChanged.connect(self.update_item_text)

        self.saveButton.clicked.connect(self.save_items)

        self.load_items()  # Load items when the application starts

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow1", "GroupBox"))
        self.toolButton_3.setText(_translate("MainWindow1", "Удалить"))
        self.toolButton_2.setText(_translate("MainWindow1", "Добавить"))
        self.label_2.setText(_translate("MainWindow1", "TextLabel"))
        self.saveButton.setText(_translate("MainWindow1", "Сохранить"))

    def on_item_clicked(self, item):
        self.label_2.setText(self.item_labels.get(item.text(), ""))

    def add_item(self):
        new_item_text = self.label_2.text()
        if new_item_text and new_item_text not in self.item_labels:
            self.listWidget.addItem(new_item_text)
            self.item_labels[new_item_text] = "TextLabel"  # Adding label to database

    def remove_item(self):
        current_row = self.listWidget.currentRow()
        if current_row != -1:
            item = self.listWidget.takeItem(current_row)
            if item:
                del self.item_labels[item.text()]

    def update_item_text(self, new_text):
        current_row = self.listWidget.currentRow()
        if current_row != -1:
            current_item = self.listWidget.item(current_row)
            old_text = current_item.text()
            if old_text != new_text:
                current_item.setText(new_text)
                self.item_labels[new_text] = self.item_labels.pop(old_text)

    def save_items(self):
        with open('items.pkl', 'wb') as f:
            pickle.dump(self.item_labels, f)

    def load_items(self):
        if os.path.exists('items.pkl'):
            with open('items.pkl', 'rb') as f:
                self.item_labels = pickle.load(f)
            for item_text in self.item_labels.keys():
                self.listWidget.addItem(item_text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())

