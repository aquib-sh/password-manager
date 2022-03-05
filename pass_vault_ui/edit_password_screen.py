from PyQt5.QtWidgets import QMainWindow
from pass_vault_ui.layouts import edit_password_ui

class EditPasswordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__edit_password_ui = edit_password_ui.Ui_Form()
        self.__edit_password_ui.setupUi(self)

    def connect_save_btn(self, event):
        self.__edit_password_ui.save_btn.clicked.connect(event)

    def connect_back_btn(self, event):
        self.__edit_password_ui.back_btn.clicked.connect(event)
    
    def connect_generate_btn(self, event):
        self.__edit_password_ui.gen_password_btn.clicked.connect(event)
    
    def connect_clipboard_btn(self, event):
        self.__edit_password_ui.clipboard_btn.clicked.connect(event)