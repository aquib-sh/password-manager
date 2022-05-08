from PyQt5.QtWidgets import QVBoxLayout

from pass_vault_ui.card import CardWrapper, PasswordCard


class HomeLayoutManager:
    def __init__(self, app):
        self.app = app
        self.cards_layout = QVBoxLayout()
        self.pcards = []
        # stores attributes of each pcards present as tuples of (username, password, site)
        self.pcards_attr = []
        self.index = -1

    def update_home_layout(self):
        self.app.home_window.set_layout(self.cards_layout)

    def create_cards_from_list(self, data: list):
        """Creates cards from list of tuples"""
        # indexing in a tuple
        USER = 1
        SITE = 2
        PASSWORD = 4
        for row in data:
            self.create_card(row[USER], row[PASSWORD], row[SITE])

    def create_card(self, username, password, site):
        """Creates a card inside a wrapper and puts it inside the layout"""
        self.index += 1

        card = PasswordCard()
        card.insert_data(username, password, site)

        wrapper = CardWrapper(self.cards_layout, card)
        wrapper.wrap()

        self.pcards.append(wrapper)
        self.update_home_layout()
        print(f"[+] Card created with User: {username} | Password: {password}")
        self.pcards_attr.append((username, password, site))

    def __delete_card(self, index: int) -> tuple:
        """Deletes an individual card."""
        self.pcards[index].detach_from_layout()
        del self.pcards[index]
        return self.pcards_attr.pop(index)

    def delete_selected(self) -> list:
        """Iterates through all the card wrappers,
        delete the one's that have checked in checkbox.
        """
        deleted_cards_attr = []
        temp = self.pcards.copy()  # create a copy to avoid pointer bugs
        for i in range(len(temp)):
            if temp[i].is_checked():
                indx_of_card = self.pcards.index(temp[i])
                deleted = self.__delete_card(indx_of_card)
                deleted_cards_attr.append(deleted)
                self.index -= 1
                self.update_home_layout()
        return deleted_cards_attr

    def reset(self):
        """Deletes all the cards and sets everything to the initial stage"""
        temp = self.pcards.copy()  # create a copy to avoid pointer bugs
        for i in range(len(temp)):
            indx_of_card = self.pcards.index(temp[i])
            self.__delete_card(indx_of_card)
            self.update_home_layout()
        self.index = -1
