from imports import *
from main import PyPlayer
from dialog import Ui_MainWindow

# ui, _ = loadUiType("ui/file_dialog.ui")


# This window will act as a main entry point of the main window
# It will allow us to select all required file paths
class StartWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(StartWindow, self).__init__(None)
        self.setupUi(self)
        self.setFixedSize(600, 200)
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        self.main = PyPlayer()

        self.confirm.clicked.connect(self.load_folders)
        self.selectFolder.clicked.connect(self.load_folder1)
        self.selectFolder2.clicked.connect(self.load_folder2)
        self.cancelBtn.clicked.connect(lambda: self.close())
        self.dialogClose.clicked.connect(lambda: self.close())
        self.dialogMini.clicked.connect(lambda: self.showMinimized())
        self.title_bar.mouseMoveEvent = self.moveTitleBar

    def open_main(self):
        if self.main.isVisible():
            self.main.close()
        else:
            self.main.call_on_start()
            self.main.show()
            self.close()

    def load_folders(self):
        text = self.folder1.text()
        text2 = self.folder2.text()
        if text and text2:
            self.main.folder1 = text
            self.main.folder2 = text2
            self.open_main()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def moveTitleBar(self, event):
        gpos = event.globalPosition().toPoint()
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + gpos - self.dragPos)
            self.dragPos = gpos
            event.accept()

    ##########################################################
    # This functions can be used to open native windows
    # explorer and get the folder instead of pasting manually
    ##########################################################

    def load_folder1(self):
        dg = QFileDialog()
        dg.setFileMode(QFileDialog.Directory)
        if dg.exec():
            filenames = dg.selectedFiles()
            self.main.folder1 = "".join(filenames[0])
            self.folder1.setText("".join(filenames[0]))

    def load_folder2(self):
        d = QFileDialog()
        d.setFileMode(QFileDialog.Directory)
        if d.exec():
            filenames = d.selectedFiles()
            self.main.folder2 = os.path.join(filenames[0])
            self.folder2.setText(filenames[0])
        

if __name__ == '__main__':
    app = QApplication()
    dialog = StartWindow()
    dialog.show()
    app.exec()


