# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'systemdatesetting.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
import re

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget

sys.path.append("..")
from model.Model import *


class Ui_QDialog(QWidget):
    model1 = Model()
    probailities_data = []
    num_people = 0
    time_max = 0
    time_min = 0
    def setupUi(self, QDialog):
        QDialog.setObjectName("QDialog")
        QDialog.resize(567, 496)
        self.label = QtWidgets.QLabel(QDialog)
        self.label.setGeometry(QtCore.QRect(19, 0, 61, 81))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(QDialog)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(QDialog)
        self.label_3.setGeometry(QtCore.QRect(170, 40, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(QDialog)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 16, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(QDialog)
        self.label_5.setGeometry(QtCore.QRect(40, 170, 16, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(QDialog)
        self.label_6.setGeometry(QtCore.QRect(40, 240, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(QDialog)
        self.label_7.setGeometry(QtCore.QRect(40, 310, 16, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(QDialog)
        self.label_8.setGeometry(QtCore.QRect(40, 370, 16, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(QDialog)
        self.label_9.setGeometry(QtCore.QRect(40, 430, 16, 16))
        self.label_9.setObjectName("label_9")

        #PCusSer是输入概率的窗口  CPCusSer是累计概率窗口
        self.PCusSer1 = QtWidgets.QLineEdit(QDialog)
        self.PCusSer1.setGeometry(QtCore.QRect(100, 110, 41, 21))
        self.PCusSer1.setObjectName("PCusSer1")
        self.CPCusSer1 = QtWidgets.QLineEdit(QDialog)
        self.CPCusSer1.setGeometry(QtCore.QRect(180, 110, 41, 21))
        self.CPCusSer1.setReadOnly(True)
        self.CPCusSer1.setObjectName("CPCusSer1")
        self.PCusSer2 = QtWidgets.QLineEdit(QDialog)
        self.PCusSer2.setGeometry(QtCore.QRect(100, 170, 41, 21))
        self.PCusSer2.setObjectName("PCusSer2")
        self.CPCusSer2 = QtWidgets.QLineEdit(QDialog)
        self.CPCusSer2.setGeometry(QtCore.QRect(180, 170, 41, 21))
        self.CPCusSer2.setReadOnly(True)
        self.CPCusSer2.setObjectName("CPCusSer2")
        self.PCusSer3 = QtWidgets.QLineEdit(QDialog)
        self.PCusSer3.setGeometry(QtCore.QRect(100, 240, 41, 21))
        self.PCusSer3.setObjectName("PCusSer3")
        self.CPCusSer3 = QtWidgets.QLineEdit(QDialog)
        self.CPCusSer3.setGeometry(QtCore.QRect(180, 240, 41, 21))
        self.CPCusSer3.setReadOnly(True)
        self.CPCusSer3.setObjectName("CPCusSer3")
        self.PCusSer4 = QtWidgets.QLineEdit(QDialog)
        self.PCusSer4.setGeometry(QtCore.QRect(100, 310, 41, 21))
        self.PCusSer4.setObjectName("PCusSer4")
        self.CPCusSer4 = QtWidgets.QLineEdit(QDialog)
        self.CPCusSer4.setGeometry(QtCore.QRect(180, 310, 41, 21))
        self.CPCusSer4.setReadOnly(True)
        self.CPCusSer4.setObjectName("CPCusSer4")
        self.PCusSer5 = QtWidgets.QLineEdit(QDialog)
        self.PCusSer5.setGeometry(QtCore.QRect(100, 370, 41, 21))
        self.PCusSer5.setObjectName("PCusSer5")
        self.CPCusSer5 = QtWidgets.QLineEdit(QDialog)
        self.CPCusSer5.setGeometry(QtCore.QRect(180, 370, 41, 21))
        self.CPCusSer5.setReadOnly(True)
        self.CPCusSer5.setObjectName("CPCusSer5")
        self.PCusSer6 = QtWidgets.QLineEdit(QDialog)
        self.PCusSer6.setGeometry(QtCore.QRect(100, 430, 41, 21))
        self.PCusSer6.setObjectName("PCusSer6")
        self.CPCusSer6 = QtWidgets.QLineEdit(QDialog)
        self.CPCusSer6.setGeometry(QtCore.QRect(180, 430, 41, 21))
        self.CPCusSer6.setReadOnly(True)
        self.CPCusSer6.setObjectName("CPCusSer6")

        #说明文字
        self.label_10 = QtWidgets.QLabel(QDialog)
        self.label_10.setGeometry(QtCore.QRect(310, 40, 171, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(QDialog)
        self.label_11.setGeometry(QtCore.QRect(290, 110, 51, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(QDialog)
        self.label_12.setGeometry(QtCore.QRect(290, 170, 51, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(QDialog)
        self.label_13.setGeometry(QtCore.QRect(290, 250, 72, 15))
        self.label_13.setObjectName("label_13")

        #划线
        self.line = QtWidgets.QFrame(QDialog)
        self.line.setGeometry(QtCore.QRect(246, 50, 51, 161))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        #数据检查和确认button
        self.DateInspection = QtWidgets.QPushButton(QDialog)
        self.DateInspection.setGeometry(QtCore.QRect(290, 360, 111, 28))
        self.DateInspection.setObjectName("DateInspection")


        #重置button
        self.Reset_1 = QtWidgets.QPushButton(QDialog)
        self.Reset_1.setGeometry(QtCore.QRect(450, 360, 61, 28))
        self.Reset_1.setObjectName("Reset_1")


        #帮助button
        self.Help = QtWidgets.QPushButton(QDialog)
        self.Help.setGeometry(QtCore.QRect(290, 430, 61, 28))
        self.Help.setObjectName("Help")
        self.Help.setCheckable(True)


        #取消button
        self.Cancel = QtWidgets.QPushButton(QDialog)
        self.Cancel.setGeometry(QtCore.QRect(450, 430, 61, 28))
        self.Cancel.setObjectName("Cancel")


        #到达时间的最大最小值
        self.arrive_timemax = QtWidgets.QLineEdit(QDialog)
        self.arrive_timemax.setGeometry(QtCore.QRect(370, 110, 91, 21))
        self.arrive_timemax.setObjectName("arrive_timemax")
        self.arrive_timemin = QtWidgets.QLineEdit(QDialog)
        self.arrive_timemin.setGeometry(QtCore.QRect(370, 170, 91, 21))
        self.arrive_timemin.setObjectName("arrive_timemin")

        #人数
        self.NumOfPeo = QtWidgets.QLineEdit(QDialog)
        self.NumOfPeo.setGeometry(QtCore.QRect(370, 250, 91, 21))
        self.NumOfPeo.setObjectName("NumOfPeo")

        #划线
        self.line_2 = QtWidgets.QFrame(QDialog)
        self.line_2.setGeometry(QtCore.QRect(480, 50, 61, 161))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(QDialog)
        self.line_3.setGeometry(QtCore.QRect(270, 40, 41, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(QDialog)
        self.line_4.setGeometry(QtCore.QRect(270, 200, 241, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(QDialog)
        self.line_5.setGeometry(QtCore.QRect(470, 40, 41, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.retranslateUi(QDialog)
        QtCore.QMetaObject.connectSlotsByName(QDialog)

        QDialog.show()

    def retranslateUi(self, QDialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(_translate("QDialog", "系统数据设置"))
        self.label.setText(_translate("QDialog", "<html><style>p{margin:0px}</style><head/><body><p>每个客户</p><p>服务时间</p><p>（时间）</p></body></html>"))
        self.label_2.setText(_translate("QDialog", "<html><head/><body><p>概率</p></body></html>"))
        self.label_3.setText(_translate("QDialog", "累计概率"))
        self.label_4.setText(_translate("QDialog", "1"))
        self.label_5.setText(_translate("QDialog", "2"))
        self.label_6.setText(_translate("QDialog", "3"))
        self.label_7.setText(_translate("QDialog", "4"))
        self.label_8.setText(_translate("QDialog", "5"))
        self.label_9.setText(_translate("QDialog", "6"))
        self.label_10.setText(_translate("QDialog", "<html><head/><body><p><span style=\" color:#5500ff;\">到达时间时间隔（分钟）</span></p></body></html>"))
        self.label_11.setText(_translate("QDialog", "<html><head/><body><p>最大值：</p></body></html>"))
        self.label_12.setText(_translate("QDialog", "最小值："))
        self.label_13.setText(_translate("QDialog", "人数："))
        self.DateInspection.setText(_translate("QDialog", "数据检查和确认"))
        self.Reset_1.setText(_translate("QDialog", "重置"))
        self.Help.setText(_translate("QDialog", "帮助"))
        self.Cancel.setText(_translate("QDialog", "取消"))




