# Author: Chairman Studios
# Year: December 2021
# Licence: GPL
# Credits: Chairman Studios

from file_dialog import StartWindow
from imports import *

if __name__ == '__main__':
    app = QApplication()
    dialog = StartWindow()
    dialog.show()
    app.exec()
