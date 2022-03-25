from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import (
    QCheckBox,
    QVBoxLayout, 
    QHBoxLayout,
    QPushButton,
    QWidget,
    QLabel
)

class DataCard:
    """Cards are the units displayed on home screen containing information."""
    def __init__(self):
        self.CARD_SIZE = (400, 150)
        self.ROW_SIZE = (350, 40)
        self.ROW_KEY_SIZE = (100, 30)
        self.ROW_VALUE_SIZE = (270, 30)

        self.card = QPushButton()

    def style_card(self):
        self.card.setFixedSize(QtCore.QSize(
            self.CARD_SIZE[0], self.CARD_SIZE[1])
            )
        self.card.setStyleSheet("""QPushButton::hover
                             {
                                border: 5px groove silver;
                                background-color : rgba(0, 255, 0, 0.21);
                             }
                            QPushButton {
                                border: 1px solid silver;
                                border-radius: 20px;
                            }""")

    def attach_to_layout(self, layout):
        layout.addWidget(self.card)

    def detach_from_layout(self):
        #self.parent.removeWidget(self.card)
        self.card.setParent(None)
    
    def insert_data(self):
        """Adds complete data to the card."""
        pass

    def __insert_row(self):
        """Adds an individual row of data to the card."""
        pass

class PasswordCard(DataCard):
    """Card containing information of website, username/email and password.
    
      -------- LAYOUT DESCRIPTION OF A PASSWORD CARD -----------------
      |  --------------QVBoxLayout (Vertical Layout)--------------   |   
      |  |    ------- QHBoxLayout (Horizontal Layout)---------    |  |
      |  |    |            -------------                      |   |  |
      |  |    |           | key | value |                     |   |  |
      |  |    |            -------------                      |   |  |
      |  |    -------------------------------------------------   |  |
      |  |  ----------------------------------------------------- |  |
      |  |                                                        |  | 
      |  |    ------- QHBoxLayout (Horizontal Layout)---------    |  |
      |  |    |            -------------                      |   |  |
      |  |    |           | key | value |                     |   |  |
      |  |    |            -------------                      |   |  |
      |  |    -------------------------------------------------   |  |
      |  |  ----------------------------------------------------- |  |
      |  |                                                        |  | 
      |  |    ------- QHBoxLayout (Horizontal Layout)---------    |  |
      |  |    |            -------------                      |   |  |
      |  |    |           | key | value |                     |   |  |
      |  |    |            -------------                      |   |  |
      |  |    -------------------------------------------------   |  |
      |  |------------------------------------------------------- |  |
      |--------------------------------------------------------------|
    """
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.entry1 = QWidget()
        self.entry2 = QWidget()
        self.entry3 = QWidget()

    def insert_data(self, user, password, site=""):
        """The insertion of data take place in 2 steps,
        First there is a vertical layout in which rows are 3 rows are inserted into QVBoxLayout 
        In next step we place a horizontal layout in each of these 3 rows, so that each QHBoxLayout has
        key: value in them and a QVBoxLayout has 3 of such QHBoxLayout.
        """
        self.style_card()

        self.__insert_row(self.entry1, "Site", site)
        self.__insert_row(self.entry2, "User", user)
        self.__insert_row(self.entry3, "Password", password)

        self.layout.addWidget(self.entry1)
        self.layout.addWidget(self.entry2)
        self.layout.addWidget(self.entry3)
        self.card.setLayout(self.layout)

    def __insert_row(self, widget, key, value):
        widget.setFixedSize(QtCore.QSize(
            self.ROW_SIZE[0], self.ROW_SIZE[1])
            )
        widget.setStyleSheet("font-size:5; font:monospace; text-align:left")
        layout = QHBoxLayout()

        key = QLabel(key+": ")
        value = QLabel(value)

        key.setFixedSize(QtCore.QSize(
            self.ROW_KEY_SIZE[0], self.ROW_KEY_SIZE[1])
            )
        value.setFixedSize(QtCore.QSize(
            self.ROW_VALUE_SIZE[0], self.ROW_VALUE_SIZE[1])
            )
        layout.addWidget(key)
        layout.addWidget(value)
        widget.setLayout(layout)

class CardWrapper:
    """CardWrapper is used to wrap cards along with a checkbutton.

    These setting of keeping checkbuttons along with a card helps while deleting multiple cards

    Here is a layout of CardWrapper

      ------- LAYOUT DESCRIPTION OF A CARD WRAPPER -------
      |                                                  |
      |   ---------DATA CARD-----------     Checkbox     |
      |   |                           |      -----       |
      |   |                           |      ||_||       |
      |   |                           |      -----       |
      |   |                           |                  |
      |   -----------------------------                  |
      ----------------------------------------------------
    """
    def __init__(self, layout: QVBoxLayout, card: DataCard):
        self.__parent = layout
        self.__card = card
        self.__layout = QHBoxLayout()
        self.__wrapper = QWidget()
        self.__checkbox = QCheckBox()

    def wrap(self):
        """Wraps card into the wrapper with a checkbox on right side."""
        self.__card.attach_to_layout(self.__layout)
        self.__layout.addWidget(self.__checkbox)
        self.__wrapper.setLayout(self.__layout)
        self.attach_to_layout()

    def is_checked(self):
        return self.__checkbox.isChecked()
        
    def attach_to_layout(self):
        self.__parent.addWidget(self.__wrapper)

    def detach_from_layout(self):
        self.__wrapper.setParent(None)