import sys
from PyQt5.QtWidgets import QApplication
from pass_vault_ui.home_screen import HomeWindow
from pass_vault_ui.login_screen import LoginWindow
from pass_vault_ui.signup_screen import SignUpWindow
from pass_vault_ui.edit_password_screen import EditPasswordWindow
from pass_vault_ui.reset_password_screen import ResetPasswordWindow
from pass_vault_ui.layout_manager import LayoutManager

class PassVault:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = LoginWindow()
        self.home_window = HomeWindow()
        self.signup_window = SignUpWindow()
        self.edit_password_window = EditPasswordWindow()
        self.reset_password_window = ResetPasswordWindow()
        self.setup_connections()
        self.layout_manager = LayoutManager(self)

    def setup_connections(self):
        """Makes connection between window buttons and methods."""
        self.login_window.connect_login_btn(self.login)
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

        self.reset_password_window.connect_otp_btn(self.send_otp)
        self.reset_password_window.connect_reset_btn(self.reset_value)

    def reset_value(self):
        pass

    def show_register_screen(self):
        self.signup_window.show()

    def valid_credentials(self, username, password) -> bool:
        """Checks whether the username and password exists in database."""
        return True

    def login(self):
        username = self.login_window.get_username()
        password = self.login_window.get_password()
        creds_are_valid = self.valid_credentials(username, password)

        if creds_are_valid:
            self.login_window.close()
            self.home_window.show()

    def show_add_screen(self):
        self.edit_password_window.show()

    def show_reset_screen(self):
        self.reset_password_window.show()

    def save_value(self):
        site, website, user, password = self.layout_manager.create_card()
        print(f"[+] New Card created with\nUser: {user}\nPassword: {password}")
        self.edit_password_window.clear_inputs()

    def generate_password(self):
        pass

    def copy_to_clipboard(self):
        pass

    def go_back_to_homescreen(self):
        self.layout_manager.delete_card()
        self.edit_password_window.close()

    def signup(self):
        pass

    def send_otp(self):
        pass

    def log_out(self):
        pass

    def delete_values(self):
        pass

if __name__ == "__main__":
    passvault = PassVault()
    passvault.login_window.show()
    sys.exit(passvault.app.exec_())
        

