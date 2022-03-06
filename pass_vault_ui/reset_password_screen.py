from PyQt5.QtWidgets import QMainWindow
from pass_vault_ui.layouts import reset_password_ui

class ResetPasswordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__reset_password_screen = reset_password_ui.Ui_Form()
        self.__reset_password_screen.setupUi(self)

    def connect_reset_btn(self, event):
        self.__reset_password_screen.reset_btn.clicked.connect(event)

    def connect_otp_btn(self, event):
        self.__reset_password_screen.get_otp_btn.clicked.connect(event)

