# Let's handle some event using signal and slots.
# In addition to notify about something happening, signals can also send data to provide context about what happened.
# Slot - signal receiver.

from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt
import sys

# Essential qt app.
app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OOP styled main-window!")
        self.setFixedSize(QSize(500, 270))

        button = QPushButton("Click!")
        button.setToolTip("Click the button!")
        button.clicked.connect(self.buttonClicked)
        self.setCentralWidget(button)  # QMainWindow specific method to add a widget in center.

        self.show()

    # A slot receiving event to handle.
    def buttonClicked(self):
        self.setWindowTitle("Button Clicked!")


window = MainWindow()

# Start the event loop.
app.exec()
