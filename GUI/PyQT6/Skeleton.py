# PyQT is a GUI library developed over QT.
# Author: Riverbank Computing.

# Tutorial: https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/

from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# We need one and only one QApplication in each app.
# Receive arguments from command line(sys.argv), if not interested then simply just use empty list: []
app = QApplication(sys.argv)

# QWidget is the top level window for our application.
# All the qt widgets are top level windows. Like JavaFX Controls.
# We can use all widget as top level window/container.
mainWindow = QMainWindow()  # Or use QWidget().
mainWindow.setWindowTitle("First PyQT App!")
mainWindow.show()

# Start the event loop.
app.exec()
