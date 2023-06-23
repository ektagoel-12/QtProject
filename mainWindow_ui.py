# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(899, 484)
        MainWindow.setStyleSheet(u"background-color: #27263c")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.setObjectName(u"actionOpen_2")
        self.actioninterface_ui = QAction(MainWindow)
        self.actioninterface_ui.setObjectName(u"actioninterface_ui")
        self.actionnew_ui = QAction(MainWindow)
        self.actionnew_ui.setObjectName(u"actionnew_ui")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionSave_All = QAction(MainWindow)
        self.actionSave_All.setObjectName(u"actionSave_All")
        self.actionSave_As_Template = QAction(MainWindow)
        self.actionSave_As_Template.setObjectName(u"actionSave_As_Template")
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionSave_Image = QAction(MainWindow)
        self.actionSave_Image.setObjectName(u"actionSave_Image")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionForm = QAction(MainWindow)
        self.actionForm.setObjectName(u"actionForm")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 350, 634, 53))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.viewRecordButton = QPushButton(self.layoutWidget)
        self.viewRecordButton.setObjectName(u"viewRecordButton")
        font = QFont()
        font.setPointSize(19)
        self.viewRecordButton.setFont(font)
        self.viewRecordButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0;\n"
"    color: #000000;\n"
"    border: 1px solid #000000;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.viewRecordButton)

        self.horizontalSpacer = QSpacerItem(248, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.addRecordButton = QPushButton(self.layoutWidget)
        self.addRecordButton.setObjectName(u"addRecordButton")
        self.addRecordButton.setFont(font)
        self.addRecordButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0;\n"
"    color: #000000;\n"
"    border: 1px solid #000000;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.addRecordButton)

        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(200, 70, 511, 141))
        self.imageLabel.setStyleSheet(u"")
        self.imageLabel.setPixmap(QPixmap(u":/logo/white_text.jpg"))
        self.imageLabel.setScaledContents(True)
        self.textLabel = QLabel(self.centralwidget)
        self.textLabel.setObjectName(u"textLabel")
        self.textLabel.setGeometry(QRect(120, 240, 651, 81))
        font1 = QFont()
        font1.setPointSize(21)
        self.textLabel.setFont(font1)
        self.textLabel.setStyleSheet(u"color: white")
        self.textLabel.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actioninterface_ui.setText(QCoreApplication.translate("MainWindow", u"interface.ui", None))
        self.actionnew_ui.setText(QCoreApplication.translate("MainWindow", u"new.ui", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionSave_All.setText(QCoreApplication.translate("MainWindow", u"Save All", None))
        self.actionSave_As_Template.setText(QCoreApplication.translate("MainWindow", u"Save As Template", None))
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.actionSave_Image.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionForm.setText(QCoreApplication.translate("MainWindow", u"Form", None))
        self.viewRecordButton.setText(QCoreApplication.translate("MainWindow", u"View Records", None))
        self.addRecordButton.setText(QCoreApplication.translate("MainWindow", u"Add Record", None))
        self.imageLabel.setText("")
        self.textLabel.setText(QCoreApplication.translate("MainWindow", u"Program for Testing & Analysis", None))
    # retranslateUi

