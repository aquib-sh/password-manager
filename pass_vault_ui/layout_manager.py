from pass_vault_ui.card import PasswordCard
from PyQt5.QtWidgets import QVBoxLayout

class LayoutManager:
    def __init__(self, app):
        self.app = app
        self.cards_layout = QVBoxLayout()
        self.pcards = []
        self.index = -1

    def update_home_layout(self):
        self.app.home_window.set_layout(self.cards_layout)

    def create_card(self) -> tuple:
        site = self.app.edit_password_window.get_site_value()
        website = self.app.edit_password_window.get_url_value()
        username = self.app.edit_password_window.get_username_value()
        password = self.app.edit_password_window.get_password_value()
        self.index += 1
        self.pcards.append(PasswordCard(self.cards_layout))
        self.pcards[self.index].insert_data(username, password, site)
        self.pcards[self.index].attach_to_layout()

        self.update_home_layout()

        return (site,  website, username, password)

    def delete_card(self):
        self.pcards[0].detach_from_layout()
        del self.pcards[0]
        self.index -= 1
        self.update_home_layout()