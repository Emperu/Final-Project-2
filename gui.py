from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Logic):
        self.logic = Logic
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 300)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Submit.setGeometry(QtCore.QRect(40, 200, 113, 32))
        self.pushButton_Submit.setObjectName("pushButton_Submit")
        self.pushButton_Submit.clicked.connect(Logic.submit)
        self.lineEdit_student_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_student_name.setGeometry(QtCore.QRect(110, 10, 113, 21))
        self.lineEdit_student_name.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_attempts = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_attempts.setGeometry(QtCore.QRect(110, 40, 113, 21))
        self.lineEdit_attempts.setObjectName("lineEdit_attempts")
        self.lineEdit_attempts.textChanged.connect(self.logic.attemptCountChange)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.submit_status_label = QtWidgets.QLabel(self.centralwidget)
        self.submit_status_label.setGeometry(QtCore.QRect(40, 240, 113, 32))  # Adjust position and size as needed
        self.submit_status_label.setObjectName("submit_status_label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.scoreLineEdits = []
        self.scoreLabels = []



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Submit.setText(_translate("MainWindow", "SUBMIT"))
        self.label.setText(_translate("MainWindow", "Student name:"))
        self.label_2.setText(_translate("MainWindow", "# of attempts:"))



