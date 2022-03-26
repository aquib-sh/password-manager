from PyQt5.QtWidgets import QMainWindow
from pass_vault_ui.layouts import signup_ui

class SignUpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__signup_screen = signup_ui.Ui_Form()
        self.__signup_screen.setupUi(self)
        self.__reg_pressed = 0 #n times register btn is pressed
        self.__dispatched_otp = "" #OTP give to user, for internal use

    def inc_reg_pressed(self):
        self.__reg_pressed += 1

    def set_otp(self, otp):
        self.__dispatched_otp = otp

    def get_dispatched_otp(self):
        """Gives the OTP that was sent to the user, 
        the value is erased from property after this method is called."""
        temp = self.__dispatched_otp
        self.__dispatched_otp = ""
        return temp

    def get_reg_press_count(self):
        return self.__reg_pressed

    def connect_signup_btn(self, event):
        self.__signup_screen.sign_up_btn.clicked.connect(event)

    def display_message(self, message):
        self.__signup_screen.message_lbl.setText(message)

    def activate_otp_input(self):
        self.__signup_screen.otp_input.setEnabled(True)

    def get_email_value(self):
        return self.__signup_screen.email_input.text()
    
    def get_confirm_password_value(self):
        return self.__signup_screen.confirm_password_input.text()

    def get_password_value(self):
        return self.__signup_screen.password_input.text()

    def get_username_value(self):
        return self.__signup_screen.username_input.text()

    def get_otp_value(self):
        return self.__signup_screen.otp_input.text()
