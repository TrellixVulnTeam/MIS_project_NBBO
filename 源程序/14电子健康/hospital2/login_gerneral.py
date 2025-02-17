from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QMessageBox, QLineEdit)
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 352)

        #login_Dialog
        self.login_Dialog = QtWidgets.QWidget(Dialog)
        self.login_Dialog.setGeometry(QtCore.QRect(0, 0, 501, 351))
        self.login_Dialog.setObjectName("login_Dialog")
        self.login_button = QtWidgets.QPushButton(self.login_Dialog)
        self.login_button.setGeometry(QtCore.QRect(180, 250, 90, 30))
        self.login_button.setObjectName("login_button")
        self.register_button = QtWidgets.QPushButton(self.login_Dialog)
        self.register_button.setGeometry(QtCore.QRect(280, 250, 81, 30))
        self.register_button.setObjectName("register_button")
        self.patient_ID_input = QtWidgets.QLineEdit(self.login_Dialog)
        self.patient_ID_input.setGeometry(QtCore.QRect(180, 170, 181, 30))
        self.patient_ID_input.setObjectName("patient_ID_input")
        # self.doctor_login_button = QtWidgets.QPushButton(self.login_Dialog)
        # self.doctor_login_button.setGeometry(QtCore.QRect(380, 330, 41, 21))
        # self.doctor_login_button.setObjectName("doctor_login_button")
        self.patient_password_input = QtWidgets.QLineEdit(self.login_Dialog)
        self.patient_password_input.setGeometry(QtCore.QRect(180, 210, 181, 30))
        self.patient_password_input.setObjectName("patient_password_input")
        self.patient_password_input.setEchoMode(QLineEdit.Password)
        # self.manager_login_button = QtWidgets.QPushButton(self.login_Dialog)
        # self.manager_login_button.setGeometry(QtCore.QRect(430, 330, 41, 21))
        # self.manager_login_button.setObjectName("manager_login_button")

        self.top_picture_Dialog = QtWidgets.QLabel(self.login_Dialog)
        self.top_picture_Dialog.setGeometry(QtCore.QRect(0, 0, 501, 141))
        # self.top_picture_Dialog.setText("")
        #self.top_picture_Dialog.setPixmap(QtGui.QPixmap("pic1.jpg"))
        self.top_picture_Dialog.setObjectName("top_picture_Dialog")
        self.gif = QMovie('source/梵高.gif')
        self.top_picture_Dialog.setMovie(self.gif)
        self.gif.start()


        self.profile_picture_lable = QtWidgets.QLabel(self.login_Dialog)
        self.profile_picture_lable.setGeometry(QtCore.QRect(60, 180, 91, 91))
        self.profile_picture_lable.setText("")
        self.profile_picture_lable.setPixmap(QtGui.QPixmap("source/尼尔.jpg").scaled((self.profile_picture_lable.rect().size())))

        self.profile_picture_lable.setObjectName("profile_picture_lable")
        #缩小与关闭按钮，每个窗口都有
        self.subtrack_button = QtWidgets.QPushButton(self)
        self.subtrack_button.setGeometry(QtCore.QRect(400, 10, 30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/subtract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subtrack_button.setIcon(icon)
        self.subtrack_button.setObjectName("subtrack_button")
        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setGeometry(QtCore.QRect(440, 10, 30, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("source/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setObjectName("close_button")




        #patient_register_widget
        self.patient_register_widget = QtWidgets.QWidget(Dialog)
        self.patient_register_widget.setGeometry(QtCore.QRect(0, 0, 501, 351))
        self.patient_register_widget.setObjectName("patient_register_widget")
        self.register_id_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_id_label.setGeometry(QtCore.QRect(80, 50, 25, 18))
        self.register_id_label.setObjectName("register_id_label")
        self.register_password_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_password_label.setGeometry(QtCore.QRect(80, 93, 25, 18))
        self.register_password_label.setObjectName("register_password_label")
        self.register_name_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_name_label.setGeometry(QtCore.QRect(80, 136, 24, 18))
        self.register_name_label.setObjectName("register_name_label")
        self.register_idcard_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_idcard_label.setGeometry(QtCore.QRect(80, 178, 49, 18))
        self.register_idcard_label.setObjectName("register_idcard_label")
        self.register_address_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_address_label.setGeometry(QtCore.QRect(80, 221, 25, 18))
        self.register_address_label.setObjectName("register_address_label")
        self.register_age_label = QtWidgets.QLabel(self.patient_register_widget)
        self.register_age_label.setGeometry(QtCore.QRect(80, 264, 25, 18))
        self.register_age_label.setObjectName("register_age_label")
        self.registerid_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.registerid_input.setGeometry(QtCore.QRect(140, 50, 251, 30))
        self.registerid_input.setObjectName("registerid_input")
        self.register_password_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.register_password_input.setGeometry(QtCore.QRect(140, 93, 251, 30))
        self.register_password_input.setObjectName("register_password_input")
        self.register_name_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.register_name_input.setGeometry(QtCore.QRect(140, 136, 251, 30))
        self.register_name_input.setObjectName("register_name_input")
        self.register_idcard_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.register_idcard_input.setGeometry(QtCore.QRect(140, 178, 251, 30))
        self.register_idcard_input.setObjectName("register_idcard_input")
        self.register_address_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.register_address_input.setGeometry(QtCore.QRect(140, 221, 251, 30))
        self.register_address_input.setObjectName("register_address_input")
        self.register_age_input = QtWidgets.QLineEdit(self.patient_register_widget)
        self.register_age_input.setGeometry(QtCore.QRect(140, 264, 251, 30))
        self.register_age_input.setObjectName("register_age_input")
        self.register_submit_button = QtWidgets.QPushButton(self.patient_register_widget)
        self.register_submit_button.setGeometry(QtCore.QRect(140, 310, 90, 30))
        self.register_submit_button.setObjectName("register_submit_button")
        self.register_cancle_button = QtWidgets.QPushButton(self.patient_register_widget)
        self.register_cancle_button.setGeometry(QtCore.QRect(300, 310, 90, 30))
        self.register_cancle_button.setObjectName("register_cancle_button")
        self.close_button.raise_()
        self.subtrack_button.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        #login
        self.register_button.setText(_translate("Dialog", "注册"))
        self.login_button.setText(_translate("Dialog", "登录"))
        # self.doctor_login_button.setText(_translate("Dialog", "医生登录"))
        # self.manager_login_button.setText(_translate("Dialog", "管理员登录"))
        #register
        self.register_id_label.setText(_translate("Dialog", "账号"))
        self.register_password_label.setText(_translate("Dialog", "密码"))
        self.register_name_label.setText(_translate("Dialog", "姓名"))
        self.register_idcard_label.setText(_translate("Dialog", "身份证号"))
        self.register_address_label.setText(_translate("Dialog", "地址"))
        self.register_age_label.setText(_translate("Dialog", "年龄"))
        self.register_submit_button.setText(_translate("Dialog", "提交"))
        self.register_cancle_button.setText(_translate("Dialog", "返回"))
        self.registerid_input.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;示例：0000012345&quot;</span></p></body></html>"))
        self.register_password_input.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;示例：123456&quot;</span></p></body></html>"))
        self.register_name_input.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;示例：王多余&quot;</span></p></body></html>"))
        self.register_idcard_input.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;十八位数字&quot;</span></p></body></html>"))
        self.register_address_input.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;请输入地址&quot;</span></p></body></html>"))
        self.register_age_input.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" color:#ff0000;\">&quot;两位数字&quot;</span></p></body></html>"))
