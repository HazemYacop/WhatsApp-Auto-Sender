# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserInterface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background: qlineargradient(spread:pad, x1:0.494318, y1:0, x2:0.506, y2:1, stop:0 rgba(204, 32, 142, 255), stop:1 rgba(103, 19, 210, 255));\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.MainPage = QWidget()
        self.MainPage.setObjectName(u"MainPage")
        self.gridLayout_4 = QGridLayout(self.MainPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.InputsLayout = QVBoxLayout()
        self.InputsLayout.setSpacing(30)
        self.InputsLayout.setObjectName(u"InputsLayout")
        self.InputsLayout.setContentsMargins(100, -1, 100, 30)
        self.Spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.InputsLayout.addItem(self.Spacer)

        self.SheetLayout = QHBoxLayout()
        self.SheetLayout.setSpacing(0)
        self.SheetLayout.setObjectName(u"SheetLayout")
        self.SheetLabel = QLabel(self.MainPage)
        self.SheetLabel.setObjectName(u"SheetLabel")
        self.SheetLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.SheetLayout.addWidget(self.SheetLabel)

        self.Sheet = QLineEdit(self.MainPage)
        self.Sheet.setObjectName(u"Sheet")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sheet.sizePolicy().hasHeightForWidth())
        self.Sheet.setSizePolicy(sizePolicy)
        self.Sheet.setMinimumSize(QSize(300, 35))
        self.Sheet.setMaximumSize(QSize(16777215, 16777215))
        self.Sheet.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background: transparent;")
        self.Sheet.setAlignment(Qt.AlignCenter)

        self.SheetLayout.addWidget(self.Sheet)


        self.InputsLayout.addLayout(self.SheetLayout)

        self.WorksheetLayout = QHBoxLayout()
        self.WorksheetLayout.setSpacing(0)
        self.WorksheetLayout.setObjectName(u"WorksheetLayout")
        self.WorksheetLabel = QLabel(self.MainPage)
        self.WorksheetLabel.setObjectName(u"WorksheetLabel")
        self.WorksheetLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.WorksheetLayout.addWidget(self.WorksheetLabel)

        self.Worksheet = QLineEdit(self.MainPage)
        self.Worksheet.setObjectName(u"Worksheet")
        sizePolicy.setHeightForWidth(self.Worksheet.sizePolicy().hasHeightForWidth())
        self.Worksheet.setSizePolicy(sizePolicy)
        self.Worksheet.setMinimumSize(QSize(300, 35))
        self.Worksheet.setMaximumSize(QSize(16777215, 16777215))
        self.Worksheet.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background: transparent;")
        self.Worksheet.setAlignment(Qt.AlignCenter)

        self.WorksheetLayout.addWidget(self.Worksheet)


        self.InputsLayout.addLayout(self.WorksheetLayout)

        self.ContactsColumnNumberLayout = QHBoxLayout()
        self.ContactsColumnNumberLayout.setSpacing(0)
        self.ContactsColumnNumberLayout.setObjectName(u"ContactsColumnNumberLayout")
        self.ContactsColumnNumberLabel = QLabel(self.MainPage)
        self.ContactsColumnNumberLabel.setObjectName(u"ContactsColumnNumberLabel")
        self.ContactsColumnNumberLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.ContactsColumnNumberLayout.addWidget(self.ContactsColumnNumberLabel)

        self.ContactsColumnNumber = QLineEdit(self.MainPage)
        self.ContactsColumnNumber.setObjectName(u"ContactsColumnNumber")
        sizePolicy.setHeightForWidth(self.ContactsColumnNumber.sizePolicy().hasHeightForWidth())
        self.ContactsColumnNumber.setSizePolicy(sizePolicy)
        self.ContactsColumnNumber.setMinimumSize(QSize(300, 35))
        self.ContactsColumnNumber.setMaximumSize(QSize(16777215, 16777215))
        self.ContactsColumnNumber.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background: transparent;")
        self.ContactsColumnNumber.setAlignment(Qt.AlignCenter)

        self.ContactsColumnNumberLayout.addWidget(self.ContactsColumnNumber)


        self.InputsLayout.addLayout(self.ContactsColumnNumberLayout)

        self.StartFromRowLayout = QHBoxLayout()
        self.StartFromRowLayout.setSpacing(0)
        self.StartFromRowLayout.setObjectName(u"StartFromRowLayout")
        self.StartFromRowLabel = QLabel(self.MainPage)
        self.StartFromRowLabel.setObjectName(u"StartFromRowLabel")
        self.StartFromRowLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")

        self.StartFromRowLayout.addWidget(self.StartFromRowLabel)

        self.StartFromRow = QLineEdit(self.MainPage)
        self.StartFromRow.setObjectName(u"StartFromRow")
        sizePolicy.setHeightForWidth(self.StartFromRow.sizePolicy().hasHeightForWidth())
        self.StartFromRow.setSizePolicy(sizePolicy)
        self.StartFromRow.setMinimumSize(QSize(300, 35))
        self.StartFromRow.setMaximumSize(QSize(16777215, 16777215))
        self.StartFromRow.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font: 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background: transparent;")
        self.StartFromRow.setAlignment(Qt.AlignCenter)

        self.StartFromRowLayout.addWidget(self.StartFromRow)


        self.InputsLayout.addLayout(self.StartFromRowLayout)

        self.Spacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.InputsLayout.addItem(self.Spacer_2)


        self.gridLayout_4.addLayout(self.InputsLayout, 0, 0, 1, 1)

        self.NextToMessageLayout = QHBoxLayout()
        self.NextToMessageLayout.setObjectName(u"NextToMessageLayout")
        self.NextToMessageLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.NextToMessageLayout.addItem(self.Spacer_3)

        self.NextToMessageButtonLayout = QVBoxLayout()
        self.NextToMessageButtonLayout.setObjectName(u"NextToMessageButtonLayout")
        self.HowDoesItWorkButton = QPushButton(self.MainPage)
        self.HowDoesItWorkButton.setObjectName(u"HowDoesItWorkButton")
        self.HowDoesItWorkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.HowDoesItWorkButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Sans Serif\";\n"
