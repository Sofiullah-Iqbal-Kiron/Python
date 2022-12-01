from PyQt6.QtCore import QSize, Qt
import sys
import pytube

# Well formatted import statement.
from PyQt6.QtWidgets import *

# Essential qt app.
app = QApplication(sys.argv)

inputLinkStyle = """
QLineEdit {
    height: 24px;
    font-family: 'Times New Roman';
    padding-left: 0px;
    text-align: left;
    font-size: 10px
    }
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        print(QStyleFactory.keys())
        # self.setStyle(QStyleFactory.create("windowsvista"))

        self.setWindowTitle("YouDowr!")

        mainWidget = QWidget()
        self.inputLink = QLineEdit()
        self.inputLink.setStyleSheet(inputLinkStyle)
        self.inputLink.textChanged.connect(self.inputLinkChanged)

        # Download button.
        self.download = QPushButton("Download!")
        self.download.clicked.connect(self.downloadMe)

        # Available formats: QComboBox
        self.availableFormats = AvailableFormats()

        firstRowLay = QHBoxLayout()
        firstRowLay.addWidget(QLabel("Insert linK: "))
        firstRowLay.addWidget(self.inputLink)
        firstRowLay.addWidget(self.availableFormats)
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
        yt = pytube.YouTube(line)
        formats = []
        for s in yt.streams.filter(type="video"):
            currentStreamDetails = str(s.resolution)+" "+str(s._filesize)+" "+str(s.mime_type)
            formats.append(currentStreamDetails)
        self.availableFormats.addItems(formats)


class AvailableFormats(QComboBox):
    def __init__(self):  # parameter bug, may be here.
        super().__init__()

        self.addItem("Available File Formats")


window = MainWindow()

# Start the event loop.
app.exec()
