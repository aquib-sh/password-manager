from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton

class DataCard:
    """Cards are the units displayed on home screen containing information."""
    def __init__(self, layout):
        self.parent = layout
        self.card = QPushButton()

    def style_card(self):
        self.card.setFixedSize(QtCore.QSize(400, 150))
        self.card.setStyleSheet("QPushButton::hover"
                             "{"
                             "border: 5px inset silver;"
                             "background-color : rgba(0, 255, 0, 0.21);"
                             "}")

    def attach_to_layout(self):
        self.parent.addWidget(self.card)
    
    def add_data(self):
        """Adds complete data to the card."""
        pass

    def __add_row(self):
        """Adds an individual row of data to the card."""
        pass

class PasswordCard(DataCard):
    """Card containing information of website, username/email and password."""
    def __init__(self, layout):
        super().__init__(layout)
