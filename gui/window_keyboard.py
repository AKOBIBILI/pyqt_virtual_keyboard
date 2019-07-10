# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_keyboard.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 462)
        MainWindow.setStyleSheet("background-color: rgb(239, 235, 231);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6.addWidget(self.widget_5)
        self.edit_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_text.sizePolicy().hasHeightForWidth())
        self.edit_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_text.setFont(font)
        self.edit_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_text.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_text.setObjectName("edit_text")
        self.horizontalLayout_6.addWidget(self.edit_text)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6.addWidget(self.widget_6)
        self.horizontalLayout_6.setStretch(0, 20)
        self.horizontalLayout_6.setStretch(1, 60)
        self.horizontalLayout_6.setStretch(2, 20)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_1.setObjectName("btn_1")
        self.horizontalLayout_3.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_2.setObjectName("btn_2")
        self.horizontalLayout_3.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_3.setObjectName("btn_3")
        self.horizontalLayout_3.addWidget(self.btn_3)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_4.setObjectName("btn_4")
        self.horizontalLayout_3.addWidget(self.btn_4)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_5.setObjectName("btn_5")
        self.horizontalLayout_3.addWidget(self.btn_5)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_6.setObjectName("btn_6")
        self.horizontalLayout_3.addWidget(self.btn_6)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_7.setObjectName("btn_7")
        self.horizontalLayout_3.addWidget(self.btn_7)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_8.setObjectName("btn_8")
        self.horizontalLayout_3.addWidget(self.btn_8)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_9.setObjectName("btn_9")
        self.horizontalLayout_3.addWidget(self.btn_9)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_0.setObjectName("btn_0")
        self.horizontalLayout_3.addWidget(self.btn_0)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 10)
        self.horizontalLayout_3.setStretch(2, 10)
        self.horizontalLayout_3.setStretch(3, 10)
        self.horizontalLayout_3.setStretch(4, 10)
        self.horizontalLayout_3.setStretch(5, 10)
        self.horizontalLayout_3.setStretch(6, 10)
        self.horizontalLayout_3.setStretch(7, 10)
        self.horizontalLayout_3.setStretch(8, 10)
        self.horizontalLayout_3.setStretch(9, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_q = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_q.sizePolicy().hasHeightForWidth())
        self.btn_q.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_q.setFont(font)
        self.btn_q.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_q.setObjectName("btn_q")
        self.horizontalLayout.addWidget(self.btn_q)
        self.btn_w = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_w.sizePolicy().hasHeightForWidth())
        self.btn_w.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_w.setFont(font)
        self.btn_w.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_w.setObjectName("btn_w")
        self.horizontalLayout.addWidget(self.btn_w)
        self.btn_e = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_e.sizePolicy().hasHeightForWidth())
        self.btn_e.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_e.setFont(font)
        self.btn_e.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_e.setObjectName("btn_e")
        self.horizontalLayout.addWidget(self.btn_e)
        self.btn_r = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_r.sizePolicy().hasHeightForWidth())
        self.btn_r.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_r.setFont(font)
        self.btn_r.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_r.setObjectName("btn_r")
        self.horizontalLayout.addWidget(self.btn_r)
        self.btn_t = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_t.sizePolicy().hasHeightForWidth())
        self.btn_t.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_t.setFont(font)
        self.btn_t.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_t.setObjectName("btn_t")
        self.horizontalLayout.addWidget(self.btn_t)
        self.btn_y = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_y.sizePolicy().hasHeightForWidth())
        self.btn_y.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_y.setFont(font)
        self.btn_y.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_y.setObjectName("btn_y")
        self.horizontalLayout.addWidget(self.btn_y)
        self.btn_u = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_u.sizePolicy().hasHeightForWidth())
        self.btn_u.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_u.setFont(font)
        self.btn_u.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_u.setObjectName("btn_u")
        self.horizontalLayout.addWidget(self.btn_u)
        self.btn_i = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_i.sizePolicy().hasHeightForWidth())
        self.btn_i.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_i.setFont(font)
        self.btn_i.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_i.setObjectName("btn_i")
        self.horizontalLayout.addWidget(self.btn_i)
        self.btn_o = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_o.sizePolicy().hasHeightForWidth())
        self.btn_o.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_o.setFont(font)
        self.btn_o.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_o.setObjectName("btn_o")
        self.horizontalLayout.addWidget(self.btn_o)
        self.btn_p = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_p.sizePolicy().hasHeightForWidth())
        self.btn_p.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_p.setFont(font)
        self.btn_p.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_p.setObjectName("btn_p")
        self.horizontalLayout.addWidget(self.btn_p)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 10)
        self.horizontalLayout.setStretch(3, 10)
        self.horizontalLayout.setStretch(4, 10)
        self.horizontalLayout.setStretch(5, 10)
        self.horizontalLayout.setStretch(6, 10)
        self.horizontalLayout.setStretch(7, 10)
        self.horizontalLayout.setStretch(8, 10)
        self.horizontalLayout.setStretch(9, 10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.btn_a = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_a.sizePolicy().hasHeightForWidth())
        self.btn_a.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_a.setFont(font)
        self.btn_a.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_a.setObjectName("btn_a")
        self.horizontalLayout_2.addWidget(self.btn_a)
        self.btn_s = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_s.sizePolicy().hasHeightForWidth())
        self.btn_s.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_s.setFont(font)
        self.btn_s.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_s.setObjectName("btn_s")
        self.horizontalLayout_2.addWidget(self.btn_s)
        self.btn_d = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_d.sizePolicy().hasHeightForWidth())
        self.btn_d.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_d.setFont(font)
        self.btn_d.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_d.setObjectName("btn_d")
        self.horizontalLayout_2.addWidget(self.btn_d)
        self.btn_f = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_f.sizePolicy().hasHeightForWidth())
        self.btn_f.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_f.setFont(font)
        self.btn_f.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_f.setObjectName("btn_f")
        self.horizontalLayout_2.addWidget(self.btn_f)
        self.btn_g = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_g.sizePolicy().hasHeightForWidth())
        self.btn_g.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_g.setFont(font)
        self.btn_g.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_g.setObjectName("btn_g")
        self.horizontalLayout_2.addWidget(self.btn_g)
        self.btn_h = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_h.sizePolicy().hasHeightForWidth())
        self.btn_h.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_h.setFont(font)
        self.btn_h.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_h.setObjectName("btn_h")
        self.horizontalLayout_2.addWidget(self.btn_h)
        self.btn_j = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_j.sizePolicy().hasHeightForWidth())
        self.btn_j.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_j.setFont(font)
        self.btn_j.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_j.setObjectName("btn_j")
        self.horizontalLayout_2.addWidget(self.btn_j)
        self.btn_k = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_k.sizePolicy().hasHeightForWidth())
        self.btn_k.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_k.setFont(font)
        self.btn_k.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_k.setObjectName("btn_k")
        self.horizontalLayout_2.addWidget(self.btn_k)
        self.btn_l = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_l.sizePolicy().hasHeightForWidth())
        self.btn_l.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_l.setFont(font)
        self.btn_l.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_l.setObjectName("btn_l")
        self.horizontalLayout_2.addWidget(self.btn_l)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 10)
        self.horizontalLayout_2.setStretch(3, 10)
        self.horizontalLayout_2.setStretch(4, 10)
        self.horizontalLayout_2.setStretch(5, 10)
        self.horizontalLayout_2.setStretch(6, 10)
        self.horizontalLayout_2.setStretch(7, 10)
        self.horizontalLayout_2.setStretch(8, 10)
        self.horizontalLayout_2.setStretch(9, 10)
        self.horizontalLayout_2.setStretch(10, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5.addWidget(self.widget_3)
        self.btn_z = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_z.sizePolicy().hasHeightForWidth())
        self.btn_z.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_z.setFont(font)
        self.btn_z.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_z.setObjectName("btn_z")
        self.horizontalLayout_5.addWidget(self.btn_z)
        self.btn_x = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_x.sizePolicy().hasHeightForWidth())
        self.btn_x.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_x.setFont(font)
        self.btn_x.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_x.setObjectName("btn_x")
        self.horizontalLayout_5.addWidget(self.btn_x)
        self.btn_c = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_c.setFont(font)
        self.btn_c.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_c.setObjectName("btn_c")
        self.horizontalLayout_5.addWidget(self.btn_c)
        self.btn_v = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_v.sizePolicy().hasHeightForWidth())
        self.btn_v.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_v.setFont(font)
        self.btn_v.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_v.setObjectName("btn_v")
        self.horizontalLayout_5.addWidget(self.btn_v)
        self.btn_b = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_b.sizePolicy().hasHeightForWidth())
        self.btn_b.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_b.setFont(font)
        self.btn_b.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_b.setObjectName("btn_b")
        self.horizontalLayout_5.addWidget(self.btn_b)
        self.btn_n = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_n.sizePolicy().hasHeightForWidth())
        self.btn_n.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_n.setFont(font)
        self.btn_n.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_n.setObjectName("btn_n")
        self.horizontalLayout_5.addWidget(self.btn_n)
        self.btn_m = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_m.sizePolicy().hasHeightForWidth())
        self.btn_m.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_m.setFont(font)
        self.btn_m.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_m.setObjectName("btn_m")
        self.horizontalLayout_5.addWidget(self.btn_m)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.horizontalLayout_5.setStretch(0, 15)
        self.horizontalLayout_5.setStretch(1, 10)
        self.horizontalLayout_5.setStretch(2, 10)
        self.horizontalLayout_5.setStretch(3, 10)
        self.horizontalLayout_5.setStretch(4, 10)
        self.horizontalLayout_5.setStretch(5, 10)
        self.horizontalLayout_5.setStretch(6, 10)
        self.horizontalLayout_5.setStretch(7, 10)
        self.horizontalLayout_5.setStretch(8, 15)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_upper = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_upper.sizePolicy().hasHeightForWidth())
        self.btn_upper.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_upper.setFont(font)
        self.btn_upper.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_upper.setObjectName("btn_upper")
        self.horizontalLayout_4.addWidget(self.btn_upper)
        self.btn_underscore = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_underscore.sizePolicy().hasHeightForWidth())
        self.btn_underscore.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_underscore.setFont(font)
        self.btn_underscore.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_underscore.setObjectName("btn_underscore")
        self.horizontalLayout_4.addWidget(self.btn_underscore)
        self.btn_at = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_at.sizePolicy().hasHeightForWidth())
        self.btn_at.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_at.setFont(font)
        self.btn_at.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_at.setObjectName("btn_at")
        self.horizontalLayout_4.addWidget(self.btn_at)
        self.btn_space = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_space.sizePolicy().hasHeightForWidth())
        self.btn_space.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_space.setFont(font)
        self.btn_space.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_space.setText("")
        self.btn_space.setObjectName("btn_space")
        self.horizontalLayout_4.addWidget(self.btn_space)
        self.btn_period = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_period.sizePolicy().hasHeightForWidth())
        self.btn_period.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_period.setFont(font)
        self.btn_period.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_period.setObjectName("btn_period")
        self.horizontalLayout_4.addWidget(self.btn_period)
        self.btn_backspace = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_backspace.setFont(font)
        self.btn_backspace.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_backspace.setObjectName("btn_backspace")
        self.horizontalLayout_4.addWidget(self.btn_backspace)
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_ok.setFont(font)
        self.btn_ok.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.521, y1:0.8925, x2:0.504, y2:0.244227, stop:0.00847458 rgba(238, 235, 232, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid gray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{    \n"
"    background-color: rgb(140, 223, 255);\n"
" }")
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_4.addWidget(self.btn_ok)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 10)
        self.horizontalLayout_4.setStretch(2, 10)
        self.horizontalLayout_4.setStretch(3, 40)
        self.horizontalLayout_4.setStretch(4, 10)
        self.horizontalLayout_4.setStretch(5, 10)
        self.horizontalLayout_4.setStretch(6, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 15)
        self.verticalLayout.setStretch(1, 17)
        self.verticalLayout.setStretch(2, 17)
        self.verticalLayout.setStretch(3, 17)
        self.verticalLayout.setStretch(4, 17)
        self.verticalLayout.setStretch(5, 17)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AKOBIBILI Virtual Keyboard"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_q.setText(_translate("MainWindow", "q"))
        self.btn_w.setText(_translate("MainWindow", "w"))
        self.btn_e.setText(_translate("MainWindow", "e"))
        self.btn_r.setText(_translate("MainWindow", "r"))
        self.btn_t.setText(_translate("MainWindow", "t"))
        self.btn_y.setText(_translate("MainWindow", "y"))
        self.btn_u.setText(_translate("MainWindow", "u"))
        self.btn_i.setText(_translate("MainWindow", "i"))
        self.btn_o.setText(_translate("MainWindow", "o"))
        self.btn_p.setText(_translate("MainWindow", "p"))
        self.btn_a.setText(_translate("MainWindow", "a"))
        self.btn_s.setText(_translate("MainWindow", "s"))
        self.btn_d.setText(_translate("MainWindow", "d"))
        self.btn_f.setText(_translate("MainWindow", "f"))
        self.btn_g.setText(_translate("MainWindow", "g"))
        self.btn_h.setText(_translate("MainWindow", "h"))
        self.btn_j.setText(_translate("MainWindow", "j"))
        self.btn_k.setText(_translate("MainWindow", "k"))
        self.btn_l.setText(_translate("MainWindow", "l"))
        self.btn_z.setText(_translate("MainWindow", "z"))
        self.btn_x.setText(_translate("MainWindow", "x"))
        self.btn_c.setText(_translate("MainWindow", "c"))
        self.btn_v.setText(_translate("MainWindow", "v"))
        self.btn_b.setText(_translate("MainWindow", "b"))
        self.btn_n.setText(_translate("MainWindow", "n"))
        self.btn_m.setText(_translate("MainWindow", "m"))
        self.btn_upper.setText(_translate("MainWindow", "↑"))
        self.btn_underscore.setText(_translate("MainWindow", "_"))
        self.btn_at.setText(_translate("MainWindow", "@"))
        self.btn_period.setText(_translate("MainWindow", "."))
        self.btn_backspace.setText(_translate("MainWindow", "←"))
        self.btn_ok.setText(_translate("MainWindow", "OK"))

