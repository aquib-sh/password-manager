from PyQt5.QtWidgets import QMainWindow
from pass_vault_ui.layouts import signup_ui

class SignUpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__signup_screen = signup_ui.Ui_Form()
        self.__signup_screen.setupUi(self)

    def connect_signup_btn(self, event):
        self.__signup_screen.sign_up_btn.clicked.connect(event)

    def connect_otp_btn(self, event):
        self.__signup_screen.get_otp_btn.clicked.connect(event)