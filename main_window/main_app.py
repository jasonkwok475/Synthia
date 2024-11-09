import logging
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

logging.basicConfig(level=logging.INFO)

class MainWindow(QWidget):
  def __init__(self, parent = None):
    super(MainWindow, self).__init__(parent)

    self.resize(200,50)
    self.setWindowTitle("Synthia")
    self.initUi()

    self.showMaximized()

  def initUi(self):
    self.grid = QGridLayout()

    self.setLayout(self.grid)

 

  
