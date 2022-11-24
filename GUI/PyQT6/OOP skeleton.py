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
        self.setCentralWidget(button)  # QMainWindow specific method to add a widget in center.
        self.show()


window = MainWindow()

# Start the event loop.
app.exec()
