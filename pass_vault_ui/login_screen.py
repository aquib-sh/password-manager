from PyQt5.QtWidgets import QMainWindow

from pass_vault_ui.layouts import login_ui


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__login_ui = login_ui.Ui_Form()
        self.__login_ui.setupUi(self)

    def reset(self):
        self.set_username("")
        self.set_password("")
        self.display_message("")

    def connect_login_btn(self, event):
        self.__login_ui.login_btn.clicked.connect(event)

    def connect_reset_btn(self, event):
        self.__login_ui.reset_btn.clicked.connect(event)

    def connect_register_btn(self, event):
        self.__login_ui.register_btn.clicked.connect(event)

    def get_username(self):
        return self.__login_ui.username_input.text()

    def get_password(self):
        return self.__login_ui.password_input.text()

    def set_username(self, text):
        self.__login_ui.username_input.setText("")

    def set_password(self, text):
        self.__login_ui.password_input.setText("")

    def display_message(self, text):
        self.__login_ui.debug_lbl.setText(text)
