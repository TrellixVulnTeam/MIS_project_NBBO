from main_widget import MainWidget
from register_widget import RegisterWidget
from Info_window_widget import InfoWindowWidget
from login_widget import LoginWidget
from add_medical_record_widget import AddMedicalRecordWidget
from show_medical_record_widget import ShowMedicalRecordWidget
from update_medical_record_widget import UpdateMedicalRecordWidget


class DigitalRecordSystem:
    def __init__(self):
        self.main_widget = MainWidget()
        self.register_widget = RegisterWidget()
        self.info_window_widget = InfoWindowWidget()
        self.login_widget = LoginWidget()
        self.add_medical_record_widget = AddMedicalRecordWidget()
        self.show_medical_record_widget = ShowMedicalRecordWidget()
        self.update_medical_record_widget=UpdateMedicalRecordWidget()
        self.init_slots()
        self.init_connects()
        return

    def init_slots(self):
        self.register_widget.signal_user.connect(self.info_window_widget.show)
        self.register_widget.signal_user.connect(self.info_window_widget.getUser)
        self.login_widget.regbtn.clicked.connect(self.register_widget.show)
        self.login_widget.signal_login.connect(self.main_widget.set_user_id)
        self.login_widget.signal_login.connect(self.main_widget.show)
        return

    def init_connects(self):
        self.main_widget.ui.add_button.clicked.connect(self.add_medical_record_widget.show)
        self.main_widget.ui.search_button.clicked.connect(self.show_search_widget)
        self.show_medical_record_widget.editButton.clicked.connect(self.show_edit_widget)

    def show_search_widget(self):
        name=self.main_widget.get_search_info()
        self.show_medical_record_widget.load_data(name)
        if self.show_medical_record_widget.refresh_data(self.main_widget.user_id):
            self.show_medical_record_widget.show()
        else:
            self.main_widget.search_fail_message()

    def show_edit_widget(self):
        name=self.show_medical_record_widget.data.get('name')
        self.update_medical_record_widget.load_data(name)
        if self.update_medical_record_widget.refresh_data(self.show_medical_record_widget.user_id):
            self.update_medical_record_widget.show()
            self.show_medical_record_widget.hide()
        else:
            return


