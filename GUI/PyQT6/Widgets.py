from PyQt6.QtCore import QSize, Qt
import sys

# Well formatted import statement.
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QDateTimeEdit,
    QDial,
    QLCDNumber,
    QFontComboBox,
)

# Essential qt app.
app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exploring Widgets!")
        widget = QFontComboBox()
        self.setCentralWidget(widget)  # QMainWindow specific method to add a widget in center.
        self.show()


window = MainWindow()

# Start the event loop.
app.exec()
