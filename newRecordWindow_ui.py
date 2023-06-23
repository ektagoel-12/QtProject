# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newRecordWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTimeEdit, QWidget)

class Ui_newRecordWindow(object):
    def setupUi(self, newRecordWindow):
        if not newRecordWindow.objectName():
            newRecordWindow.setObjectName(u"newRecordWindow")
        newRecordWindow.resize(727, 623)
        newRecordWindow.setStyleSheet(u"QWidget {\n"
"    background-color:#27263c;/* Blue background color */\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QDoubleSpinBox,\n"
"QSpinBox,\n"
"QTimeEdit {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    border: 1px solid #000000;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #FFFFFF; /* White background color */\n"
"    color: #000000; /* Black text color */\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CCCCCC; /* Light gray background color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #999999; /* Dark gray background color when pressed */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(newRecordWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(290, 420, 381, 91))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.saveRecordButton = QPushButton(self.widget)
        self.saveRecordButton.setObjectName(u"saveRecordButton")

        self.horizontalLayout_4.addWidget(self.saveRecordButton)

        self.clearPushButton = QPushButton(self.widget)
        self.clearPushButton.setObjectName(u"clearPushButton")

        self.horizontalLayout_4.addWidget(self.clearPushButton)

        self.cancelPushButton = QPushButton(self.widget)
        self.cancelPushButton.setObjectName(u"cancelPushButton")

        self.horizontalLayout_4.addWidget(self.cancelPushButton)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 40, 571, 296))
        self.formLayout = QFormLayout(self.widget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.startTimeLabel = QLabel(self.widget1)
        self.startTimeLabel.setObjectName(u"startTimeLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.startTimeLabel)

        self.startTimeEdit = QTimeEdit(self.widget1)
        self.startTimeEdit.setObjectName(u"startTimeEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.startTimeEdit)

        self.endTimeLabel = QLabel(self.widget1)
        self.endTimeLabel.setObjectName(u"endTimeLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.endTimeLabel)

        self.endTimeEdit = QTimeEdit(self.widget1)
        self.endTimeEdit.setObjectName(u"endTimeEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.endTimeEdit)

        self.batteryBeforeLabel = QLabel(self.widget1)
        self.batteryBeforeLabel.setObjectName(u"batteryBeforeLabel")
        self.batteryBeforeLabel.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.batteryBeforeLabel)

        self.batteryBeforeDoubleSpinBox = QDoubleSpinBox(self.widget1)
        self.batteryBeforeDoubleSpinBox.setObjectName(u"batteryBeforeDoubleSpinBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.batteryBeforeDoubleSpinBox)

        self.batteryAfterLabel = QLabel(self.widget1)
        self.batteryAfterLabel.setObjectName(u"batteryAfterLabel")
        self.batteryAfterLabel.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.batteryAfterLabel)

        self.batteryAfterDoubleSpinBox = QDoubleSpinBox(self.widget1)
        self.batteryAfterDoubleSpinBox.setObjectName(u"batteryAfterDoubleSpinBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.batteryAfterDoubleSpinBox)

        self.lightOnLabel = QLabel(self.widget1)
        self.lightOnLabel.setObjectName(u"lightOnLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lightOnLabel)

        self.lightsOnCheckBox = QCheckBox(self.widget1)
        self.lightsOnCheckBox.setObjectName(u"lightsOnCheckBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lightsOnCheckBox)

        self.distanceLabel = QLabel(self.widget1)
        self.distanceLabel.setObjectName(u"distanceLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.distanceLabel)

        self.distanceDoubleSpinBox = QDoubleSpinBox(self.widget1)
        self.distanceDoubleSpinBox.setObjectName(u"distanceDoubleSpinBox")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.distanceDoubleSpinBox)

        self.maxSpeedLabel = QLabel(self.widget1)
        self.maxSpeedLabel.setObjectName(u"maxSpeedLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.maxSpeedLabel)

        self.maxSpeedSpinBox = QSpinBox(self.widget1)
        self.maxSpeedSpinBox.setObjectName(u"maxSpeedSpinBox")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.maxSpeedSpinBox)

        self.avgSpeedLabel = QLabel(self.widget1)
        self.avgSpeedLabel.setObjectName(u"avgSpeedLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.avgSpeedLabel)

        self.avgSpeedSpinBox = QSpinBox(self.widget1)
        self.avgSpeedSpinBox.setObjectName(u"avgSpeedSpinBox")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.avgSpeedSpinBox)

        self.weightLabel = QLabel(self.widget1)
        self.weightLabel.setObjectName(u"weightLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.weightLabel)

        self.weightSpinBox = QSpinBox(self.widget1)
        self.weightSpinBox.setObjectName(u"weightSpinBox")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.weightSpinBox)

        self.speedModeLabel = QLabel(self.widget1)
        self.speedModeLabel.setObjectName(u"speedModeLabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.speedModeLabel)

        self.speedModeSpinBox = QSpinBox(self.widget1)
        self.speedModeSpinBox.setObjectName(u"speedModeSpinBox")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.speedModeSpinBox)

        newRecordWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(newRecordWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 727, 26))
        newRecordWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(newRecordWindow)
        self.statusbar.setObjectName(u"statusbar")
        newRecordWindow.setStatusBar(self.statusbar)

        self.retranslateUi(newRecordWindow)

        QMetaObject.connectSlotsByName(newRecordWindow)
    # setupUi

    def retranslateUi(self, newRecordWindow):
        newRecordWindow.setWindowTitle(QCoreApplication.translate("newRecordWindow", u"MainWindow", None))
        self.saveRecordButton.setText(QCoreApplication.translate("newRecordWindow", u"Save ", None))
        self.clearPushButton.setText(QCoreApplication.translate("newRecordWindow", u"Clear", None))
        self.cancelPushButton.setText(QCoreApplication.translate("newRecordWindow", u"Cancel", None))
        self.startTimeLabel.setText(QCoreApplication.translate("newRecordWindow", u"Start Time", None))
        self.startTimeEdit.setDisplayFormat(QCoreApplication.translate("newRecordWindow", u"hh:mm:ss", None))
        self.endTimeLabel.setText(QCoreApplication.translate("newRecordWindow", u"End Time", None))
        self.endTimeEdit.setDisplayFormat(QCoreApplication.translate("newRecordWindow", u"hh:mm:ss", None))
        self.batteryBeforeLabel.setText(QCoreApplication.translate("newRecordWindow", u"Battery % Before", None))
        self.batteryAfterLabel.setText(QCoreApplication.translate("newRecordWindow", u"Battery % After", None))
        self.lightOnLabel.setText(QCoreApplication.translate("newRecordWindow", u"Lights on", None))
        self.lightsOnCheckBox.setText("")
        self.distanceLabel.setText(QCoreApplication.translate("newRecordWindow", u"Distance(KM)", None))
        self.maxSpeedLabel.setText(QCoreApplication.translate("newRecordWindow", u"Max Speed(kmph)", None))
        self.avgSpeedLabel.setText(QCoreApplication.translate("newRecordWindow", u"Avg Speed(kmph)", None))
        self.weightLabel.setText(QCoreApplication.translate("newRecordWindow", u"Weight", None))
        self.speedModeLabel.setText(QCoreApplication.translate("newRecordWindow", u"Speed Mode", None))
    # retranslateUi

