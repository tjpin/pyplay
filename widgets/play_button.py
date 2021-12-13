from PySide6.QtCore import Qt, Signal, QEvent
from PySide6.QtWidgets import *


class PlayButton(QWidget):
    clicked = Signal()
    pressed = True
    hovered = False

    def __init__(self, text, *args, callback=None):
        super(PlayButton, self).__init__()
        self.setFixedHeight(40)
        self.text = text
        self.bg_normal = "background-color: #292b31; padding-left: 10;"
        self.bg_hover = "background-color:#2c2d34; padding-left: 10;"
        self.style_down = "background-color: #ffc000; padding-left: 10;"
        self.callback = callback

        self.setStyleSheet("background-color: #292b31; padding-left: 10;")

        music = QLabel(self.text)
        music.setMinimumHeight(40)
        music.setAlignment(Qt.AlignVCenter)
        music.setStyleSheet("color: #898da2; text-align: center;")
        # music.setAlignment(Qt.AlignLeft)

        layout = QHBoxLayout()
        layout.addWidget(music)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def mousePressEvent(self, event):
        if event.MouseButtonPress:
            self.clicked.connect(self.callback)
            self.setStyleSheet(self.style_down)
            self.repaint_btn(event)
            self.clicked.emit()

    def mouseReleaseEvent(self, event):
        if event.MouseButtonRelease and self.hovered:
            self.setStyleSheet(self.bg_normal)
            self.repaint_btn(event)

    def enterEvent(self, event):
        if event.Enter:
            self.hovered = True
            self.setStyleSheet(self.bg_hover)
            self.repaint_btn(event)

    def leaveEvent(self, event):
        self.hovered = False
        if event.Leave:
            self.setStyleSheet(self.bg_normal)
            self.repaint_btn(event)

    def repaint_btn(self, event):
        if event == QEvent.Enter:
            self.repaint()
        if event == QEvent.Leave:
            self.repaint()
        if event == QEvent.MouseButtonPress:
            self.repaint()
        if event == QEvent.MouseButtonRelease:
            self.repaint()
