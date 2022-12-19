# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1354, 708)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imag/invest.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{background-color: rgb(208, 201, 196);}\n"
"\n"
"QPushButton {\n"
"    color: #eff0f1;\n"
"    background-color: #31363b;\n"
"    border-width: 1px;\n"
"    border-color: #76797C;\n"
"    border-style: solid;\n"
"    padding: 5px;\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #31363b;\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton :focus,\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(48, 97, 145);\n"
"    color: rgb(210, 170, 108);\n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(53, 159, 159);\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #76797C;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color : #31363b;\n"
"border:2px solid #ffffff;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QGroupBox{border-style: solid;\n"
"  border-width: 3px;}\n"
"/*for table*/\n"
"QHeaderView::section {\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(260, 0, 1061, 651))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.label = QtWidgets.QLabel(self.tab_14)
        self.label.setGeometry(QtCore.QRect(-4, -48, 1061, 701))
        self.label.setStyleSheet("image: url(:/imag/h3.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.tab_14)
        self.groupBox.setGeometry(QtCore.QRect(210, 150, 661, 311))
        self.groupBox.setStyleSheet("background-color: rgb(208, 201, 196);\n"
"border-radius: 25px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_16.setGeometry(QtCore.QRect(170, 120, 361, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_16.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_11.setGeometry(QtCore.QRect(170, 40, 361, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("image: url(:/imag/pass.png);\n"
"border:null;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_21.setGeometry(QtCore.QRect(110, 220, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_21.setStyleSheet("QPushButton { background: #188c4a;\n"
"  background-image: -webkit-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -moz-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -ms-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -o-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: linear-gradient(to bottom, #188c4a, #0f5928);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 15px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background: #003800;\n"
"    \n"
"  background-image: -webkit-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -moz-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -ms-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -o-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: linear-gradient(to bottom, #1e47eb, #1436de);\n"
"  text-decoration: none;\n"
"}\n"
"")
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(60, 40, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("image: url(:/imag/username.png);\n"
"border:null;\n"
"QLable{rgb(0, 0, 0)};\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_27.setGeometry(QtCore.QRect(350, 220, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton { background: #188c4a;\n"
"  background-image: -webkit-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -moz-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -ms-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -o-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: linear-gradient(to bottom, #188c4a, #0f5928);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 15px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background: #003800;\n"
"  background-image: -webkit-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -moz-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -ms-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -o-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: linear-gradient(to bottom, #1e47eb, #1436de);\n"
"  text-decoration: none;\n"
"}\n"
"")
        self.pushButton_27.setObjectName("pushButton_27")
        self.tabWidget.addTab(self.tab_14, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.label_4 = QtWidgets.QLabel(self.tab_13)
        self.label_4.setGeometry(QtCore.QRect(-10, -50, 1061, 701))
        self.label_4.setStyleSheet("image: url(:/imag/h3.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.groupBox_21 = QtWidgets.QGroupBox(self.tab_13)
        self.groupBox_21.setGeometry(QtCore.QRect(200, 140, 661, 311))
        self.groupBox_21.setStyleSheet("background-color: rgb(208, 201, 196);\n"
"border-radius: 25px;")
        self.groupBox_21.setTitle("")
        self.groupBox_21.setObjectName("groupBox_21")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_21)
        self.lineEdit_20.setGeometry(QtCore.QRect(180, 50, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox_21)
        self.pushButton_28.setGeometry(QtCore.QRect(220, 250, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_28.setStyleSheet("QPushButton { background: #188c4a;\n"
"  background-image: -webkit-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -moz-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -ms-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -o-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: linear-gradient(to bottom, #188c4a, #0f5928);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 15px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background: #003800;\n"
"  background-image: -webkit-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -moz-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -ms-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -o-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: linear-gradient(to bottom, #1e47eb, #1436de);\n"
"  text-decoration: none;\n"
"}\n"
"")
        self.pushButton_28.setObjectName("pushButton_28")
        self.groupBox_22 = QtWidgets.QGroupBox(self.groupBox_21)
        self.groupBox_22.setGeometry(QtCore.QRect(70, 160, 491, 61))
        self.groupBox_22.setTitle("")
        self.groupBox_22.setObjectName("groupBox_22")
        self.label_15 = QtWidgets.QLabel(self.groupBox_22)
        self.label_15.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(109, 109, 109);\n"
"border:null")
        self.label_15.setObjectName("label_15")
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_22)
        self.pushButton_30.setGeometry(QtCore.QRect(180, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("QPushButton { background: #188c4a;\n"
"  background-image: -webkit-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -moz-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -ms-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -o-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: linear-gradient(to bottom, #188c4a, #0f5928);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 15px;\n"
"  \n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background: #003800;\n"
"  background-image: -webkit-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -moz-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -ms-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -o-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: linear-gradient(to bottom, #1e47eb, #1436de);\n"
"  text-decoration: none;\n"
"}\n"
"")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.groupBox_22)
        self.pushButton_31.setGeometry(QtCore.QRect(320, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("QPushButton { background: #188c4a;\n"
"  background-image: -webkit-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -moz-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -ms-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -o-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: linear-gradient(to bottom, #188c4a, #0f5928);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 15px;\n"
" \n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background: #003800;\n"
"  background-image: -webkit-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -moz-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -ms-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -o-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: linear-gradient(to bottom, #1e47eb, #1436de);\n"
"  text-decoration: none;\n"
"}\n"
"")
        self.pushButton_31.setObjectName("pushButton_31")
        self.label_5 = QtWidgets.QLabel(self.groupBox_21)
        self.label_5.setGeometry(QtCore.QRect(60, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:none")
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_13, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 10, 1101, 611))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("QTabWidget{\n"
"\n"
"background:none repeat 0 0 rgb(255, 255, 255);\n"
"\n"
"}")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_20 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_20.setGeometry(QtCore.QRect(30, 50, 931, 411))
        self.groupBox_20.setTitle("")
        self.groupBox_20.setObjectName("groupBox_20")
        self.label_11 = QtWidgets.QLabel(self.groupBox_20)
        self.label_11.setGeometry(QtCore.QRect(350, 10, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border:none;")
        self.label_11.setObjectName("label_11")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_20)
        self.comboBox_7.setGeometry(QtCore.QRect(150, 110, 231, 41))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.label_12 = QtWidgets.QLabel(self.groupBox_20)
        self.label_12.setGeometry(QtCore.QRect(20, 110, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_20)
        self.label_13.setGeometry(QtCore.QRect(480, 110, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_20)
        self.comboBox_8.setGeometry(QtCore.QRect(610, 110, 231, 41))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_20)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 240, 111, 41))
        self.pushButton_2.setStyleSheet("QPushButton { background: #188c4a;\n"
"  background-image: -webkit-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -moz-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -ms-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -o-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: linear-gradient(to bottom, #188c4a, #0f5928);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 20px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background: #1e47eb;\n"
"  background-image: -webkit-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -moz-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -ms-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -o-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: linear-gradient(to bottom, #1e47eb, #1436de);\n"
"  text-decoration: none;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_20)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 170, 511, 221))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("border:2px solid black")
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setGeometry(QtCore.QRect(420, 500, 181, 41))
        self.pushButton_12.setStyleSheet("QPushButton { background: #188c4a;\n"
"  background-image: -webkit-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -moz-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -ms-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: -o-linear-gradient(top, #188c4a, #0f5928);\n"
"  background-image: linear-gradient(to bottom, #188c4a, #0f5928);\n"
"  -webkit-border-radius: 28;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 20px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background: #1e47eb;\n"
"  background-image: -webkit-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -moz-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -ms-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: -o-linear-gradient(top, #1e47eb, #1436de);\n"
"  background-image: linear-gradient(to bottom, #1e47eb, #1436de);\n"
"  text-decoration: none;\n"
"}")
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 10, 1201, 591))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setToolTip("")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.groupBox_11 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 10, 1001, 111))
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 30, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 30, 161, 41))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_12 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 140, 1001, 401))
        self.groupBox_12.setTitle("")
        self.groupBox_12.setObjectName("groupBox_12")
        self.pushButton_40 = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_40.setGeometry(QtCore.QRect(500, 350, 151, 31))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_41.setGeometry(QtCore.QRect(680, 350, 161, 31))
        self.pushButton_41.setObjectName("pushButton_41")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_12)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 20, 961, 321))
        self.tableWidget_2.setStyleSheet("QHeaderView::section {\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}")
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(129)
        self.tabWidget_3.addTab(self.widget, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 20, 1031, 501))
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_7.setGeometry(QtCore.QRect(380, 400, 271, 41))
        self.pushButton_7.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imag/plu.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 30, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_37 = QtWidgets.QLabel(self.groupBox_10)
        self.label_37.setGeometry(QtCore.QRect(40, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        self.label_37.setObjectName("label_37")
        self.label_35 = QtWidgets.QLabel(self.groupBox_10)
        self.label_35.setGeometry(QtCore.QRect(40, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("")
        self.label_35.setObjectName("label_35")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_9.setGeometry(QtCore.QRect(200, 210, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_36 = QtWidgets.QLabel(self.groupBox_10)
        self.label_36.setGeometry(QtCore.QRect(40, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setObjectName("label_36")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_8.setGeometry(QtCore.QRect(200, 270, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_38 = QtWidgets.QLabel(self.groupBox_10)
        self.label_38.setGeometry(QtCore.QRect(40, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("")
        self.label_38.setObjectName("label_38")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_2.setGeometry(QtCore.QRect(440, 330, 141, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_68 = QtWidgets.QLabel(self.groupBox_10)
        self.label_68.setGeometry(QtCore.QRect(330, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_68.setFont(font)
        self.label_68.setStyleSheet("")
        self.label_68.setObjectName("label_68")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_37.setGeometry(QtCore.QRect(200, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_37.setFont(font)
        self.lineEdit_37.setText("")
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_67 = QtWidgets.QLabel(self.groupBox_10)
        self.label_67.setGeometry(QtCore.QRect(40, 330, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("")
        self.label_67.setObjectName("label_67")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_10)
        self.textEdit_2.setGeometry(QtCore.QRect(600, 30, 411, 331))
        self.textEdit_2.setObjectName("textEdit_2")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_10)
        self.dateEdit.setGeometry(QtCore.QRect(200, 150, 121, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.label_45 = QtWidgets.QLabel(self.groupBox_10)
        self.label_45.setGeometry(QtCore.QRect(40, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("")
        self.label_45.setObjectName("label_45")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 90, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 20, 971, 101))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(57, 31, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_9.setGeometry(QtCore.QRect(480, 30, 271, 41))
        self.pushButton_9.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imag/sear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_4.setGeometry(QtCore.QRect(40, 140, 971, 401))
        self.groupBox_4.setStyleSheet("")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setGeometry(QtCore.QRect(530, 330, 161, 41))
        self.pushButton_10.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imag/ar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_41 = QtWidgets.QLabel(self.groupBox_4)
        self.label_41.setGeometry(QtCore.QRect(28, 219, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("")
        self.label_41.setObjectName("label_41")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(488, 10, 471, 291))
        self.textEdit.setObjectName("textEdit")
        self.label_40 = QtWidgets.QLabel(self.groupBox_4)
        self.label_40.setGeometry(QtCore.QRect(28, 169, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("")
        self.label_40.setObjectName("label_40")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 330, 171, 41))
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_69 = QtWidgets.QLabel(self.groupBox_4)
        self.label_69.setGeometry(QtCore.QRect(290, 270, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_69.setFont(font)
        self.label_69.setStyleSheet("")
        self.label_69.setObjectName("label_69")
        self.label_39 = QtWidgets.QLabel(self.groupBox_4)
        self.label_39.setGeometry(QtCore.QRect(28, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("")
        self.label_39.setObjectName("label_39")
        self.label_44 = QtWidgets.QLabel(self.groupBox_4)
        self.label_44.setGeometry(QtCore.QRect(28, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("")
        self.label_44.setObjectName("label_44")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(160, 169, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_39.setGeometry(QtCore.QRect(158, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_39.setFont(font)
        self.lineEdit_39.setText("")
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.label_70 = QtWidgets.QLabel(self.groupBox_4)
        self.label_70.setGeometry(QtCore.QRect(28, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_70.setFont(font)
        self.label_70.setStyleSheet("")
        self.label_70.setObjectName("label_70")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(160, 219, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(160, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_4.setGeometry(QtCore.QRect(380, 270, 91, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox_4)
        self.dateEdit_2.setGeometry(QtCore.QRect(160, 119, 121, 31))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_35.setGeometry(QtCore.QRect(160, 70, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_35.setFont(font)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.label_61 = QtWidgets.QLabel(self.groupBox_4)
        self.label_61.setGeometry(QtCore.QRect(30, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("")
        self.label_61.setObjectName("label_61")
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_4.setGeometry(QtCore.QRect(-4, 9, 1051, 621))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.tabWidget_4.setFont(font)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_8.setGeometry(QtCore.QRect(40, 10, 931, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.groupBox_8.setFont(font)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 30, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_15.setGeometry(QtCore.QRect(500, 30, 161, 41))
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_9.setGeometry(QtCore.QRect(40, 140, 931, 401))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.groupBox_9)
        self.tableWidget_4.setGeometry(QtCore.QRect(30, 20, 871, 301))
        self.tableWidget_4.setStyleSheet("QHeaderView::section {\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}")
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(169)
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_17.setGeometry(QtCore.QRect(500, 340, 151, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_18.setGeometry(QtCore.QRect(690, 340, 161, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.tabWidget_4.addTab(self.tab_7, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_11)
        self.groupBox_5.setGeometry(QtCore.QRect(40, 30, 971, 531))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_32.setGeometry(QtCore.QRect(200, 240, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.label_29 = QtWidgets.QLabel(self.groupBox_5)
        self.label_29.setGeometry(QtCore.QRect(40, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("")
        self.label_29.setObjectName("label_29")
        self.label_51 = QtWidgets.QLabel(self.groupBox_5)
        self.label_51.setGeometry(QtCore.QRect(40, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("")
        self.label_51.setObjectName("label_51")
        self.label_53 = QtWidgets.QLabel(self.groupBox_5)
        self.label_53.setGeometry(QtCore.QRect(40, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("")
        self.label_53.setObjectName("label_53")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_29.setGeometry(QtCore.QRect(200, 60, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_16.setGeometry(QtCore.QRect(140, 400, 161, 41))
        self.pushButton_16.setObjectName("pushButton_16")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_30.setGeometry(QtCore.QRect(200, 300, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setGeometry(QtCore.QRect(200, 180, 301, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_52 = QtWidgets.QLabel(self.groupBox_5)
        self.label_52.setGeometry(QtCore.QRect(40, 240, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("")
        self.label_52.setObjectName("label_52")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(520, 60, 331, 311))
        self.label_6.setStyleSheet("background-image: url(:/imag/doctor.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_36.setGeometry(QtCore.QRect(200, 120, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_36.setFont(font)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.label_62 = QtWidgets.QLabel(self.groupBox_5)
        self.label_62.setGeometry(QtCore.QRect(40, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("")
        self.label_62.setObjectName("label_62")
        self.tabWidget_4.addTab(self.tab_11, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_10)
        self.groupBox_6.setGeometry(QtCore.QRect(40, 140, 971, 421))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_54 = QtWidgets.QLabel(self.groupBox_6)
        self.label_54.setGeometry(QtCore.QRect(30, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("")
        self.label_54.setObjectName("label_54")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_13.setGeometry(QtCore.QRect(330, 360, 151, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_3.setGeometry(QtCore.QRect(200, 160, 301, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_28.setGeometry(QtCore.QRect(200, 220, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_28.setFont(font)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.label_27 = QtWidgets.QLabel(self.groupBox_6)
        self.label_27.setGeometry(QtCore.QRect(30, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("")
        self.label_27.setObjectName("label_27")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_27.setGeometry(QtCore.QRect(200, 280, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_27.setFont(font)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_14.setGeometry(QtCore.QRect(110, 360, 161, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_26.setGeometry(QtCore.QRect(200, 40, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label_24 = QtWidgets.QLabel(self.groupBox_6)
        self.label_24.setGeometry(QtCore.QRect(30, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("")
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(self.groupBox_6)
        self.label_26.setGeometry(QtCore.QRect(30, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("")
        self.label_26.setObjectName("label_26")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(530, 30, 411, 331))
        self.label_7.setStyleSheet("background-image: url(:/imag/do.jpg);\n"
"background-image: url(:/imag/doctor.jpg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_42.setGeometry(QtCore.QRect(200, 100, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.label_63 = QtWidgets.QLabel(self.groupBox_6)
        self.label_63.setGeometry(QtCore.QRect(30, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("")
        self.label_63.setObjectName("label_63")
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_10)
        self.groupBox_13.setGeometry(QtCore.QRect(40, 10, 971, 101))
        self.groupBox_13.setTitle("")
        self.groupBox_13.setObjectName("groupBox_13")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_18.setGeometry(QtCore.QRect(37, 31, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.pushButton_42 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_42.setGeometry(QtCore.QRect(480, 30, 271, 41))
        self.pushButton_42.setStyleSheet("")
        self.pushButton_42.setIcon(icon2)
        self.pushButton_42.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_42.setObjectName("pushButton_42")
        self.tabWidget_4.addTab(self.tab_10, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_17 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_17.setGeometry(QtCore.QRect(10, 10, 1031, 601))
        self.groupBox_17.setTitle("")
        self.groupBox_17.setObjectName("groupBox_17")
        self.groupBox_19 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_19.setEnabled(True)
        self.groupBox_19.setGeometry(QtCore.QRect(470, 20, 521, 141))
        self.groupBox_19.setStyleSheet("border:2px solid black")
        self.groupBox_19.setTitle("")
        self.groupBox_19.setObjectName("groupBox_19")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_40.setEnabled(False)
        self.lineEdit_40.setGeometry(QtCore.QRect(400, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_40.setFont(font)
        self.lineEdit_40.setText("")
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.groupBox_19)
        self.dateEdit_3.setEnabled(False)
        self.dateEdit_3.setGeometry(QtCore.QRect(400, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_19)
        self.comboBox_5.setGeometry(QtCore.QRect(112, 240, 151, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_21.setEnabled(False)
        self.lineEdit_21.setGeometry(QtCore.QRect(10, 50, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_22.setEnabled(False)
        self.lineEdit_22.setGeometry(QtCore.QRect(10, 90, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_19)
        self.comboBox_6.setEnabled(False)
        self.comboBox_6.setGeometry(QtCore.QRect(400, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_43.setEnabled(False)
        self.lineEdit_43.setGeometry(QtCore.QRect(10, 10, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_43.setFont(font)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_17)
        self.pushButton_11.setGeometry(QtCore.QRect(860, 560, 131, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.groupBox_18 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_18.setGeometry(QtCore.QRect(20, 20, 441, 141))
        self.groupBox_18.setStyleSheet("border:2px solid black")
        self.groupBox_18.setTitle("")
        self.groupBox_18.setObjectName("groupBox_18")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_18)
        self.lineEdit_15.setGeometry(QtCore.QRect(10, 40, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_18)
        self.pushButton_22.setGeometry(QtCore.QRect(330, 40, 101, 41))
        self.pushButton_22.setStyleSheet("")
        self.pushButton_22.setIcon(icon2)
        self.pushButton_22.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_22.setObjectName("pushButton_22")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_17)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 180, 971, 371))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("border:2px solid black")
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.tab_12)
        self.tabWidget_6.setGeometry(QtCore.QRect(0, 10, 1051, 601))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tabWidget_6.setFont(font)
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 1031, 541))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_5.setGeometry(QtCore.QRect(10, 10, 1001, 521))
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, item)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(135)
        self.tabWidget_6.addTab(self.tab_6, "")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.groupBox_32 = QtWidgets.QGroupBox(self.tab_20)
        self.groupBox_32.setGeometry(QtCore.QRect(10, 130, 971, 411))
        self.groupBox_32.setStyleSheet("")
        self.groupBox_32.setTitle("")
        self.groupBox_32.setObjectName("groupBox_32")
        self.label_90 = QtWidgets.QLabel(self.groupBox_32)
        self.label_90.setGeometry(QtCore.QRect(28, 219, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("")
        self.label_90.setObjectName("label_90")
        self.textEdit_10 = QtWidgets.QTextEdit(self.groupBox_32)
        self.textEdit_10.setGeometry(QtCore.QRect(488, 10, 471, 291))
        self.textEdit_10.setObjectName("textEdit_10")
        self.label_91 = QtWidgets.QLabel(self.groupBox_32)
        self.label_91.setGeometry(QtCore.QRect(28, 169, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_91.setFont(font)
        self.label_91.setStyleSheet("")
        self.label_91.setObjectName("label_91")
        self.pushButton_51 = QtWidgets.QPushButton(self.groupBox_32)
        self.pushButton_51.setGeometry(QtCore.QRect(360, 340, 171, 41))
        self.pushButton_51.setStyleSheet("")
        self.pushButton_51.setObjectName("pushButton_51")
        self.label_92 = QtWidgets.QLabel(self.groupBox_32)
        self.label_92.setGeometry(QtCore.QRect(290, 270, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_92.setFont(font)
        self.label_92.setStyleSheet("")
        self.label_92.setObjectName("label_92")
        self.label_93 = QtWidgets.QLabel(self.groupBox_32)
        self.label_93.setGeometry(QtCore.QRect(28, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_93.setFont(font)
        self.label_93.setStyleSheet("")
        self.label_93.setObjectName("label_93")
        self.label_94 = QtWidgets.QLabel(self.groupBox_32)
        self.label_94.setGeometry(QtCore.QRect(28, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_94.setFont(font)
        self.label_94.setStyleSheet("")
        self.label_94.setObjectName("label_94")
        self.lineEdit_62 = QtWidgets.QLineEdit(self.groupBox_32)
        self.lineEdit_62.setGeometry(QtCore.QRect(160, 169, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_62.setFont(font)
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.lineEdit_63 = QtWidgets.QLineEdit(self.groupBox_32)
        self.lineEdit_63.setGeometry(QtCore.QRect(158, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_63.setFont(font)
        self.lineEdit_63.setText("")
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.label_95 = QtWidgets.QLabel(self.groupBox_32)
        self.label_95.setGeometry(QtCore.QRect(28, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_95.setFont(font)
        self.label_95.setStyleSheet("")
        self.label_95.setObjectName("label_95")
        self.lineEdit_64 = QtWidgets.QLineEdit(self.groupBox_32)
        self.lineEdit_64.setGeometry(QtCore.QRect(160, 219, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_64.setFont(font)
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.lineEdit_65 = QtWidgets.QLineEdit(self.groupBox_32)
        self.lineEdit_65.setGeometry(QtCore.QRect(160, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_65.setFont(font)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.comboBox_14 = QtWidgets.QComboBox(self.groupBox_32)
        self.comboBox_14.setGeometry(QtCore.QRect(380, 270, 91, 31))
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.dateEdit_9 = QtWidgets.QDateEdit(self.groupBox_32)
        self.dateEdit_9.setGeometry(QtCore.QRect(160, 119, 121, 31))
        self.dateEdit_9.setObjectName("dateEdit_9")
        self.lineEdit_66 = QtWidgets.QLineEdit(self.groupBox_32)
        self.lineEdit_66.setGeometry(QtCore.QRect(160, 70, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_66.setFont(font)
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.label_96 = QtWidgets.QLabel(self.groupBox_32)
        self.label_96.setGeometry(QtCore.QRect(30, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_96.setFont(font)
        self.label_96.setStyleSheet("")
        self.label_96.setObjectName("label_96")
        self.groupBox_33 = QtWidgets.QGroupBox(self.tab_20)
        self.groupBox_33.setGeometry(QtCore.QRect(10, 10, 971, 101))
        self.groupBox_33.setTitle("")
        self.groupBox_33.setObjectName("groupBox_33")
        self.lineEdit_67 = QtWidgets.QLineEdit(self.groupBox_33)
        self.lineEdit_67.setGeometry(QtCore.QRect(57, 31, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_67.setFont(font)
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.pushButton_52 = QtWidgets.QPushButton(self.groupBox_33)
        self.pushButton_52.setGeometry(QtCore.QRect(480, 30, 271, 41))
        self.pushButton_52.setStyleSheet("")
        self.pushButton_52.setIcon(icon2)
        self.pushButton_52.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_52.setObjectName("pushButton_52")
        self.tabWidget_6.addTab(self.tab_20, "")
        self.tabWidget.addTab(self.tab_12, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_15)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, 0, 1101, 611))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.tabWidget_5.setFont(font)
        self.tabWidget_5.setStyleSheet("QTabWidget{\n"
"\n"
"background:none repeat 0 0 rgb(255, 255, 255);\n"
"\n"
"}")
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_47 = QtWidgets.QWidget()
        self.tab_47.setObjectName("tab_47")
        self.groupBox_50 = QtWidgets.QGroupBox(self.tab_47)
        self.groupBox_50.setGeometry(QtCore.QRect(20, 60, 481, 371))
        self.groupBox_50.setTitle("")
        self.groupBox_50.setObjectName("groupBox_50")
        self.lineEdit_82 = QtWidgets.QLineEdit(self.groupBox_50)
        self.lineEdit_82.setGeometry(QtCore.QRect(160, 130, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_82.setFont(font)
        self.lineEdit_82.setObjectName("lineEdit_82")
        self.label_128 = QtWidgets.QLabel(self.groupBox_50)
        self.label_128.setGeometry(QtCore.QRect(20, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_128.setFont(font)
        self.label_128.setStyleSheet("")
        self.label_128.setObjectName("label_128")
        self.lineEdit_83 = QtWidgets.QLineEdit(self.groupBox_50)
        self.lineEdit_83.setGeometry(QtCore.QRect(160, 50, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_83.setFont(font)
        self.lineEdit_83.setObjectName("lineEdit_83")
        self.label_129 = QtWidgets.QLabel(self.groupBox_50)
        self.label_129.setGeometry(QtCore.QRect(20, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_129.setFont(font)
        self.label_129.setStyleSheet("")
        self.label_129.setObjectName("label_129")
        self.pushButton_104 = QtWidgets.QPushButton(self.groupBox_50)
        self.pushButton_104.setGeometry(QtCore.QRect(120, 230, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_104.setFont(font)
        self.pushButton_104.setStyleSheet("")
        self.pushButton_104.setIcon(icon1)
        self.pushButton_104.setIconSize(QtCore.QSize(70, 43))
        self.pushButton_104.setObjectName("pushButton_104")
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_47)
        self.groupBox_16.setGeometry(QtCore.QRect(530, 60, 491, 371))
        self.groupBox_16.setTitle("")
        self.groupBox_16.setObjectName("groupBox_16")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.groupBox_16)
        self.tableWidget_6.setGeometry(QtCore.QRect(20, 50, 451, 311))
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.setColumnCount(2)
        self.tableWidget_6.setObjectName("tableWidget_6")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(151)
        self.tableWidget_6.horizontalHeader().setMinimumSectionSize(43)
        self.label_3 = QtWidgets.QLabel(self.groupBox_16)
        self.label_3.setGeometry(QtCore.QRect(170, 9, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("border:none")
        self.label_3.setObjectName("label_3")
        self.tabWidget_5.addTab(self.tab_47, "")
        self.tab_52 = QtWidgets.QWidget()
        self.tab_52.setObjectName("tab_52")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_52)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 30, 1011, 531))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setFlat(False)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton.setGeometry(QtCore.QRect(440, 80, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_31.setGeometry(QtCore.QRect(50, 70, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setGeometry(QtCore.QRect(620, 60, 351, 341))
        self.label_8.setStyleSheet("background-image: url(:/imag/do.jpg);\n"
"background-image: url(:/imag/doctor.jpg);")
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.tabWidget_5.addTab(self.tab_52, "")
        self.tabWidget.addTab(self.tab_15, "")
        self.groupBox_15 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_15.setEnabled(False)
        self.groupBox_15.setGeometry(QtCore.QRect(-10, 10, 261, 641))
        self.groupBox_15.setStyleSheet("  border: 2px solid black;")
        self.groupBox_15.setTitle("")
        self.groupBox_15.setObjectName("groupBox_15")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton_20.setGeometry(QtCore.QRect(30, 14, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton:focus {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;}\n"
"\n"
"QPushButton:pressed {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;\n"
"}")
        self.pushButton_20.setIcon(icon)
        self.pushButton_20.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton_26.setGeometry(QtCore.QRect(70, 570, 121, 41))
        self.pushButton_26.setStyleSheet("QPushButton:focus {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;}\n"
"\n"
"QPushButton:pressed {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imag/pass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_26.setIcon(icon4)
        self.pushButton_26.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 194, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton:focus {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;}\n"
"\n"
"QPushButton:pressed {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imag/do.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 374, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton:focus {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;}\n"
"\n"
"QPushButton:pressed {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imag/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton_19.setGeometry(QtCore.QRect(30, 104, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton:focus {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;}\n"
"\n"
"QPushButton:pressed {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/imag/patient.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon7)
        self.pushButton_19.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_39 = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton_39.setGeometry(QtCore.QRect(30, 280, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setStyleSheet("QPushButton:focus {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;}\n"
"\n"
"QPushButton:pressed {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/imag/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_39.setIcon(icon8)
        self.pushButton_39.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton_29.setGeometry(QtCore.QRect(30, 470, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("QPushButton:focus {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;}\n"
"\n"
"QPushButton:pressed {\n"
"     background: #10730b;\n"
"  background-image: -webkit-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -moz-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -ms-linear-gradient(top, #10730b, #146108);\n"
"  background-image: -o-linear-gradient(top, #10730b, #146108);\n"
"  background-image: linear-gradient(to bottom, #10730b, #146108);\n"
"  text-decoration: none;\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/imag/setting.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_29.setIcon(icon9)
        self.pushButton_29.setIconSize(QtCore.QSize(44, 37))
        self.pushButton_29.setObjectName("pushButton_29")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1354, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(1)
        self.tabWidget_6.setCurrentIndex(1)
        self.tabWidget_5.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EndScop"))
        self.lineEdit_16.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "Enter User Name "))
        self.pushButton_21.setText(_translate("MainWindow", "Login "))
        self.pushButton_27.setText(_translate("MainWindow", "Reset password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), _translate("MainWindow", "Page"))
        self.lineEdit_20.setPlaceholderText(_translate("MainWindow", "Enter User Mail "))
        self.pushButton_28.setText(_translate("MainWindow", "Send Me On Gmail  "))
        self.label_15.setText(_translate("MainWindow", "Login from here"))
        self.pushButton_30.setText(_translate("MainWindow", "Reset Mail"))
        self.pushButton_31.setText(_translate("MainWindow", "Login"))
        self.label_5.setText(_translate("MainWindow", "Enter yor Mail"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("MainWindow", "Page"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>Information of Investigation</p></body></html>"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "-----------------------------------------------------------------------"))
        self.label_12.setText(_translate("MainWindow", "choose patient"))
        self.label_13.setText(_translate("MainWindow", "choose doctor"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "-----------------------------------------------------------------------"))
        self.pushButton_2.setText(_translate("MainWindow", "Add"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "Notification for investigation"))
        self.pushButton_12.setText(_translate("MainWindow", "open Camera"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "investigation "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "patient national Id"))
        self.pushButton_4.setText(_translate("MainWindow", "Search"))
        self.pushButton_40.setText(_translate("MainWindow", "Import"))
        self.pushButton_41.setText(_translate("MainWindow", "Export"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "National Id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Age"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Phone "))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Surgery Date"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.widget), _translate("MainWindow", "All Patient"))
        self.pushButton_7.setText(_translate("MainWindow", "Add Patient"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Patient Name "))
        self.label_37.setText(_translate("MainWindow", "Patient Name"))
        self.label_35.setText(_translate("MainWindow", "Surgery Date"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "Enter Phone Number"))
        self.label_36.setText(_translate("MainWindow", "Phone Number"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "Enter  The Address"))
        self.label_38.setText(_translate("MainWindow", "Address"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Female"))
        self.label_68.setText(_translate("MainWindow", "Gender"))
        self.lineEdit_37.setPlaceholderText(_translate("MainWindow", "Enter  age"))
        self.label_67.setText(_translate("MainWindow", "Age"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Enter the discription"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.label_45.setText(_translate("MainWindow", "National Id"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Patient National Id "))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "Add Patient"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Enter ptient national Id"))
        self.pushButton_9.setText(_translate("MainWindow", "Search"))
        self.pushButton_10.setText(_translate("MainWindow", "Archive"))
        self.label_41.setText(_translate("MainWindow", "Address"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter the Discription"))
        self.label_40.setText(_translate("MainWindow", "Phone Number"))
        self.pushButton_8.setText(_translate("MainWindow", "Edit Patient"))
        self.label_69.setText(_translate("MainWindow", "Gender"))
        self.label_39.setText(_translate("MainWindow", "Date of Surgery"))
        self.label_44.setText(_translate("MainWindow", "Patient Name"))
        self.lineEdit_14.setPlaceholderText(_translate("MainWindow", "Enter the Number"))
        self.lineEdit_39.setPlaceholderText(_translate("MainWindow", "Enter  age"))
        self.label_70.setText(_translate("MainWindow", "Age"))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", "Enter Address"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "Enter Name"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Female"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.lineEdit_35.setPlaceholderText(_translate("MainWindow", "Patient National Id "))
        self.label_61.setText(_translate("MainWindow", "National Id"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Edit / Archive "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Doctor national Id"))
        self.pushButton_15.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "National Id"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Doctor Name"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phone number"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Doctor Address"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "specialization"))
        self.pushButton_17.setText(_translate("MainWindow", "Import"))
        self.pushButton_18.setText(_translate("MainWindow", "Export"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), _translate("MainWindow", "All Doctors"))
        self.lineEdit_32.setPlaceholderText(_translate("MainWindow", "Enter Phone Number"))
        self.label_29.setText(_translate("MainWindow", "Doctor Address"))
        self.label_51.setText(_translate("MainWindow", "Doctor Name"))
        self.label_53.setText(_translate("MainWindow", "Specialization"))
        self.lineEdit_29.setPlaceholderText(_translate("MainWindow", "Doctor Name "))
        self.pushButton_16.setText(_translate("MainWindow", "Add"))
        self.lineEdit_30.setPlaceholderText(_translate("MainWindow", "Enter  The Address"))
        self.label_52.setText(_translate("MainWindow", "Phone Number"))
        self.lineEdit_36.setPlaceholderText(_translate("MainWindow", "Doctor National Id "))
        self.label_62.setText(_translate("MainWindow", "National Id"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), _translate("MainWindow", "Add Doctor"))
        self.label_54.setText(_translate("MainWindow", "Specialization"))
        self.pushButton_13.setText(_translate("MainWindow", "Delete"))
        self.lineEdit_28.setPlaceholderText(_translate("MainWindow", "Enter Phone Number"))
        self.label_27.setText(_translate("MainWindow", "Doctor Name"))
        self.lineEdit_27.setPlaceholderText(_translate("MainWindow", "Enter  The Address"))
        self.pushButton_14.setText(_translate("MainWindow", "Edit"))
        self.lineEdit_26.setPlaceholderText(_translate("MainWindow", "Doctor Name "))
        self.label_24.setText(_translate("MainWindow", "Doctor Address"))
        self.label_26.setText(_translate("MainWindow", "Phone Number"))
        self.lineEdit_42.setPlaceholderText(_translate("MainWindow", "Doctor National Id "))
        self.label_63.setText(_translate("MainWindow", "National Id"))
        self.lineEdit_18.setPlaceholderText(_translate("MainWindow", "Doctor National Id"))
        self.pushButton_42.setText(_translate("MainWindow", "Search"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), _translate("MainWindow", "Edit /Delete "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.lineEdit_40.setPlaceholderText(_translate("MainWindow", "paient  age"))
        self.dateEdit_3.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Female"))
        self.lineEdit_21.setPlaceholderText(_translate("MainWindow", "Phone Number"))
        self.lineEdit_22.setPlaceholderText(_translate("MainWindow", "patient Address"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Female"))
        self.lineEdit_43.setPlaceholderText(_translate("MainWindow", "patient Name"))
        self.pushButton_11.setText(_translate("MainWindow", "Export"))
        self.lineEdit_15.setPlaceholderText(_translate("MainWindow", "Enter Patient National Id"))
        self.pushButton_22.setText(_translate("MainWindow", "Search"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "description of report"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nationa Id"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Age"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "gender"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Surgery Date"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Phone "))
        item = self.tableWidget_5.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Address"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_6), _translate("MainWindow", "Patients Archive"))
        self.label_90.setText(_translate("MainWindow", "Address"))
        self.textEdit_10.setPlaceholderText(_translate("MainWindow", "Enter the Discription"))
        self.label_91.setText(_translate("MainWindow", "Phone Number"))
        self.pushButton_51.setText(_translate("MainWindow", "Return"))
        self.label_92.setText(_translate("MainWindow", "Gender"))
        self.label_93.setText(_translate("MainWindow", "Date of Surgery"))
        self.label_94.setText(_translate("MainWindow", "Patient Name"))
        self.lineEdit_62.setPlaceholderText(_translate("MainWindow", "Enter the Number"))
        self.lineEdit_63.setPlaceholderText(_translate("MainWindow", "Enter  age"))
        self.label_95.setText(_translate("MainWindow", "Age"))
        self.lineEdit_64.setPlaceholderText(_translate("MainWindow", "Enter Address"))
        self.lineEdit_65.setPlaceholderText(_translate("MainWindow", "Enter Name"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "Female"))
        self.dateEdit_9.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.lineEdit_66.setPlaceholderText(_translate("MainWindow", "Patient National Id "))
        self.label_96.setText(_translate("MainWindow", "National Id"))
        self.lineEdit_67.setPlaceholderText(_translate("MainWindow", "Enter ptient national Id"))
        self.pushButton_52.setText(_translate("MainWindow", "Search"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_20), _translate("MainWindow", "Patient Return"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "Page"))
        self.lineEdit_82.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.label_128.setText(_translate("MainWindow", "Password"))
        self.lineEdit_83.setPlaceholderText(_translate("MainWindow", "Enter User-name "))
        self.label_129.setText(_translate("MainWindow", "User Name"))
        self.pushButton_104.setText(_translate("MainWindow", "Add Administrative"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User Name"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "All Administrative"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_47), _translate("MainWindow", "Add_admin"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.lineEdit_31.setPlaceholderText(_translate("MainWindow", "Specialization Name"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_52), _translate("MainWindow", "Add Sepecialization"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), _translate("MainWindow", "setting"))
        self.pushButton_20.setText(_translate("MainWindow", "INVESTIGATION"))
        self.pushButton_26.setText(_translate("MainWindow", "Logout"))
        self.pushButton_5.setText(_translate("MainWindow", "      DOCTORS"))
        self.pushButton_6.setText(_translate("MainWindow", "   Archive"))
        self.pushButton_19.setText(_translate("MainWindow", "         PATIENT"))
        self.pushButton_39.setText(_translate("MainWindow", "      Report"))
        self.pushButton_29.setText(_translate("MainWindow", "setting  "))


import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

