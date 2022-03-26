import sys
import config
from PyQt5.QtWidgets import QApplication
from pass_vault_ui.home_screen import HomeWindow
from pass_vault_ui.login_screen import LoginWindow
from pass_vault_ui.signup_screen import SignUpWindow
from pass_vault_ui.edit_password_screen import EditPasswordWindow
from pass_vault_ui.reset_password_screen import ResetPasswordWindow
from pass_vault_ui.layout_manager import HomeLayoutManager
from services.google.email import Gmail
from services.google.token import TokenRetriever
from database.manager import DBManager
from utils import OTPGenerator

class PassVault:
    def __init__(self):
        # Intialize UI components
        self.app = QApplication(sys.argv)
        self.login_window = LoginWindow()
        self.home_window = HomeWindow()
        self.signup_window = SignUpWindow()
        self.edit_password_window = EditPasswordWindow()
        self.reset_password_window = ResetPasswordWindow()
        self.__setup_connections()
        self.layout_manager = HomeLayoutManager(self)
        self.otp_gen = OTPGenerator()

        # Initialize Gmail service for emailing OTP 
        self.retr = TokenRetriever()
        gtoken = self.retr.retrieve_google_api_token(
                    token_path=config.GOOGLE_API_TOKEN_PATH, 
                    scopes=config.GOOGLE_API_SCOPE
                )
        self.gmail = Gmail(
                token=gtoken, 
                scope=config.GOOGLE_API_SCOPE
            )
        self.gmail.start_service()

    def __setup_connections(self):
        """Makes connection between window buttons and methods."""
        self.login_window.connect_login_btn(self.login)
        self.login_window.connect_register_btn(self.show_register_screen)
        self.login_window.connect_reset_btn(self.show_reset_screen)

        self.signup_window.connect_signup_btn(self.signup)

        self.home_window.connect_add_btn(self.show_add_screen)
        self.home_window.connect_delete_btn(self.delete_values)
        self.home_window.connect_logout_btn(self.log_out)

        self.edit_password_window.connect_back_btn(self.go_back_to_homescreen)
        self.edit_password_window.connect_clipboard_btn(self.copy_to_clipboard)
        self.edit_password_window.connect_generate_btn(self.generate_password)
        self.edit_password_window.connect_save_btn(self.save_value)

        #self.reset_password_window.connect_otp_btn(self.__send_otp)
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
        self.edit_password_window.close()

    def signup(self):
        self.signup_window.inc_reg_pressed()
        reg_press_count = self.signup_window.get_reg_press_count()

        user = self.signup_window.get_username_value()
        email = self.signup_window.get_email_value()
        password = self.signup_window.get_password_value()
        confirm_password = self.signup_window.get_confirm_password_value()

        if (confirm_password != password):
            self.signup_window.display_message(config.PASSWORD_MISMATCH_MSG)
        else:
            # If register btn is clicked first time then send OTP
            # when clicked 2nd time then verify entered OTP
            if reg_press_count == 1:
                otp = self.otp_gen.generate_alpha_numeric_otp()
                self.signup_window.set_otp(otp)
                self.__send_otp(email, user, otp)
                self.signup_window.display_message(config.ENTER_OTP_MSG.format(email=email))
                self.signup_window.activate_otp_input()
            else:
                if (self.__verify_otp(self.signup_window.get_dispatched_otp())):
                    self.signup_window.display_message(config.REG_SUCESS_MSG)
                else:
                    self.signup_window.display_message(config.INCORRECT_OTP_MSG)


    def __verify_otp(self, otp) -> bool:
        entered_otp = self.signup_window.get_otp_value()
        return (entered_otp == otp)

    def __send_otp(self, email, user, otp):
        msg = self.gmail.create_message(
                sender=config.APP_EMAIL,
                to=email,
                subject="PassVault Verification",
                message_text=config.OTP_MSG.format(
                    user=user, 
                    otp=otp
                    )
                )
        self.gmail.send_message(msg)

    def log_out(self):
        pass

    def delete_values(self):
        self.layout_manager.delete_selected()

if __name__ == "__main__":
    passvault = PassVault()
    passvault.login_window.show()
    sys.exit(passvault.app.exec_())
        

