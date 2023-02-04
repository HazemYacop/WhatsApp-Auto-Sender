import os
import json
import gspread
import webbrowser
from tqdm import tk
import tkinter as tk
import win32clipboard
import pywhatkit as pyw
from PySide2 import QtGui
from selenium import webdriver
from tkinter import filedialog
from PySide2.QtWidgets import *
from selenium_stealth import stealth
from UserInterface import Ui_MainWindow
from webdriver_manager.chrome import ChromeDriverManager
from oauth2client.service_account import ServiceAccountCredentials


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
    def control_chrome(profile):
        chrome_path = f"{os.path.expanduser('~')}\AppData\Local\Google\Chrome"
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument(f"user-data-dir={chrome_path}\\{profile}")
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        stealth(chrome,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        return chrome

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
        self.setWindowIcon(QtGui.QIcon("Icon.png"))
        self.show()
