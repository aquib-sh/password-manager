from curses import wrapper
from pass_vault_ui.card import PasswordCard
from pass_vault_ui.card import CardWrapper
from PyQt5.QtWidgets import QVBoxLayout

class HomeLayoutManager:
    def __init__(self, app):
        self.app = app
        self.cards_layout = QVBoxLayout()
        self.pcards = []
        self.index = -1

    def update_home_layout(self):
        self.app.home_window.set_layout(self.cards_layout)

    def create_card(self) -> tuple:
        """Creates a card inside a wrapper and puts it inside the layout """
        site = self.app.edit_password_window.get_site_value()
        website = self.app.edit_password_window.get_url_value()
        username = self.app.edit_password_window.get_username_value()
        password = self.app.edit_password_window.get_password_value()
        self.index += 1

        card = PasswordCard()
        card.insert_data(username, password, site)

        wrapper = CardWrapper(self.cards_layout, card)
        wrapper.wrap()

        self.pcards.append(wrapper)
        self.update_home_layout()
        return (site,  website, username, password)

    def __delete_card(self, card_wrapper):
        """Deletes an individual card."""
        card_wrapper.detach_from_layout()
        del card_wrapper

    def delete_selected(self):
        """Iterates through all the card wrappers,
        delete the one's that have checked in checkbox.
        """
        temp = self.pcards.copy()   #create a copy to avoid pointer bugs
        for i in range(0, len(temp)):
            if (temp[i].is_checked()):
                indx_of_card = self.pcards.index(temp[i])
                self.__delete_card(self.pcards[indx_of_card])
                self.index -= 1
                self.update_home_layout()