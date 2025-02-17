from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
class profile_widget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)#相当于下面那句
        self.setupUI()
    def setupUI(self):
        #self=QtWidgets.QWidget(Form)#self不能变
        self.setGeometry(QtCore.QRect(259, 29, 981, 671))
        self.setObjectName("profile_widget")
        self.register_age_label = QtWidgets.QLabel(self)
        self.register_age_label.setGeometry(QtCore.QRect(60, 334, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.register_age_label.setFont(font)
        self.register_age_label.setObjectName("register_age_label")
        self.register_address_label = QtWidgets.QLabel(self)
        self.register_address_label.setGeometry(QtCore.QRect(60, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.register_address_label.setFont(font)
        self.register_address_label.setObjectName("register_address_label")
        self.register_name_label = QtWidgets.QLabel(self)
        self.register_name_label.setGeometry(QtCore.QRect(60, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.register_name_label.setFont(font)
        self.register_name_label.setObjectName("register_name_label")
        self.register_id_label = QtWidgets.QLabel(self)
        self.register_id_label.setGeometry(QtCore.QRect(60, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.register_id_label.setFont(font)
        self.register_id_label.setObjectName("register_id_label")
        self.register_password_label = QtWidgets.QLabel(self)
        self.register_password_label.setGeometry(QtCore.QRect(60, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.register_password_label.setFont(font)
        self.register_password_label.setObjectName("register_password_label")
        self.register_idcard_label = QtWidgets.QLabel(self)
        self.register_idcard_label.setGeometry(QtCore.QRect(60, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.register_idcard_label.setFont(font)
        self.register_idcard_label.setObjectName("register_idcard_label")
        self.register_id_output = QtWidgets.QLabel(self)
        self.register_id_output.setGeometry(QtCore.QRect(210, 80, 271, 31))
        self.register_id_output.setObjectName("register_id_output")
        self.profile_picture = QtWidgets.QLabel(self)
        self.profile_picture.setGeometry(QtCore.QRect(530, 80, 211, 211))
        self.profile_picture.setText("")
        self.profile_picture.setPixmap(QtGui.QPixmap("source/女.png"))
        self.profile_picture.setObjectName("profile_picture")
        self.medical_record_button = QtWidgets.QPushButton(self)
        self.medical_record_button.setGeometry(QtCore.QRect(520, 310, 211, 51))
        self.medical_record_button.setObjectName("medical_record_button")
        self.register_password_output = QtWidgets.QLabel(self)
        self.register_password_output.setGeometry(QtCore.QRect(210, 130, 271, 31))
        self.register_password_output.setObjectName("register_password_output")
        self.register_name_output = QtWidgets.QLabel(self)
        self.register_name_output.setGeometry(QtCore.QRect(210, 180, 271, 31))
        self.register_name_output.setObjectName("register_name_output")
        self.register_idcard_output = QtWidgets.QLabel(self)
        self.register_idcard_output.setGeometry(QtCore.QRect(210, 230, 271, 31))
        self.register_idcard_output.setObjectName("register_idcard_output")
        self.register_address_output = QtWidgets.QLabel(self)
        self.register_address_output.setGeometry(QtCore.QRect(210, 280, 271, 31))
        self.register_address_output.setObjectName("register_address_output")
        self.register_age_output = QtWidgets.QLabel(self)
        self.register_age_output.setGeometry(QtCore.QRect(210, 334, 271, 31))
        self.register_age_output.setObjectName("register_age_output")

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #Form.setWindowTitle(_translate("Form", "Form"))
        self.register_age_label.setText(_translate("Form", "年龄"))
        self.register_address_label.setText(_translate("Form", "地址"))
        self.register_name_label.setText(_translate("Form", "姓名"))
        self.register_id_label.setText(_translate("Form", "账号"))
        self.register_password_label.setText(_translate("Form", "密码"))
        self.register_idcard_label.setText(_translate("Form", "身份证号"))
        self.register_id_output.setText(_translate("Form", "TextLabel"))
        self.medical_record_button.setText(_translate("Form", "电子病历"))
        self.register_password_output.setText(_translate("Form", "TextLabel"))
        self.register_name_output.setText(_translate("Form", "TextLabel"))
        self.register_idcard_output.setText(_translate("Form", "TextLabel"))
        self.register_address_output.setText(_translate("Form", "TextLabel"))
        self.register_age_output.setText(_translate("Form", "TextLabel"))