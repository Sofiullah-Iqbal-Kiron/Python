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

        print(QStyleFactory.keys())
        self.setStyle(QStyleFactory.create("windowsvista"))

        self.setWindowTitle("YouDowr!")

        mainWidget = QWidget()
        self.inputLink = QLineEdit()
        self.inputLink.textChanged.connect(self.inputLinkChanged)

        # Download button.
        self.download = QPushButton("Download!")
        self.download.clicked.connect(self.downloadMe)

        firstRowLay = QHBoxLayout()
        firstRowLay.addWidget(QLabel("Insert linK: "))
        firstRowLay.addWidget(self.inputLink)
        firstRow = QWidget()
        firstRow.setLayout(firstRowLay)

        secondRow = QVBoxLayout()
        secondRow.setSpacing(5)
        secondRow.addWidget(firstRow)
        secondRow.addWidget(self.download)

        mainWidget.setLayout(secondRow)
        # QMainWindow specific method to add a widget in center.
        self.setCentralWidget(mainWidget)
        self.show()

    def downloadMe(self):
        pass
        # yt = pytube.YouTube(self.inputLink.text().strip())
        # yt.streams.first().download()

    def inputLinkChanged(self, line):
        self.download.setText(line)


window = MainWindow()

# Start the event loop.
app.exec()
