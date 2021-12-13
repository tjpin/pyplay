# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyplay.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 560)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 560))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.centralwidget)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMinimumSize(QSize(0, 50))
        self.titleBar.setMaximumSize(QSize(16777215, 50))
        self.titleBar.setStyleSheet(u"background-color: rgb(26, 27, 31);\n"
"border: none;\n"
"border-bottom: 1px solid rgb(117, 117, 117);")
        self.titleBar.setFrameShape(QFrame.NoFrame)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.titleBar)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.openFile = QPushButton(self.titleBar)
        self.openFile.setObjectName(u"openFile")
        self.openFile.setMinimumSize(QSize(28, 28))
        self.openFile.setMaximumSize(QSize(28, 28))
        self.openFile.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/assets/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openFile.setIcon(icon)
        self.openFile.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.openFile)

        self.label = QLabel(self.titleBar)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(59, 117, 176);\n"
"border: none;")

        self.horizontalLayout_8.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(217, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.titleBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(300, 0))
        self.label_2.setMaximumSize(QSize(300, 16777215))
        self.label_2.setStyleSheet(u"color: rgb(122, 122, 122);\n"
"border: none;")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(218, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.miniBtn = QPushButton(self.titleBar)
        self.miniBtn.setObjectName(u"miniBtn")
        self.miniBtn.setMinimumSize(QSize(28, 28))
        self.miniBtn.setMaximumSize(QSize(28, 28))
        self.miniBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.miniBtn.setIcon(icon1)
        self.miniBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.miniBtn)

        self.miniMaxi = QPushButton(self.titleBar)
        self.miniMaxi.setObjectName(u"miniMaxi")
        self.miniMaxi.setMinimumSize(QSize(28, 28))
        self.miniMaxi.setMaximumSize(QSize(28, 28))
        self.miniMaxi.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/full_screen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.miniMaxi.setIcon(icon2)
        self.miniMaxi.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.miniMaxi)

        self.closeBtn = QPushButton(self.titleBar)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(28, 28))
        self.closeBtn.setMaximumSize(QSize(28, 28))
        self.closeBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon3)
        self.closeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_8.addWidget(self.closeBtn)


        self.verticalLayout.addWidget(self.titleBar)

        self.root = QFrame(self.centralwidget)
        self.root.setObjectName(u"root")
        self.root.setStyleSheet(u"background-color: rgb(26, 27, 31);")
        self.root.setFrameShape(QFrame.NoFrame)
        self.root.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.root)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentRoot = QFrame(self.root)
        self.contentRoot.setObjectName(u"contentRoot")
        self.contentRoot.setFrameShape(QFrame.StyledPanel)
        self.contentRoot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentRoot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideBar = QFrame(self.contentRoot)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setMinimumSize(QSize(235, 0))
        self.sideBar.setMaximumSize(QSize(235, 16777215))
        self.sideBar.setMouseTracking(True)
        self.sideBar.setAcceptDrops(True)
        self.sideBar.setStyleSheet(u"border: none;\n"
"border-right: 1px solid rgb(94, 94, 94);")
        self.sideBar.setFrameShape(QFrame.NoFrame)
        self.sideBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.sideBar)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tree = QFrame(self.sideBar)
        self.tree.setObjectName(u"tree")
        self.tree.setStyleSheet(u"border: none;\n"
"")
        self.tree.setFrameShape(QFrame.NoFrame)
        self.tree.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.tree)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.settings01_5 = QFrame(self.tree)
        self.settings01_5.setObjectName(u"settings01_5")
        self.settings01_5.setMinimumSize(QSize(250, 30))
        self.settings01_5.setMaximumSize(QSize(250, 30))
        self.settings01_5.setStyleSheet(u"border: none;\n"
"background-color: rgb(48, 48, 56);\n"
"color: rgb(184, 184, 184);\n"
"")
        self.settings01_5.setFrameShape(QFrame.NoFrame)
        self.settings01_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.settings01_5)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.settings01_5)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"border: none;\n"
