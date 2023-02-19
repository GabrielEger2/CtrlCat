from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QAbstractItemView, QCheckBox, QApplication, QHBoxLayout, QHeaderView, QKeySequenceEdit,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar, QSlider, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 800))
        MainWindow.setMaximumSize(QSize(700, 800))
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(24, 24, 24);\n"
"}\n"
"\n"
"QMenuBar {\n"
"    background-color: black;\n"
"    spacing: 3px; \n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    padding: 4px 4px;\n"
"    background: transparent;\n"
"    border-radius: 2px;\n"
"    color: #FFF;\n"
"}\n"
"\n"
"QMenuBar::item:selected { \n"
"    background: #a8a8a8;\n"
"    color: black;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #888888;\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu {\n"
"    color: white;\n"
"}\n"
"\n"
"QMenu:selected {\n"
"    color: black;\n"
"	background-color: #a8a8a8;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 5px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 56);\n"
"}\n"
"\n"
"QText"
                        "Browser {\n"
"	border: 2px solid rgb(37, 39, 48);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QTextBrowser:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QTextBrowser:focus{\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}\n"
"\n"
"QTableWidget {\n"
"	border: 2px solid rgb(37, 39, 48);\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	border-radius: 5px;\n"
"	color: #FFF;\n"
"	background-color: rgb(34, 36, 44);\n"
"}\n"
"QTableWidget:hover {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QTableWidget:focus{\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}\n"
"\n"
"QHeaderView::section { \n"
"	color:white; \n"
"	background-color:#232326; \n"
"}\n"
"QTableCornerButton::section { \n"
"	background-color:#232326; \n"
"}\n"
"\n"
"QPushButton{\n"
"    color: white;\n"
"    bord"
                        "er: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"    background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QScrollBar:horizontal,\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 20px;\n"
"    margin: 20px 0 20px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal,\n"
"QScrollBar::handle:vertical {\n"
"    background: #555;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background:"
                        " none;\n"
