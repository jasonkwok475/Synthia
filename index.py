import sys
from PyQt5.QtWidgets import QApplication
from main_window.select_window import SelectWindow

def main():
  app = QApplication(sys.argv)
  ex = SelectWindow()
  #ex.show()
  
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()