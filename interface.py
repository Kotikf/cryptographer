# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.15.9


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from decryption import Decryption
from encryption import Encryption



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Folder = QtWidgets.QPushButton(self.centralwidget)
        self.Folder.setGeometry(QtCore.QRect(20, 40, 91, 23))
        self.Folder.setStyleSheet("QPushButton:hover {\n"
"    background-color:rgb(213, 215, 245)\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 1.5px solid rgb(225, 225, 225)\n"
"}\n"
"")
        self.Folder.setObjectName("Folder")
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(120, 40, 350, 23))
        self.path.setObjectName("lineEdit")
        self.lable = QtWidgets.QLabel(self.centralwidget)
        self.lable.setGeometry(QtCore.QRect(20, 80, 91, 23))
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(120, 80, 200, 23))
        self.decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt.setGeometry(QtCore.QRect(20, 120, 91, 23))
        self.decrypt.setStyleSheet("QPushButton:hover {\n"
"    background-color:rgb(213, 215, 245)\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 1.5px solid rgb(225, 225, 225)\n"
"}\n"
"")
        self.decrypt.setObjectName("decrypt")
        self.encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt.setGeometry(QtCore.QRect(120, 120, 91, 23))
        self.encrypt.setStyleSheet("QPushButton:hover {\n"
"    background-color:rgb(213, 215, 245)\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 1.5px solid rgb(225, 225, 225)\n"
"}\n"
"")
        self.encrypt.setObjectName("encrypt")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Folder.clicked.connect(self.get_path_folder)
        self.encrypt.clicked.connect(self.encrypt_file)
        self.decrypt.clicked.connect(self.decrypt_file)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Folder.setText(_translate("MainWindow", "выбрать папку"))
        self.decrypt.setText(_translate("MainWindow", "Расшифровать"))
        self.encrypt.setText(_translate("MainWindow", "Зашифровать"))
        self.lable.setText('Введите пароль')

    def get_path_folder(self):
        self.path.setText(QFileDialog.getExistingDirectory(None, 'Open directory', './'))

    def get_password(self):
            password = self.password_input.text().strip()
            if len(password) <= 3:
                error = QMessageBox()
                error.setWindowTitle('Слишком короткий пароль')
                error.setText('Минимальная длина пароля - 4 символа')
                error.setIcon(QMessageBox.Warning)

                error.exec_()
            if len(password) > 3:
                return password


    def decrypt_file(self):
        try:
            password = self.get_password()
            Decryption().walking_by_dirs(dir=self.path.text(), password=password)
        except FileNotFoundError:
            error = QMessageBox()
            error.setWindowTitle('Неверный путь')
            error.setText('Файл не существует или путь указан с ошибками')
            error.setIcon(QMessageBox.Warning)

            error.exec_()

    def encrypt_file(self):
        try:
            password = self.get_password()
            Encryption().walking_by_dirs(dir=self.path.text(), password=password)
        except FileNotFoundError:
            error = QMessageBox()
            error.setWindowTitle('Неверный путь')
            error.setText('Файл не существует или путь указан с ошибками')
            error.setIcon(QMessageBox.Warning)

            error.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