"text-align: left;\n"
"padding-left: 10px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/toggle_off_1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.pushButton)


        self.verticalLayout_9.addWidget(self.settings01_5)

        self.settings01 = QFrame(self.tree)
        self.settings01.setObjectName(u"settings01")
        self.settings01.setMinimumSize(QSize(230, 40))
        self.settings01.setMaximumSize(QSize(230, 40))
        self.settings01.setStyleSheet(u"border: none;\n"
"background-color: rgb(67, 68, 79);\n"
"border-radius: 20px;")
        self.settings01.setFrameShape(QFrame.NoFrame)
        self.settings01.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.settings01)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.repeater1 = QRadioButton(self.settings01)
        self.repeater1.setObjectName(u"repeater1")
        self.repeater1.setMinimumSize(QSize(100, 30))
        self.repeater1.setMaximumSize(QSize(100, 30))
        self.repeater1.setFont(font)
        self.repeater1.setStyleSheet(u"color: rgb(255, 202, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.repeater1.setIcon(icon5)
        self.repeater1.setAutoRepeat(False)

        self.horizontalLayout_9.addWidget(self.repeater1)

        self.repeaterOff = QRadioButton(self.settings01)
        self.repeaterOff.setObjectName(u"repeaterOff")
        self.repeaterOff.setMinimumSize(QSize(100, 30))
        self.repeaterOff.setMaximumSize(QSize(100, 30))
        self.repeaterOff.setFont(font)
        self.repeaterOff.setStyleSheet(u"color: rgb(255, 202, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/toggle-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.repeaterOff.setIcon(icon6)
        self.repeaterOff.setAutoRepeat(False)

        self.horizontalLayout_9.addWidget(self.repeaterOff)


        self.verticalLayout_9.addWidget(self.settings01, 0, Qt.AlignHCenter)

        self.settings01_2 = QFrame(self.tree)
        self.settings01_2.setObjectName(u"settings01_2")
        self.settings01_2.setMinimumSize(QSize(230, 40))
        self.settings01_2.setMaximumSize(QSize(230, 40))
        self.settings01_2.setStyleSheet(u"border: none;\n"
"background-color: rgb(67, 68, 79);\n"
"border-radius: 20px;")
        self.settings01_2.setFrameShape(QFrame.NoFrame)
        self.settings01_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.settings01_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.showTabs = QRadioButton(self.settings01_2)
        self.showTabs.setObjectName(u"showTabs")
        self.showTabs.setMinimumSize(QSize(100, 30))
        self.showTabs.setMaximumSize(QSize(100, 30))
        self.showTabs.setFont(font)
        self.showTabs.setStyleSheet(u"color: rgb(255, 202, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/reset.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.showTabs.setIcon(icon7)
        self.showTabs.setAutoRepeat(False)

        self.horizontalLayout_10.addWidget(self.showTabs)

        self.hideTabs = QRadioButton(self.settings01_2)
        self.hideTabs.setObjectName(u"hideTabs")
        self.hideTabs.setMinimumSize(QSize(100, 30))
        self.hideTabs.setMaximumSize(QSize(100, 30))
        self.hideTabs.setFont(font)
        self.hideTabs.setStyleSheet(u"color: rgb(255, 202, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/loop-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hideTabs.setIcon(icon8)
        self.hideTabs.setAutoRepeat(False)

        self.horizontalLayout_10.addWidget(self.hideTabs)


        self.verticalLayout_9.addWidget(self.settings01_2, 0, Qt.AlignHCenter)

        self.settings01_3 = QFrame(self.tree)
        self.settings01_3.setObjectName(u"settings01_3")
        self.settings01_3.setMinimumSize(QSize(230, 40))
        self.settings01_3.setMaximumSize(QSize(230, 40))
        self.settings01_3.setStyleSheet(u"border: none;\n"
"background-color: rgb(67, 68, 79);\n"
"border-radius: 20px;")
        self.settings01_3.setFrameShape(QFrame.NoFrame)
        self.settings01_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.settings01_3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tabsOn = QRadioButton(self.settings01_3)
        self.tabsOn.setObjectName(u"tabsOn")
        self.tabsOn.setMinimumSize(QSize(100, 30))
        self.tabsOn.setMaximumSize(QSize(100, 30))
        self.tabsOn.setFont(font)
        self.tabsOn.setStyleSheet(u"color: rgb(255, 202, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/tab-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabsOn.setIcon(icon9)
        self.tabsOn.setAutoRepeat(False)

        self.horizontalLayout_11.addWidget(self.tabsOn)

        self.tabsOff = QRadioButton(self.settings01_3)
        self.tabsOff.setObjectName(u"tabsOff")
        self.tabsOff.setMinimumSize(QSize(100, 30))
        self.tabsOff.setMaximumSize(QSize(100, 30))
        self.tabsOff.setFont(font)
        self.tabsOff.setStyleSheet(u"color: rgb(255, 202, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/tab-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabsOff.setIcon(icon10)
        self.tabsOff.setAutoRepeat(False)

        self.horizontalLayout_11.addWidget(self.tabsOff)


        self.verticalLayout_9.addWidget(self.settings01_3, 0, Qt.AlignHCenter)

        self.settings01_4 = QFrame(self.tree)
        self.settings01_4.setObjectName(u"settings01_4")
        self.settings01_4.setMinimumSize(QSize(230, 40))
        self.settings01_4.setMaximumSize(QSize(230, 40))
        self.settings01_4.setStyleSheet(u"border: none;\n"
"background-color: rgb(67, 68, 79);\n"
"border-radius: 20px;")
        self.settings01_4.setFrameShape(QFrame.NoFrame)
        self.settings01_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.settings01_4)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.moveTabs = QRadioButton(self.settings01_4)
        self.moveTabs.setObjectName(u"moveTabs")
        self.moveTabs.setMinimumSize(QSize(110, 30))
        self.moveTabs.setMaximumSize(QSize(110, 30))
        self.moveTabs.setFont(font)
        self.moveTabs.setStyleSheet(u"color: rgb(255, 202, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moveTabs.setIcon(icon11)
        self.moveTabs.setAutoRepeat(False)

        self.horizontalLayout_12.addWidget(self.moveTabs)

        self.moveTabsOff = QRadioButton(self.settings01_4)
        self.moveTabsOff.setObjectName(u"moveTabsOff")
        self.moveTabsOff.setMinimumSize(QSize(100, 30))
        self.moveTabsOff.setMaximumSize(QSize(110, 30))
        self.moveTabsOff.setFont(font)
        self.moveTabsOff.setStyleSheet(u"color: rgb(255, 202, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"border: none;\n"
"border-radius: 15px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
        self.moveTabsOff.setIcon(icon4)
        self.moveTabsOff.setAutoRepeat(False)

        self.horizontalLayout_12.addWidget(self.moveTabsOff)


        self.verticalLayout_9.addWidget(self.settings01_4, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 177, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.resetBtn = QPushButton(self.tree)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setMinimumSize(QSize(200, 30))
        self.resetBtn.setMaximumSize(QSize(200, 30))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.resetBtn.setFont(font2)
        self.resetBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-right: 3px solid rgb(26, 27, 31);\n"
"	color: rgb(167, 167, 167);\n"
"	border-radius: 14px;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"	border-right: 3px solid rgb(255, 192, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-right: 3px solid rgb(255, 192, 0);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/restore.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resetBtn.setIcon(icon12)
        self.resetBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_9.addWidget(self.resetBtn)


        self.verticalLayout_6.addWidget(self.tree, 0, Qt.AlignHCenter)

        self.controls = QFrame(self.sideBar)
        self.controls.setObjectName(u"controls")
        self.controls.setMinimumSize(QSize(0, 30))
        self.controls.setMaximumSize(QSize(16777215, 30))
        self.controls.setStyleSheet(u"border: none;")
        self.controls.setFrameShape(QFrame.StyledPanel)
        self.controls.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.controls)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.volumeSlider = QSlider(self.controls)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setStyleSheet(u"QSlider {\n"
"	background-color: rgb(26, 27, 31);\n"
"	border: none;\n"
"}\n"
"\n"
"QSlider::groove {\n"
"	height: 10px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(67, 68, 79);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color: rgb(255, 202, 29);\n"
"	border-radius: 5px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"}\n"
"")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(3)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.volumeSlider)

        self.volumeDisplay = QLabel(self.controls)
        self.volumeDisplay.setObjectName(u"volumeDisplay")
        self.volumeDisplay.setMinimumSize(QSize(40, 0))
        self.volumeDisplay.setMaximumSize(QSize(40, 16777215))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.volumeDisplay.setFont(font3)
        self.volumeDisplay.setStyleSheet(u"border: none;\n"
"color: rgb(255, 206, 29);")

        self.horizontalLayout_7.addWidget(self.volumeDisplay)


        self.verticalLayout_6.addWidget(self.controls)


        self.horizontalLayout.addWidget(self.sideBar)

        self.container = QFrame(self.contentRoot)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabs = QTabWidget(self.container)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setEnabled(True)
        self.tabs.setStyleSheet(u"QTabWidget {\n"
"	border: none;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"	border: none;\n"
"}\n"
"\n"
"QTabBar:tab{\n"
"	color: rgb(163, 163, 163);\n"
"	font-weight: bold;\n"
"	background-color: rgb(26, 27, 31);\n"
"}\n"
"\n"
"QTabBar:tab:selected {\n"
"	\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"")
        self.tabs.setTabPosition(QTabWidget.East)
        self.tabs.setElideMode(Qt.ElideNone)
        self.tabs.setUsesScrollButtons(False)
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(False)
        self.tabs.setTabBarAutoHide(True)
        self.allMusicTab = QWidget()
        self.allMusicTab.setObjectName(u"allMusicTab")
        self.allMusicTab.setStyleSheet(u"background-color: rgb(26, 27, 31);")
        self.verticalLayout_5 = QVBoxLayout(self.allMusicTab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea = QScrollArea(self.allMusicTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	\n"
"	background-color: rgb(26, 27, 31);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	background-color: rgb(50, 51, 59);\n"
"	width: 8px;\n"
"	border-radius: 4px;\n"
"	border: none;\n"
"	margin: 0;\n"
"}\n"
"\n"
"QScrollBar:handle {\n"
"	width: 8px;\n"
"	border-radius: 4px;\n"
"	background-color: rgb(26, 27, 31);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 737, 426))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"background-color: rgb(26, 27, 31);\n"
"border: none;")
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.addMusic = QVBoxLayout()
        self.addMusic.setSpacing(0)
        self.addMusic.setObjectName(u"addMusic")

        self.verticalLayout_8.addLayout(self.addMusic)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_7.addWidget(self.scrollArea)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        icon13 = QIcon()
        icon13.addFile(u":/icons/assets/tunes.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabs.addTab(self.allMusicTab, icon13, "")
        self.musicTab = QWidget()
        self.musicTab.setObjectName(u"musicTab")
        self.verticalLayout_11 = QVBoxLayout(self.musicTab)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.musicTab)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"border: none;")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 739, 428))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"border: none;")
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.musicFolderTab = QVBoxLayout()
        self.musicFolderTab.setSpacing(0)
        self.musicFolderTab.setObjectName(u"musicFolderTab")
        self.musicLibrary = QListWidget(self.scrollAreaWidgetContents_2)
        self.musicLibrary.setObjectName(u"musicLibrary")
        self.musicLibrary.setStyleSheet(u"QListWidget  {\n"
"	border: none;\n"
"	color: rgb(122, 122, 122);\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"QListWidget:item {\n"
"	border: none;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QListWidget:item:hover {\n"
"	background-color: rgb(48, 50, 57);\n"
"}\n"
"\n"
"QListWidget:item:selected {\n"
"	background-color: rgb(255, 202, 29);\n"
"	color: rgb(50, 51, 59);\n"
"}\n"
"\n"
"QScrollArea {\n"
"	\n"
"	background-color: rgb(26, 27, 31);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	background-color: rgb(50, 51, 59);\n"
"	width: 8px;\n"
"	border-radius: 4px;\n"
"	border: none;\n"
"	margin: 0;\n"
"}\n"
"\n"
"QScrollBar:handle {\n"
"	width: 8px;\n"
"	border-radius: 4px;\n"
"	background-color: rgb(26, 27, 31);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"")

        self.musicFolderTab.addWidget(self.musicLibrary)

        self.musicFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.musicFrame.setObjectName(u"musicFrame")
        self.musicFrame.setMinimumSize(QSize(0, 40))
        self.musicFrame.setMaximumSize(QSize(16777215, 40))
        self.musicFrame.setStyleSheet(u"")
        self.musicFrame.setFrameShape(QFrame.NoFrame)
        self.musicFrame.setFrameShadow(QFrame.Raised)
        self.musicFrame.setLineWidth(0)
        self.horizontalLayout_14 = QHBoxLayout(self.musicFrame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 0, 5, 0)
        self.running_2 = QLabel(self.musicFrame)
        self.running_2.setObjectName(u"running_2")
        self.running_2.setMinimumSize(QSize(0, 40))
        self.running_2.setMaximumSize(QSize(16777215, 40))
        self.running_2.setStyleSheet(u"font-weight: bold;\n"
"font-size: 13px;\n"
"color: rgb(255, 206, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"padding-left: 10px;")

        self.horizontalLayout_14.addWidget(self.running_2)

        self.playPause_2 = QPushButton(self.musicFrame)
        self.playPause_2.setObjectName(u"playPause_2")
        self.playPause_2.setMinimumSize(QSize(28, 28))
        self.playPause_2.setMaximumSize(QSize(28, 28))
        self.playPause_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playPause_2.setIcon(icon14)
        self.playPause_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.playPause_2)


        self.musicFolderTab.addWidget(self.musicFrame)


        self.verticalLayout_15.addLayout(self.musicFolderTab)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_11.addWidget(self.scrollArea_4)

        icon15 = QIcon()
        icon15.addFile(u":/icons/assets/music-folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabs.addTab(self.musicTab, icon15, "")
        self.playlistTab = QWidget()
        self.playlistTab.setObjectName(u"playlistTab")
        self.verticalLayout_3 = QVBoxLayout(self.playlistTab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.playlistTab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.playListWidget = QWidget()
        self.playListWidget.setObjectName(u"playListWidget")
        self.playListWidget.setGeometry(QRect(0, 0, 739, 428))
        self.playListWidget.setMouseTracking(True)
        self.playListWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.playListWidget.setAcceptDrops(True)
        self.verticalLayout_12 = QVBoxLayout(self.playListWidget)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.playlistContainer = QVBoxLayout()
        self.playlistContainer.setSpacing(0)
        self.playlistContainer.setObjectName(u"playlistContainer")
        self.playlistContainer.setContentsMargins(-1, -1, 0, -1)
        self.playBox = QVBoxLayout()
        self.playBox.setSpacing(5)
        self.playBox.setObjectName(u"playBox")

        self.playlistContainer.addLayout(self.playBox)

        self.frame_2 = QFrame(self.playListWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.running3 = QLabel(self.frame_2)
        self.running3.setObjectName(u"running3")
        self.running3.setMinimumSize(QSize(0, 30))
        self.running3.setMaximumSize(QSize(16777215, 30))
        self.running3.setStyleSheet(u"font-weight: bold;\n"
"font-size: 13px;\n"
"color: rgb(255, 206, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"padding-left: 10px;")

        self.horizontalLayout_15.addWidget(self.running3)

        self.playPause_3 = QPushButton(self.frame_2)
        self.playPause_3.setObjectName(u"playPause_3")
        self.playPause_3.setMinimumSize(QSize(28, 28))
        self.playPause_3.setMaximumSize(QSize(28, 28))
        self.playPause_3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.playPause_3.setIcon(icon14)
        self.playPause_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.playPause_3)


        self.playlistContainer.addWidget(self.frame_2)


        self.verticalLayout_12.addLayout(self.playlistContainer)

        self.scrollArea_2.setWidget(self.playListWidget)

        self.verticalLayout_3.addWidget(self.scrollArea_2)

        icon16 = QIcon()
        icon16.addFile(u":/icons/assets/playlist.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabs.addTab(self.playlistTab, icon16, "")
        self.docsTab = QWidget()
        self.docsTab.setObjectName(u"docsTab")
        self.verticalLayout_10 = QVBoxLayout(self.docsTab)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.docsTab)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"border: none;")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 739, 428))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.docsMusicList = QVBoxLayout()
        self.docsMusicList.setSpacing(0)
        self.docsMusicList.setObjectName(u"docsMusicList")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.docsMusicList.addWidget(self.label_3)


        self.verticalLayout_13.addLayout(self.docsMusicList)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea_3)

        icon17 = QIcon()
        icon17.addFile(u":/icons/assets/docs.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabs.addTab(self.docsTab, icon17, "")

        self.horizontalLayout_2.addWidget(self.tabs)


        self.horizontalLayout.addWidget(self.container)


        self.verticalLayout_2.addWidget(self.contentRoot)

        self.statusBar = QFrame(self.root)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 80))
        self.statusBar.setMaximumSize(QSize(16777215, 80))
        self.statusBar.setStyleSheet(u"border: none;\n"
"border-top: 1px solid rgb(97, 97, 97);\n"
"background-color: rgb(26, 27, 31)")
        self.statusBar.setFrameShape(QFrame.StyledPanel)
        self.statusBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.statusBar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 20, 0)
        self.playActions = QFrame(self.statusBar)
        self.playActions.setObjectName(u"playActions")
        self.playActions.setMinimumSize(QSize(0, 40))
        self.playActions.setMaximumSize(QSize(16777215, 40))
        self.playActions.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(40, 40, 50);")
        self.playActions.setFrameShape(QFrame.StyledPanel)
        self.playActions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.playActions)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.frame_4 = QFrame(self.playActions)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setStyleSheet(u"background-color: rgb(50, 51, 59);\n"
"border: none;\n"
"border-radius: 15;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.progress = QSlider(self.frame_4)
        self.progress.setObjectName(u"progress")
        font4 = QFont()
        font4.setBold(False)
        self.progress.setFont(font4)
        self.progress.setStyleSheet(u"QSlider {\n"
"	background-color: rgb(50, 51, 59);\n"
"	border: none;\n"
"}\n"
"\n"
"QSlider::groove {\n"
"	height: 10px;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(26, 27, 31);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color: rgb(255, 202, 29);\n"
"	border-radius: 5px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"}\n"
"\n"
"QSlider::sub-page {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(76, 78, 90);\n"
"}\n"
"")
        self.progress.setMaximum(0)
        self.progress.setOrientation(Qt.Horizontal)
        self.progress.setInvertedAppearance(False)
        self.progress.setInvertedControls(False)
        self.progress.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_6.addWidget(self.progress)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame = QFrame(self.playActions)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(260, 30))
        self.frame.setMaximumSize(QSize(260, 30))
        self.frame.setStyleSheet(u"background-color: rgb(50, 51, 59);\n"
"border-radius: 15;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(3, 0, 3, 0)
        self.repeater = QRadioButton(self.frame)
        self.repeater.setObjectName(u"repeater")
        self.repeater.setMinimumSize(QSize(80, 0))
        self.repeater.setMaximumSize(QSize(80, 16777215))
        font5 = QFont()
        font5.setPointSize(8)
        self.repeater.setFont(font5)
        self.repeater.setStyleSheet(u"color: rgb(176, 176, 176);\n"
"background-color: rgb(44, 45, 52);\n"
"border-radius: 15px;")
        self.repeater.setIcon(icon5)

        self.horizontalLayout_5.addWidget(self.repeater)

        self.backward = QPushButton(self.frame)
        self.backward.setObjectName(u"backward")
        self.backward.setMinimumSize(QSize(24, 24))
        self.backward.setMaximumSize(QSize(24, 24))
        self.backward.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/icons/assets/backward.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backward.setIcon(icon18)
        self.backward.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.backward)

        self.prev = QPushButton(self.frame)
        self.prev.setObjectName(u"prev")
        self.prev.setMinimumSize(QSize(24, 24))
        self.prev.setMaximumSize(QSize(24, 24))
        self.prev.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/icons/assets/prev.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.prev.setIcon(icon19)
        self.prev.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.prev)

        self.playPause = QPushButton(self.frame)
        self.playPause.setObjectName(u"playPause")
        self.playPause.setMinimumSize(QSize(28, 28))
        self.playPause.setMaximumSize(QSize(28, 28))
        self.playPause.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.playPause.setIcon(icon14)
        self.playPause.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.playPause)

        self.next = QPushButton(self.frame)
        self.next.setObjectName(u"next")
        self.next.setMinimumSize(QSize(24, 24))
        self.next.setMaximumSize(QSize(24, 24))
        self.next.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/icons/assets/next.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next.setIcon(icon20)
        self.next.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.next)

        self.forward = QPushButton(self.frame)
        self.forward.setObjectName(u"forward")
        self.forward.setMinimumSize(QSize(24, 24))
        self.forward.setMaximumSize(QSize(24, 24))
        self.forward.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(45, 47, 54);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/icons/assets/forwad.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.forward.setIcon(icon21)
        self.forward.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.forward)


        self.horizontalLayout_4.addWidget(self.frame)


        self.verticalLayout_4.addWidget(self.playActions)

        self.statusFrame = QFrame(self.statusBar)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setStyleSheet(u"border: none;")
        self.statusFrame.setFrameShape(QFrame.StyledPanel)
        self.statusFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.statusFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.running = QLabel(self.statusFrame)
        self.running.setObjectName(u"running")
        self.running.setMinimumSize(QSize(0, 40))
        self.running.setMaximumSize(QSize(16777215, 40))
        self.running.setStyleSheet(u"font-weight: bold;\n"
"font-size: 13px;\n"
"color: rgb(255, 206, 29);\n"
"background-color: rgb(26, 27, 31);\n"
"padding-left: 10px;")

        self.horizontalLayout_3.addWidget(self.running)

        self.duration = QLabel(self.statusFrame)
        self.duration.setObjectName(u"duration")
        self.duration.setMaximumSize(QSize(100, 16777215))
        self.duration.setFont(font3)
        self.duration.setStyleSheet(u"color: rgb(216, 165, 5);\n"
"border: none;\n"
"padding-right: 10px;")

        self.horizontalLayout_3.addWidget(self.duration, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.statusFrame)


        self.verticalLayout_2.addWidget(self.statusBar)


        self.verticalLayout.addWidget(self.root)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openFile.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PyPlayer 2022", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Made with Love by @Chairman Studios", None))
        self.miniBtn.setText("")
        self.miniMaxi.setText("")
        self.closeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.sideBar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.repeater1.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.repeaterOff.setText(QCoreApplication.translate("MainWindow", u"Desable", None))
        self.showTabs.setText(QCoreApplication.translate("MainWindow", u"Show Tab", None))
        self.hideTabs.setText(QCoreApplication.translate("MainWindow", u"Hide Tab", None))
        self.tabsOn.setText(QCoreApplication.translate("MainWindow", u"Tabs On", None))
        self.tabsOff.setText(QCoreApplication.translate("MainWindow", u"Tabs Off", None))
        self.moveTabs.setText(QCoreApplication.translate("MainWindow", u"Move Tab", None))
        self.moveTabsOff.setText(QCoreApplication.translate("MainWindow", u"Freeze Tab", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset Settings", None))
        self.volumeDisplay.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.allMusicTab), QCoreApplication.translate("MainWindow", u"All Music", None))
#if QT_CONFIG(tooltip)
        self.tabs.setTabToolTip(self.tabs.indexOf(self.allMusicTab), QCoreApplication.translate("MainWindow", u"Playlist", None))
#endif // QT_CONFIG(tooltip)
        self.running_2.setText("")
        self.playPause_2.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.musicTab), QCoreApplication.translate("MainWindow", u"Music", None))
        self.running3.setText("")
        self.playPause_3.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.playlistTab), QCoreApplication.translate("MainWindow", u"Playlist", None))
#if QT_CONFIG(tooltip)
        self.tabs.setTabToolTip(self.tabs.indexOf(self.playlistTab), QCoreApplication.translate("MainWindow", u"Music", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#969696;\">Delete this Lable and add anything you want.</span></p></body></html>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.docsTab), QCoreApplication.translate("MainWindow", u"Videos", None))
        self.repeater.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.backward.setText("")
        self.prev.setText("")
        self.playPause.setText("")
        self.next.setText("")
        self.forward.setText("")
        self.running.setText("")
        self.duration.setText("")
    # retranslateUi

