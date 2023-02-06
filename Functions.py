import os
import json
import wsgiref
import gspread
import webbrowser
from tqdm import tk
import tkinter as tk
import win32clipboard
import pywhatkit as pyw
import wsgiref.simple_server
from tkinter import filedialog
from PySide2.QtWidgets import *
from UserInterface import Ui_MainWindow
from oauth2client.service_account import ServiceAccountCredentials
from PySide2.QtCore import QParallelAnimationGroup, QPropertyAnimation, QEasingCurve, QPoint


class Package:
    @staticmethod
    def create_json(credentials):
        path = f"{os.path.expanduser('~')}\AppData\Local\Whatsapp Auto Sender"

        # Creating Json File
        try:
            os.mkdir(path)
        except FileExistsError:
            try:
                with open(f"{path}\Creds.json", "w") as j:
                    j.write(json.dumps(credentials))

            except FileExistsError:
                pass

    @staticmethod
    def load_txt(user_interface, name):
        try:
            with open(f'{os.path.expanduser("~")}\AppData\Local\Whatsapp Auto Sender\{name}.txt', 'r+',
                      encoding="utf-8") as file:
                try:
                    user_interface.setText(str(file.read()))
                except AttributeError:
                    user_interface.setPlainText(str(file.read()))
        except FileNotFoundError:
            pass

    @staticmethod
    def save_txt(name, value):
        with open(f'{os.path.expanduser("~")}\AppData\Local\Whatsapp Auto Sender\{name}.txt', 'w+',
                  encoding="utf-8") as file:
            file.writelines(str(value))

    @staticmethod
    def access_google_spreadsheet(sheet, worksheet):
        scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file",
                 "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            f"{os.path.expanduser('~')}\AppData\Local\Whatsapp Auto Sender\Creds.json", scope)
        client = gspread.authorize(credentials)
        sheet_acess = client.open(sheet).worksheet(worksheet)
        return sheet_acess

    @staticmethod
    def ask_for_file():
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        file = filedialog.askopenfilename()
        if file != "":
            return file.replace('/', '\\')
        else:
            return "..."

    @staticmethod
    def message_contact(number, image, message):
        # Sending message
        if message != "":
            pyw.sendwhatmsg_instantly(number, message, 20, True, 5)
        elif image != "...":
            pyw.sendwhats_image(number, image, wait_time=30, tab_close=True, close_time=3)
        else:
            pyw.sendwhatmsg_instantly(number, message, 20, True, 5)
            pyw.sendwhats_image(number, image, wait_time=30, tab_close=True, close_time=3)

    @staticmethod
    def help():
        # webbrowser.open('https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python')
        print("This will be available in the future")


class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UserInterface, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Whatsapp Auto Sender")
        self.show()

    def transition(self, ui_element):
        self.anim_group = QParallelAnimationGroup()

        for element in ui_element:
            self.element = element
            x = self.element.x()
            y = self.element.y()
            element.move(x - 50, y)

        for element in ui_element:
            effect = QGraphicsOpacityEffect(element)
            self.element = element
            x = self.element.x()
            y = self.element.y()
            self.element.setGraphicsEffect(effect)
            self.anim_1 = QPropertyAnimation(effect, b"opacity")
            self.anim_1.setStartValue(0)
            self.anim_1.setEndValue(1)
            self.anim_1.setDuration(300)
            self.child = element
            self.anim = QPropertyAnimation(self.child, b"pos")
            self.anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.anim.setEndValue(QPoint(x + 50, y))
            self.anim.setDuration(300)
            self.anim_group.addAnimation(self.anim_1)
            self.anim_group.addAnimation(self.anim)

        self.anim_group.start()
