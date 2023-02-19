import sys
import webbrowser

# Importing user interface file
from ui_main import Ui_MainWindow
from ui_main import Ui_Settings

# Importing classes from PySide6 modules
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtCore import QDate
from PySide6 import QtWidgets

# Importing classes from PySide6 modules
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

# Importing SQLite3 module for database operations
import sqlite3

import datetime

# Creating the class for the main window
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.create_table()
        self.load_data()

        QApplication.clipboard().dataChanged.connect(self.save_copy)

        self.ui.SQL_Table.clicked.connect(self.load_copy)
        self.ui.actionCreator_Github.triggered.connect(self.acess_creator_github)
        self.ui.actionProgram_GitHub.triggered.connect(self.acess_project_github)
        self.ui.actionSupport_me.triggered.connect(self.acess_support)
        self.ui.menuHelp.triggered.connect(self.acess_help)
        self.ui.Settings.triggered.connect(self.open_settings)
        self.ui.actionClose_2.triggered.connect(self.close_application)
        self.ui.EditButton.clicked.connect(lambda: self.update_copy(self.row))

        self.last_copied_text = ''

    # Method to create the table in the database
    def create_table(self):
        # Connecting to the database
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS copies (text TEXT, Date TEXT)")
        conn.commit()
        conn.close()
    
    # Method to load data from the database to the table widget
    def load_data(self):
        # Clear any existing items in the table widget
        self.ui.SQL_Table.clearContents()

        conn = sqlite3.connect("database.db")
        cursor = conn.execute("SELECT COUNT(*) FROM copies")
        number_of_rows = cursor.fetchone()[0]
        c = conn.cursor()
        sqlquery = f"SELECT * FROM copies LIMIT {number_of_rows}"
        self.ui.SQL_Table.setRowCount(number_of_rows)
        tablerow = 0
        for row in c.execute(sqlquery):
            self.ui.SQL_Table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.SQL_Table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            tablerow+=1
    
    def save_copy(self):
        text = QApplication.clipboard().text()
        if text and text != self.last_copied_text:
            self.last_copied_text = text
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("INSERT INTO copies (text, date) VALUES (?, ?)", (text, date))
            conn.commit()
            conn.close()
            # Insert a new row at the top of the table
            self.ui.SQL_Table.insertRow(0)
            # Create two new items with the copied text and date, and add them to the new row
            text_item = QTableWidgetItem(text)
            date_item = QTableWidgetItem(date)
            self.ui.SQL_Table.setItem(0, 0, text_item)
            self.ui.SQL_Table.setItem(0, 1, date_item)
            # Select the first cell of the new row
            self.ui.SQL_Table.setCurrentCell(0, 0)
    
    def load_copy(self, index):
        self.row = index.row()
        text = self.ui.SQL_Table.item(self.row, 0).text()
        self.ui.copytext.setText(text)

    # Method to update a user to the database and table widget
    def update_copy(self, index):
        row = self.row
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        text = self.ui.SQL_Table.item(self.row, 0).text()
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        conn.execute("UPDATE copies SET Text=?, Date=? WHERE ROWID = (SELECT ROWID FROM copies LIMIT 1 OFFSET ?)", (text, date, row))
        conn.commit()
        conn.close()
        print(row)
        self.load_data()
        self.load_data()

    # Close program
    def close_application(Self):
        sys.exit()
    
    # Open config file
    def open_settings(self):
        self.window = QMainWindow()
        self.settings = Ui_Settings()
        self.settings.setupUi(self.window)
        self.window.show()

    def acess_creator_github(self):
        webbrowser.open("https://github.com/GabrielEger2")
    def acess_project_github(self):
        webbrowser.open("https://github.com/GabrielEger2/CtrlCat")
    def acess_support(self):
        webbrowser.open("https://www.buymeacoffee.com/GabrielEger")
    def acess_help(self):
        webbrowser.open("https://github.com/GabrielEger2/CtrlCat")
    

# Creating the main window and showing it
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())