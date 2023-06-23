# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 598)
        MainWindow.setStyleSheet(u"\n"
"            QTableView {\n"
"                background-color: #ffffff; /* White background color */\n"
"                border: 1px solid #000000;\n"
"            }\n"
"\n"
"            QHeaderView::section {\n"
"                background-color: #f2f2f2; /* Light gray background color */\n"
"                color: #000000; /* Black text color */\n"
"                border: none;\n"
"                padding: 8px;\n"
"                font-weight: bold;\n"
"            }\n"
"\n"
"            QTableWidgetItem {\n"
"                padding: 4px;\n"
"            }\n"
"     \n"
"            QPushButton {\n"
"                background-color: #FFFFFF; /* White background color */\n"
"                color: #000000; /* Black text color */\n"
"                border: none;\n"
"                padding: 8px;\n"
"                font-size: 12px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: #CCCCCC; /* Light gray background color on hover */\n"
"            }\n"
"\n"
""
                        "            QPushButton:pressed {\n"
"                background-color: #999999; /* Dark gray background color when pressed */\n"
"            }\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 20, 781, 391))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

