import sys
from PyQt5.QtWidgets import QApplication
from pass_vault_ui import (
    home_screen,
    login_screen,
    signup_screen,
    edit_password_screen
)

class PassVault:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = login_screen.LoginWindow()
        self.home_window = home_screen.HomeWindow()
        self.signup_window = signup_screen.SignUpWindow()
        self.edit_password_window = edit_password_screen.EditPasswordWindow()
        self.setup_connections()

    def setup_connections(self):
        """Makes connection between window buttons and methods."""
        self.login_window.connect_login_btn(self.show_home_screen)
        self.login_window.connect_register_btn(self.show_register_screen)
        self.login_window.connect_reset_btn(self.show_reset_screen)

        self.signup_window.connect_otp_btn(self.send_otp)
        self.signup_window.connect_signup_btn(self.signup)

        self.home_window.connect_add_btn(self.show_add_screen)
        self.home_window.connect_delete_btn(self.delete_values)
        self.home_window.connect_logout_btn(self.log_out)

        self.edit_password_window.connect_back_btn(self.go_back_to_homescreen)
        self.edit_password_window.connect_clipboard_btn(self.copy_to_clipboard)
        self.edit_password_window.connect_generate_btn(self.generate_password)
        self.edit_password_window.connect_save_btn(self.save_value)

    def show_register_screen(self):
        self.signup_window.show()

    def show_home_screen(self):
        self.login_window.close()
        self.home_window.show()

    def show_add_screen(self):
        self.edit_password_window.show()

    def save_value(self):
        pass

    def generate_password(self):
        pass

    def copy_to_clipboard(self):
        pass

    def go_back_to_homescreen(self):
        pass

    def signup(self):
        pass

    def send_otp(self):
        pass

    def log_out(self):
        pass

    def delete_values(self):
        pass

    def show_reset_screen(self):
        pass

if __name__ == "__main__":
    passvault = PassVault()
    passvault.login_window.show()
    sys.exit(passvault.app.exec_())
        

