from PyQt6.QtCore import QSize, Qt
import sys
import pytube

# Well formatted import statement.
from PyQt6.QtWidgets import *

# Essential qt app.
app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouDowr!")

        mainWidget = QWidget()
        self.inputLink = QLineEdit()
        download = QPushButton("Download!")
        download.clicked.connect(self.downloadMe)

        firstRowLay = QHBoxLayout()
        firstRowLay.addWidget(QLabel("Insert linK: "))
        firstRowLay.addWidget(self.inputLink)
        firstRow = QWidget()
        firstRow.setLayout(firstRowLay)

        secondRow = QVBoxLayout()
        secondRow.setSpacing(5)
        secondRow.addWidget(firstRow)
        secondRow.addWidget(download)

        mainWidget.setLayout(secondRow)
        self.setCentralWidget(mainWidget)  # QMainWindow specific method to add a widget in center.
        self.show()

    def downloadMe(self):
        yt = pytube.YouTube(self.inputLink.text().strip())
        yt.streams.first().download()


window = MainWindow()

# Start the event loop.
app.exec()