"}\n"
"")
        self.Settings = QAction(MainWindow)
        self.Settings.setObjectName(u"Settings")
        self.actionCtrl_V_config = QAction(MainWindow)
        self.actionCtrl_V_config.setObjectName(u"actionCtrl_V_config")
        self.actionProgram_GitHub = QAction(MainWindow)
        self.actionProgram_GitHub.setObjectName(u"actionProgram_GitHub")
        self.actionCreator_Github = QAction(MainWindow)
        self.actionCreator_Github.setObjectName(u"actionCreator_Github")
        self.actionSupport_me = QAction(MainWindow)
        self.actionSupport_me.setObjectName(u"actionSupport_me")
        self.actionClose_2 = QAction(MainWindow)
        self.actionClose_2.setObjectName(u"actionClose_2")
        self.actionDark_Mode = QAction(MainWindow)
        self.actionDark_Mode.setObjectName(u"actionDark_Mode")
        self.actionWhite_Mode = QAction(MainWindow)
        self.actionWhite_Mode.setObjectName(u"actionWhite_Mode")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, 10, 20)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(400, 350))
        self.label.setStyleSheet(u"image: url(source.qr/newPrefix/Snyfe_Cute_baby_cat_playing_with_a_scissor_wearing_a_yellow_saf_c99dda6f-684d-4b94-a3a0-279ffd9eadf2.png);")
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label.setPixmap(QPixmap(u"Snyfe_Cute_baby_cat_playing_with_a_scissor_wearing_a_yellow_saf_c99dda6f-684d-4b94-a3a0-279ffd9eadf2.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label)

        self.copytext = QTextBrowser(self.centralwidget)
        self.copytext.setObjectName(u"copytext")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.copytext.sizePolicy().hasHeightForWidth())
        self.copytext.setSizePolicy(sizePolicy2)
        self.copytext.setStyleSheet(u"")
        self.copytext.setLocale(QLocale(QLocale.English, QLocale.Kenya))
        self.copytext.setReadOnly(False)

        self.verticalLayout_2.addWidget(self.copytext)

        self.EditButton = QPushButton(self.centralwidget)
        self.EditButton.setObjectName(u"EditButton")
        self.EditButton.setStyleSheet(u"")
        self.EditButton.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_2.addWidget(self.EditButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Search = QLineEdit(self.centralwidget)
        self.Search.setObjectName(u"Search")
        self.Search.setAutoFillBackground(False)
        self.Search.setStyleSheet(u"")
        self.Search.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.Search.setDragEnabled(True)
        self.Search.setReadOnly(False)
        self.Search.setPlaceholderText(u"Search for a Ctrl+C")

        self.verticalLayout.addWidget(self.Search)

        self.SQL_Table = QTableWidget(self.centralwidget)
        if (self.SQL_Table.columnCount() < 2):
            self.SQL_Table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.SQL_Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.SQL_Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.SQL_Table.setObjectName(u"SQL_Table")
        self.SQL_Table.setMinimumSize(QSize(333, 0))
        self.SQL_Table.setMaximumSize(QSize(333, 687))
        self.SQL_Table.setStyleSheet(u"")
        self.SQL_Table.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.SQL_Table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.SQL_Table.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.SQL_Table.setTabKeyNavigation(False)
        self.SQL_Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SQL_Table.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.SQL_Table.setShowGrid(True)
        self.SQL_Table.horizontalHeader().setVisible(True)
        self.SQL_Table.horizontalHeader().setCascadingSectionResizes(False)
        self.SQL_Table.horizontalHeader().setHighlightSections(True)
        self.SQL_Table.horizontalHeader().setProperty("showSortIndicator", False)
        self.SQL_Table.setColumnWidth(0, 233)
        self.SQL_Table.setColumnWidth(1, 80)

        self.verticalLayout.addWidget(self.SQL_Table)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 25))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSettings.addAction(self.Settings)
        self.menuSettings.addAction(self.actionClose_2)
        self.menuAbout.addAction(self.actionProgram_GitHub)
        self.menuAbout.addAction(self.actionCreator_Github)
        self.menuAbout.addAction(self.actionSupport_me)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CtrlCat", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionCtrl_V_config.setText(QCoreApplication.translate("MainWindow", u"Ctrl+V Config", None))
        self.actionProgram_GitHub.setText(QCoreApplication.translate("MainWindow", u"Program's GitHub", None))
        self.actionCreator_Github.setText(QCoreApplication.translate("MainWindow", u"Creator's Github", None))
        self.actionSupport_me.setText(QCoreApplication.translate("MainWindow", u"Support Me :)", None))
        self.actionClose_2.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionDark_Mode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.actionWhite_Mode.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.label.setText("")
        self.copytext.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.EditButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.Search.setText("")
        ___qtablewidgetitem = self.SQL_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ctrl+C", None));
        ___qtablewidgetitem1 = self.SQL_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(446, 198)
        Settings.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(Settings)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CtrlCCheck = QCheckBox(Settings)
        self.CtrlCCheck.setObjectName(u"CtrlCCheck")
        self.CtrlCCheck.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.CtrlCCheck.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.CtrlCCheck.setChecked(True)
        self.CtrlCCheck.setTristate(False)

        self.verticalLayout.addWidget(self.CtrlCCheck)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Settings)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout.addWidget(self.label)

        self.CopyKeySequence = QKeySequenceEdit(Settings)
        self.CopyKeySequence.setObjectName(u"CopyKeySequence")
        self.CopyKeySequence.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.CopyKeySequence.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout.addWidget(self.CopyKeySequence)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Settings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.PasteKeySequence = QKeySequenceEdit(Settings)
        self.PasteKeySequence.setObjectName(u"PasteKeySequence")
        self.PasteKeySequence.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.PasteKeySequence.setLocale(QLocale(QLocale.English, QLocale.Kenya))

        self.horizontalLayout_2.addWidget(self.PasteKeySequence)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.ChangeKeyWordSequence = QKeySequenceEdit(Settings)
        self.ChangeKeyWordSequence.setObjectName(u"ChangeKeyWordSequence")
        self.ChangeKeyWordSequence.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ChangeKeyWordSequence.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_3.addWidget(self.ChangeKeyWordSequence)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(Settings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_2.addWidget(self.label_4)

        self.CopiesSlider = QSlider(Settings)
        self.CopiesSlider.setObjectName(u"CopiesSlider")
        self.CopiesSlider.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.CopiesSlider.setMinimum(1)
        self.CopiesSlider.setMaximum(100)
        self.CopiesSlider.setValue(10)
        self.CopiesSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.CopiesSlider)

        self.CopiesSpinBox = QSpinBox(Settings)
        self.CopiesSpinBox.setObjectName(u"CopiesSpinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CopiesSpinBox.sizePolicy().hasHeightForWidth())
        self.CopiesSpinBox.setSizePolicy(sizePolicy)
        self.CopiesSpinBox.setMinimumSize(QSize(60, 21))
        self.CopiesSpinBox.setMaximumSize(QSize(16777215, 16777215))
        self.CopiesSpinBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.CopiesSpinBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.CopiesSpinBox.setReadOnly(True)
        self.CopiesSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.CopiesSpinBox.setMinimum(1)
        self.CopiesSpinBox.setMaximum(100)
        self.CopiesSpinBox.setValue(10)

        self.verticalLayout_2.addWidget(self.CopiesSpinBox)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"CtrlCat - Settings", None))
        self.CtrlCCheck.setText(QCoreApplication.translate("Settings", u"Show past Ctrl+C", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Copy KeyWord:", None))
        self.CopyKeySequence.setKeySequence(QCoreApplication.translate("Settings", u"Ctrl+C", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Paste KeyWord:", None))
        self.PasteKeySequence.setKeySequence(QCoreApplication.translate("Settings", u"Ctrl+V", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"Change Paste KeyWord:", None))
        self.ChangeKeyWordSequence.setKeySequence(QCoreApplication.translate("Settings", u"Up, Down", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"Set Max Amount of Copies:", None))
    # retranslateUi
