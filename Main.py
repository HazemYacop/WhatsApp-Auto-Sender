import os
import Creds
import threading
import pyperclip as pc
from PySide2.QtWidgets import QApplication
from Functions import Package, UserInterface


class Main:
    def __init__(self):
        super().__init__()

        # Start-Up
        Package.create_json(Creds.google_api_json_creds)  # Replace With your Credentials
        self.UserInterface = UserInterface()
        self.UserInterface.stackedWidget.setCurrentIndex(0)

        # Program location
        self.program_location = f'{os.path.expanduser("~")}\AppData\Local\Whatsapp Auto Sender'

        # Load last session
        Package.load_txt(self.UserInterface.Sheet, "Sheetname")
        Package.load_txt(self.UserInterface.Worksheet, "Worksheet")
        Package.load_txt(self.UserInterface.ContactsColumnNumber, "ContactsColumnNumber")
        Package.load_txt(self.UserInterface.StartFromRow, "StartFromRow")
        Package.load_txt(self.UserInterface.Message, "Message")

        # Button(s) Function(s)
        self.UserInterface.NextToMessagePageButton.clicked.connect(lambda: self.UserInterface.stackedWidget.setCurrentIndex(1))
        self.UserInterface.ChooseImageButton.clicked.connect(lambda: self.UserInterface.ChooseImageButton.setText(Package.ask_for_file()))
        self.UserInterface.BackToMainPageButton.clicked.connect(lambda: self.UserInterface.stackedWidget.setCurrentIndex(0))
        self.UserInterface.NextToSharePageButton.clicked.connect(lambda: self.UserInterface.stackedWidget.setCurrentIndex(2))
        self.UserInterface.CopyEmailButton.clicked.connect(lambda: [pc.copy(Creds.google_api_email), print("Email Copied Successfully")])  # Put The Email of you Creds.json
        self.UserInterface.BackToMesaagePageButton.clicked.connect(lambda: self.UserInterface.stackedWidget.setCurrentIndex(0))
        self.UserInterface.StartButton.clicked.connect(lambda: self.startup())
        self.UserInterface.BackButton.clicked.connect(lambda: self.UserInterface.stackedWidget.setCurrentIndex(0))
        self.UserInterface.HowDoesItWorkButton.clicked.connect(lambda: Package.help())

    def startup(self):
        try:
            self.required_data()
            self.UserInterface.stackedWidget.setCurrentIndex(3)
            self.UserInterface.WorkingLabel.setText("Working")
            self.UserInterface.BackButton.setDisabled(True)
            Package.save_txt("Sheetname", self.sheet)
            Package.save_txt("Worksheet", self.worksheet)
            Package.save_txt("ContactsColumnNumber", self.contacts_column_number)
            Package.save_txt("StartFromRow", self.start_from_row)
            Package.save_txt("Message", self.message)
            start = threading.Thread(target=self.main)
            start.start()
        except NotImplementedError as e:
            print(e)
            self.UserInterface.WorkingLabel.setText("Error Occured, Take a screenshot of the CMD (Black Screen) and Contact : +201150169348")
            self.UserInterface.CurrentNumberLabel.setText("")
            self.UserInterface.BackButton.setDisabled(False)

    def main(self):
        for number in self.contacts:
            self.UserInterface.CurrentNumberLabel.setText(f"Current Number : {number}")
            message_status = self.sheet_access.cell(self.start_from_row, self.confirm_column).value

            if message_status != "Message is sent":
                try:
                    Package.message_contact(number, self.image_location, self.message)
                    self.sheet_access.update_cell(self.start_from_row, self.confirm_column, "Message is sent")
                except Exception as e:
                    print(e)
                    self.sheet_access.update_cell(self.start_from_row, self.confirm_column, "Message is not sent")

            self.start_from_row += 1

        # Re Defining UI
        self.UserInterface.WorkingLabel.setText("Program Finished")
        self.UserInterface.CurrentNumberLabel.setText("")
        self.UserInterface.BackButton.setDisabled(False)

    def required_data(self):
        # Sheet access
        self.sheet = self.UserInterface.Sheet.text()
        self.worksheet = self.UserInterface.Worksheet.text()
        self.sheet_access = Package.access_google_spreadsheet(self.sheet, self.worksheet)

        # Required Data
        self.contacts_column_number = int(self.UserInterface.ContactsColumnNumber.text())
        self.confirm_column = self.contacts_column_number + 1
        self.contacts = self.sheet_access.col_values(self.contacts_column_number)
        self.start_from_row = int(self.UserInterface.StartFromRow.text())
        self.message = self.UserInterface.Message.toPlainText()
        self.image_location = self.UserInterface.ChooseImageButton.text()


if __name__ == '__main__':
    app = QApplication()
    main = Main()
    app.exec_()
