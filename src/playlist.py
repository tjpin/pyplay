# #################### Drag and drop Playlist ########
from PySide6.QtGui import QImage

from imports import *

styles = """
    QListView  {
        border: none;\n
        color: rgb(122, 122, 122);\n
        font-size: 12px;\n
    }
    
    QListView:item {
        border: none;\n
        height: 25px;\n
    }
    
    QListView:item:hover {
        background-color: rgb(48, 50, 57);\n
    }
    
    QListView:item:selected {
        background-color: rgb(255, 202, 29);\n
        color: rgb(50, 51, 59);\n
    }
    
    QScrollArea {
        background-color: rgb(26, 27, 31);\n
    }
    
    QScrollBar:vertical {
        background-color: rgb(50, 51, 59);\n
        width: 8px;\n
        border-radius: 4px;\n
        border: none;\n
        margin: 0;\n
    }
    
    QScrollBar:horizontal {
        background-color: rgb(50, 51, 59);\n
        height: 8px;\n
        border-radius: 4px;\n
        border: none;\n
        margin: 0;\n
    }
    
    QScrollBar:handle {
        width: 8px;\n
        border-radius: 4px;\n
        background-color: #32333b;\n
    }
    
    QScrollBar::add-page:vertical {
        background-color: rgb(255, 170, 0);\n
    }
    
    QScrollBar::sub-page:vertical {
        background-color: rgb(255, 170, 0);\n
    }
    
    QScrollBar::add-page:horizontal {
        background-color: rgb(255, 170, 0);\n
    }
    
    QScrollBar::sub-page:horizontal {
        background-color: rgb(255, 170, 0);\n
    }

"""
mixer.init()


# ############## Using Qt MVC to create drag and drop playlist view
###################################################################
class PlayModel(QAbstractListModel):
    def __init__(self, data_=None):
        super(PlayModel, self).__init__(None)
        self.data_ = data_ or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.data_[index.row()]
            return text

    def rowCount(self, index):
        return len(self.data_)


class PlayLists(QListView):
    textdata = Signal(str)

    def __init__(self):
        super(PlayLists, self).__init__(parent=None)
        self.setAcceptDrops(True)
        self.setVisible(True)
        self.setStyleSheet(styles)
        self.model = PlayModel()
        self.setModel(self.model)
        self.root = ""
        self.clicked.connect(self.callback)

    def callback(self, s):
        mixer.music.load(os.path.join(self.root, s.data()))
        mixer.music.play()
        self.textdata.emit(s.data())
        self.model.layoutChanged.emit()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = []
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            for path in event.mimeData().urls():
                if path.isLocalFile():
                    files.append(path)
                else:
                    files.append(str(path))
        else:
            event.ignore()

        for file in files:
            f = QUrl.path(file)
            if f.endswith(".mp3"):
                self.root = ntpath.dirname(str(f[1:]))
                self.model.data_.append(ntpath.basename(str(f[1:])))
                self.model.layoutChanged.emit()

