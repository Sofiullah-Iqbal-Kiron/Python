from PyQt6.QtCore import QSize, Qt
import sys

# Well formatted import statement.
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QDateTimeEdit,
    QDial,
    QLCDNumber,
    QComboBox,
    QFontComboBox,
    QVBoxLayout,
)

# Essential qt app.
app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exploring Widgets!")

        comboBox = QComboBox()
        comboBox.addItems(["Kiron", "Nirob", "Israt", "Tisha", "Meha"])
        comboBox.currentTextChanged.connect(
            lambda x: print("Changed, now:", x))

        fontComboBox = QFontComboBox()

        layout = QVBoxLayout()
        layout.addWidget(comboBox)
        layout.addWidget(fontComboBox)

        # QMainWindow specific method to add a widget in center.
        mainWidget = QWidget()
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)
        self.show()


window = MainWindow()

# Start the event loop.
app.exec()