"text-decoration: underline;")

        self.NextToMessageButtonLayout.addWidget(self.HowDoesItWorkButton)

        self.NextToMessagePageButton = QPushButton(self.MainPage)
        self.NextToMessagePageButton.setObjectName(u"NextToMessagePageButton")
        self.NextToMessagePageButton.setMinimumSize(QSize(300, 40))
        self.NextToMessagePageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.NextToMessagePageButton.setStyleSheet(u"QPushButton#NextToMessagePageButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#NextToMessagePageButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.NextToMessageButtonLayout.addWidget(self.NextToMessagePageButton)


        self.NextToMessageLayout.addLayout(self.NextToMessageButtonLayout)

        self.Spacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.NextToMessageLayout.addItem(self.Spacer_4)


        self.gridLayout_4.addLayout(self.NextToMessageLayout, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.MainPage)
        self.MessagePage = QWidget()
        self.MessagePage.setObjectName(u"MessagePage")
        self.gridLayout_3 = QGridLayout(self.MessagePage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.MessageInputLayout = QVBoxLayout()
        self.MessageInputLayout.setSpacing(50)
        self.MessageInputLayout.setObjectName(u"MessageInputLayout")
        self.MessageInputLayout.setContentsMargins(-1, 20, -1, 20)
        self.ChooseImageLayout = QVBoxLayout()
        self.ChooseImageLayout.setSpacing(6)
        self.ChooseImageLayout.setObjectName(u"ChooseImageLayout")
        self.ChooseImageLayout.setContentsMargins(-1, -1, -1, 0)
        self.ChooseImageLabel = QLabel(self.MessagePage)
        self.ChooseImageLabel.setObjectName(u"ChooseImageLabel")
        self.ChooseImageLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.ChooseImageLabel.setAlignment(Qt.AlignCenter)

        self.ChooseImageLayout.addWidget(self.ChooseImageLabel)

        self.ChooseImageButton = QPushButton(self.MessagePage)
        self.ChooseImageButton.setObjectName(u"ChooseImageButton")
        self.ChooseImageButton.setMinimumSize(QSize(300, 40))
        self.ChooseImageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ChooseImageButton.setStyleSheet(u"QPushButton#ChooseImageButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#ChooseImageButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.ChooseImageLayout.addWidget(self.ChooseImageButton)


        self.MessageInputLayout.addLayout(self.ChooseImageLayout)

        self.MessageLayout = QVBoxLayout()
        self.MessageLayout.setSpacing(6)
        self.MessageLayout.setObjectName(u"MessageLayout")
        self.WriteYourMessageLabel = QLabel(self.MessagePage)
        self.WriteYourMessageLabel.setObjectName(u"WriteYourMessageLabel")
        self.WriteYourMessageLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.WriteYourMessageLabel.setAlignment(Qt.AlignCenter)

        self.MessageLayout.addWidget(self.WriteYourMessageLabel)

        self.Message = QPlainTextEdit(self.MessagePage)
        self.Message.setObjectName(u"Message")
        self.Message.setStyleSheet(u"background: white;\n"
"border: none;\n"
"border-radius: 10px;\n"
"font: 87 11pt \"Segoe UI Black\";")

        self.MessageLayout.addWidget(self.Message)


        self.MessageInputLayout.addLayout(self.MessageLayout)


        self.gridLayout_3.addLayout(self.MessageInputLayout, 0, 0, 1, 1)

        self.NextToShareLayout = QHBoxLayout()
        self.NextToShareLayout.setObjectName(u"NextToShareLayout")
        self.NextToShareLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.NextToShareLayout.addItem(self.Spacer_5)

        self.BackToMainPageButton = QPushButton(self.MessagePage)
        self.BackToMainPageButton.setObjectName(u"BackToMainPageButton")
        self.BackToMainPageButton.setMinimumSize(QSize(300, 40))
        self.BackToMainPageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackToMainPageButton.setStyleSheet(u"QPushButton#BackToMainPageButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#BackToMainPageButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.NextToShareLayout.addWidget(self.BackToMainPageButton)

        self.NextToSharePageButton = QPushButton(self.MessagePage)
        self.NextToSharePageButton.setObjectName(u"NextToSharePageButton")
        self.NextToSharePageButton.setMinimumSize(QSize(300, 40))
        self.NextToSharePageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.NextToSharePageButton.setStyleSheet(u"QPushButton#NextToSharePageButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#NextToSharePageButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.NextToShareLayout.addWidget(self.NextToSharePageButton)

        self.Spacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.NextToShareLayout.addItem(self.Spacer_6)


        self.gridLayout_3.addLayout(self.NextToShareLayout, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.MessagePage)
        self.ShareEmailPage = QWidget()
        self.ShareEmailPage.setObjectName(u"ShareEmailPage")
        self.gridLayout_5 = QGridLayout(self.ShareEmailPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Spacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.Spacer_7, 2, 0, 1, 1)

        self.ShareEmailLayout = QVBoxLayout()
        self.ShareEmailLayout.setSpacing(60)
        self.ShareEmailLayout.setObjectName(u"ShareEmailLayout")
        self.ShareEmailLabel = QLabel(self.ShareEmailPage)
        self.ShareEmailLabel.setObjectName(u"ShareEmailLabel")
        self.ShareEmailLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.ShareEmailLabel.setAlignment(Qt.AlignCenter)

        self.ShareEmailLayout.addWidget(self.ShareEmailLabel)

        self.CopyEmailButton = QPushButton(self.ShareEmailPage)
        self.CopyEmailButton.setObjectName(u"CopyEmailButton")
        self.CopyEmailButton.setMinimumSize(QSize(300, 40))
        self.CopyEmailButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.CopyEmailButton.setStyleSheet(u"QPushButton#CopyEmailButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#CopyEmailButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.ShareEmailLayout.addWidget(self.CopyEmailButton)


        self.gridLayout_5.addLayout(self.ShareEmailLayout, 1, 0, 1, 1)

        self.StartLayout = QHBoxLayout()
        self.StartLayout.setObjectName(u"StartLayout")
        self.StartLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StartLayout.addItem(self.Spacer_10)

        self.BackToMesaagePageButton = QPushButton(self.ShareEmailPage)
        self.BackToMesaagePageButton.setObjectName(u"BackToMesaagePageButton")
        self.BackToMesaagePageButton.setMinimumSize(QSize(300, 40))
        self.BackToMesaagePageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackToMesaagePageButton.setStyleSheet(u"QPushButton#BackToMesaagePageButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#BackToMesaagePageButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.StartLayout.addWidget(self.BackToMesaagePageButton)

        self.StartButton = QPushButton(self.ShareEmailPage)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setMinimumSize(QSize(300, 40))
        self.StartButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.StartButton.setStyleSheet(u"QPushButton#StartButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#StartButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.StartLayout.addWidget(self.StartButton)

        self.Spacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.StartLayout.addItem(self.Spacer_9)


        self.gridLayout_5.addLayout(self.StartLayout, 3, 0, 1, 1)

        self.Spacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.Spacer_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.ShareEmailPage)
        self.StatusPage = QWidget()
        self.StatusPage.setObjectName(u"StatusPage")
        self.gridLayout_2 = QGridLayout(self.StatusPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Spacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.Spacer_13, 0, 0, 1, 1)

        self.StatusLayout = QVBoxLayout()
        self.StatusLayout.setSpacing(50)
        self.StatusLayout.setObjectName(u"StatusLayout")
        self.WorkingLabel = QLabel(self.StatusPage)
        self.WorkingLabel.setObjectName(u"WorkingLabel")
        self.WorkingLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.WorkingLabel.setAlignment(Qt.AlignCenter)

        self.StatusLayout.addWidget(self.WorkingLabel)

        self.CurrentNumberLabel = QLabel(self.StatusPage)
        self.CurrentNumberLabel.setObjectName(u"CurrentNumberLabel")
        self.CurrentNumberLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent;\n"
"font: 87 14pt \"Segoe UI Black\";")
        self.CurrentNumberLabel.setAlignment(Qt.AlignCenter)

        self.StatusLayout.addWidget(self.CurrentNumberLabel)


        self.gridLayout_2.addLayout(self.StatusLayout, 1, 0, 1, 1)

        self.Spacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.Spacer_14, 2, 0, 1, 1)

        self.BackButtonLayout = QHBoxLayout()
        self.BackButtonLayout.setObjectName(u"BackButtonLayout")
        self.BackButtonLayout.setContentsMargins(-1, -1, -1, 40)
        self.Spacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BackButtonLayout.addItem(self.Spacer_11)

        self.BackButton = QPushButton(self.StatusPage)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setMinimumSize(QSize(300, 40))
        self.BackButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.BackButton.setStyleSheet(u"QPushButton#BackButton{\n"
"	border: none;\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"	color: #000\n"
"}\n"
"QPushButton#BackButton::hover{\n"
"	background-color: transparent;\n"
"	border: 1px solid #fff;\n"
"	color: #fff;\n"
"}")

        self.BackButtonLayout.addWidget(self.BackButton)

        self.Spacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BackButtonLayout.addItem(self.Spacer_12)


        self.gridLayout_2.addLayout(self.BackButtonLayout, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.StatusPage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SheetLabel.setText(QCoreApplication.translate("MainWindow", u"Sheet :", None))
        self.Sheet.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.WorksheetLabel.setText(QCoreApplication.translate("MainWindow", u"Worksheet :", None))
        self.Worksheet.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ContactsColumnNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Contacts Column Number :", None))
        self.ContactsColumnNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.StartFromRowLabel.setText(QCoreApplication.translate("MainWindow", u"Start From Row :", None))
        self.StartFromRow.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.HowDoesItWorkButton.setText(QCoreApplication.translate("MainWindow", u"How does it work ?", None))
        self.NextToMessagePageButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.ChooseImageLabel.setText(QCoreApplication.translate("MainWindow", u"Choose Image :", None))
        self.ChooseImageButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.WriteYourMessageLabel.setText(QCoreApplication.translate("MainWindow", u"Write Your Message :", None))
        self.BackToMainPageButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.NextToSharePageButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.ShareEmailLabel.setText(QCoreApplication.translate("MainWindow", u"Please Share The Program's Email to the sheet :", None))
        self.CopyEmailButton.setText(QCoreApplication.translate("MainWindow", u"Copy Email", None))
        self.BackToMesaagePageButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.WorkingLabel.setText(QCoreApplication.translate("MainWindow", u"Working ...", None))
        self.CurrentNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Current Number :", None))
        self.BackButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

