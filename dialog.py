# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 200)
        MainWindow.setMinimumSize(QSize(600, 200))
        MainWindow.setMaximumSize(QSize(600, 200))
        MainWindow.setStyleSheet(u"background-color: rgb(58, 58, 58);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame *{\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"}\n"
"\n"
"QWidget *{\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.centralwidget)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 30))
        self.title_bar.setMaximumSize(QSize(16777215, 30))
        self.title_bar.setStyleSheet(u"")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.label_2 = QLabel(self.title_bar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/assets/play.svg"))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.title_bar)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(375, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.dialogMini = QPushButton(self.title_bar)
        self.dialogMini.setObjectName(u"dialogMini")
        self.dialogMini.setMinimumSize(QSize(28, 28))
        self.dialogMini.setMaximumSize(QSize(28, 28))
        self.dialogMini.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
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
        icon.addFile(u":/icons/assets/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dialogMini.setIcon(icon)
        self.dialogMini.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.dialogMini)

        self.dialogClose = QPushButton(self.title_bar)
        self.dialogClose.setObjectName(u"dialogClose")
        self.dialogClose.setMinimumSize(QSize(30, 28))
        self.dialogClose.setMaximumSize(QSize(30, 28))
        self.dialogClose.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(26, 27, 31);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 94, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dialogClose.setIcon(icon1)
        self.dialogClose.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.dialogClose)


        self.verticalLayout.addWidget(self.title_bar)

        self.inputFrame = QFrame(self.centralwidget)
        self.inputFrame.setObjectName(u"inputFrame")
        self.inputFrame.setMinimumSize(QSize(0, 100))
        self.inputFrame.setMaximumSize(QSize(16777215, 100))
        self.inputFrame.setFrameShape(QFrame.NoFrame)
        self.inputFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.inputFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_4 = QFrame(self.inputFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.folder1 = QLineEdit(self.frame_4)
        self.folder1.setObjectName(u"folder1")
        self.folder1.setMinimumSize(QSize(0, 30))
        self.folder1.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.folder1.setFont(font)
        self.folder1.setStyleSheet(u"border: 1px solid rgb(255, 170, 0);\n"
"border-radius: 15px;\n"
"padding-left: 20px;\n"
"background-color: rgb(50, 51, 59);\n"
"color: rgb(171, 171, 171); ")
        self.folder1.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.folder1)

        self.folder2 = QLineEdit(self.frame_4)
        self.folder2.setObjectName(u"folder2")
        self.folder2.setMinimumSize(QSize(0, 30))
        self.folder2.setMaximumSize(QSize(16777215, 30))
        self.folder2.setFont(font)
        self.folder2.setStyleSheet(u"border: 1px solid rgb(255, 170, 0);\n"
"border-radius: 15px;\n"
"padding-left: 20px;\n"
"background-color: rgb(50, 51, 59);\n"
"color: rgb(171, 171, 171); ")
        self.folder2.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.folder2)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.inputFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(40, 0))
        self.frame_3.setMaximumSize(QSize(40, 16777215))
        self.frame_3.setSizeIncrement(QSize(40, 0))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.selectFolder = QPushButton(self.frame_3)
        self.selectFolder.setObjectName(u"selectFolder")
        self.selectFolder.setMinimumSize(QSize(28, 28))
        self.selectFolder.setMaximumSize(QSize(28, 28))
        self.selectFolder.setStyleSheet(u"QPushButton {\n"
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
"	background-color: rgb(50, 51, 59);\n"
"}\n"
"\n"
"QToolTip {\n"
"	background-color: rgb(26, 27, 31);\n"
"	color: rgb(255, 192, 0);\n"
"	min-width: 100px;\n"
"	min-height: 20px;\n"
"	border: 2px solid rgb(255, 85, 0) ;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/music_folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.selectFolder.setIcon(icon2)
        self.selectFolder.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.selectFolder)

        self.selectFolder2 = QPushButton(self.frame_3)
        self.selectFolder2.setObjectName(u"selectFolder2")
        self.selectFolder2.setMinimumSize(QSize(28, 28))
        self.selectFolder2.setMaximumSize(QSize(28, 28))
        self.selectFolder2.setStyleSheet(u"QPushButton {\n"
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
"	background-color: rgb(50, 51, 59);\n"
"}\n"
"\n"
"QToolTip {\n"
"	background-color: rgb(26, 27, 31);\n"
"	color: rgb(255, 192, 0);\n"
"	min-width: 120px;\n"
"	min-height: 20px;\n"
"	border: 2px solid rgb(255, 85, 0) ;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"}")
        self.selectFolder2.setIcon(icon2)
        self.selectFolder2.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.selectFolder2)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.inputFrame)

        self.buttonFrame = QFrame(self.centralwidget)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttonFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cancelBtn = QPushButton(self.buttonFrame)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(150, 40))
        self.cancelBtn.setMaximumSize(QSize(150, 40))
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 51, 59);\n"
"	border: 2px solid rgb(255, 0, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(171, 171, 171);\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.cancelBtn.setIcon(icon2)
        self.cancelBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.confirm = QPushButton(self.buttonFrame)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setMinimumSize(QSize(150, 40))
        self.confirm.setMaximumSize(QSize(150, 40))
        self.confirm.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 51, 59);\n"
"	border: 2px solid rgb(0, 255, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(171, 171, 171);\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(74, 74, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/tick-green.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.confirm.setIcon(icon3)
        self.confirm.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.confirm)


        self.verticalLayout.addWidget(self.buttonFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#616161;\">From Chairman studios</span></p></body></html>", None))
        self.dialogMini.setText("")
        self.dialogClose.setText("")
        self.folder1.setText("")
        self.folder1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"paste music folder 1", None))
        self.folder2.setText("")
        self.folder2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"paste music folder 2", None))
#if QT_CONFIG(tooltip)
        self.selectFolder.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select Folder 1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.selectFolder.setText("")
#if QT_CONFIG(tooltip)
        self.selectFolder2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select Folder 2</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.selectFolder2.setText("")
        self.cancelBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
    # retranslateUi

