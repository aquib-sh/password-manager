from PyQt5.QtWidgets import QMainWindow
from pass_vault_ui.layouts import home_ui

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__home_ui = home_ui.Ui_MainWindow()
        self.__home_ui.setupUi(self) 

    def connect_logout_btn(self, event):
        self.__home_ui.log_out_btn.clicked.connect(event)

    def connect_add_btn(self, event):
        self.__home_ui.add_btn.clicked.connect(event)

    def connect_delete_btn(self, event):
        self.__home_ui.delete_btn.clicked.connect(event)