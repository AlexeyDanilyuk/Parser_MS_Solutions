# Form implementation generated from reading ui file 'msud_gui.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 537)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 485, 191))
        self.groupBox.setObjectName("groupBox")
        self.cbTypeCourtProc = QtWidgets.QComboBox(self.groupBox)
        self.cbTypeCourtProc.setGeometry(QtCore.QRect(15, 40, 181, 22))
        self.cbTypeCourtProc.setObjectName("cbTypeCourtProc")
        self.cbTypeCourtProc.addItem("")
        self.cbTypeCourtProc.addItem("")
        self.cbTypeCourtProc.addItem("")
        self.cbTypeCourtProc.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(14, 20, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 161, 16))
        self.label_2.setObjectName("label_2")
        self.dtBegin = QtWidgets.QDateEdit(self.groupBox)
        self.dtBegin.setGeometry(QtCore.QRect(253, 40, 90, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.dtBegin.setFont(font)
        self.dtBegin.setObjectName("dtBegin")
        self.dtEnd = QtWidgets.QDateEdit(self.groupBox)
        self.dtEnd.setGeometry(QtCore.QRect(371, 40, 90, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.dtEnd.setFont(font)
        self.dtEnd.setObjectName("dtEnd")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(240, 40, 21, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(350, 40, 21, 20))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(15, 70, 461, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 54, 15))
        self.label_5.setObjectName("label_5")
        self.lnSubDomain = QtWidgets.QLineEdit(self.groupBox_2)
        self.lnSubDomain.setGeometry(QtCore.QRect(240, 17, 190, 20))
        self.lnSubDomain.setObjectName("lnSubDomain")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 50, 15))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 62, 81, 15))
        self.label_7.setObjectName("label_7")
        self.lnHost = QtWidgets.QLineEdit(self.groupBox_2)
        self.lnHost.setGeometry(QtCore.QRect(100, 59, 190, 20))
        self.lnHost.setText("")
        self.lnHost.setObjectName("lnHost")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(300, 61, 110, 15))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 81, 52, 15))
        self.label_9.setObjectName("label_9")
        self.lnPathDB = QtWidgets.QLineEdit(self.groupBox_2)
        self.lnPathDB.setGeometry(QtCore.QRect(100, 80, 271, 20))
        self.lnPathDB.setObjectName("lnPathDB")
        self.lnNumSU = QtWidgets.QLineEdit(self.groupBox_2)
        self.lnNumSU.setGeometry(QtCore.QRect(100, 17, 61, 20))
        self.lnNumSU.setObjectName("lnNumSU")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(380, 83, 73, 15))
        self.label_13.setObjectName("label_13")
        self.txtSiteSU = QtWidgets.QLabel(self.groupBox_2)
        self.txtSiteSU.setGeometry(QtCore.QRect(100, 40, 331, 16))
        self.txtSiteSU.setText("")
        self.txtSiteSU.setObjectName("txtSiteSU")
        self.viewResult = QtWidgets.QColumnView(self.centralwidget)
        self.viewResult.setGeometry(QtCore.QRect(9, 220, 351, 192))
        self.viewResult.setObjectName("viewResult")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 200, 116, 15))
        self.label_10.setObjectName("label_10")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 213, 120, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 49, 15))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 25, 15))
        self.label_12.setObjectName("label_12")
        self.lblSiteTotal = QtWidgets.QLabel(self.groupBox_3)
        self.lblSiteTotal.setGeometry(QtCore.QRect(60, 20, 47, 13))
        self.lblSiteTotal.setObjectName("lblSiteTotal")
        self.lblSiteTotal_2 = QtWidgets.QLabel(self.groupBox_3)
        self.lblSiteTotal_2.setGeometry(QtCore.QRect(60, 40, 47, 13))
        self.lblSiteTotal_2.setObjectName("lblSiteTotal_2")
        self.btnCompare = QtWidgets.QPushButton(self.centralwidget)
        self.btnCompare.setGeometry(QtCore.QRect(370, 300, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnCompare.setFont(font)
        self.btnCompare.setObjectName("btnCompare")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(250, 420, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.mnuMenu = QtWidgets.QMenu(self.menubar)
        self.mnuMenu.setObjectName("mnuMenu")
        self.mnuService = QtWidgets.QMenu(self.menubar)
        self.mnuService.setObjectName("mnuService")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mnuDBset = QtGui.QAction(MainWindow)
        self.mnuDBset.setObjectName("mnuDBset")
        self.mnuListDB = QtGui.QAction(MainWindow)
        self.mnuListDB.setObjectName("mnuListDB")
        self.mnuExit = QtGui.QAction(MainWindow)
        self.mnuExit.setObjectName("mnuExit")
        self.mnuMenu.addAction(self.mnuExit)
        self.mnuService.addAction(self.mnuDBset)
        self.mnuService.addAction(self.mnuListDB)
        self.menubar.addAction(self.mnuMenu.menuAction())
        self.menubar.addAction(self.mnuService.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сравнение решений"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры выбора дел"))
        self.cbTypeCourtProc.setItemText(0, _translate("MainWindow", "Уголовные дела"))
        self.cbTypeCourtProc.setItemText(1, _translate("MainWindow", "Гражданские дела"))
        self.cbTypeCourtProc.setItemText(2, _translate("MainWindow", "Административные дела"))
        self.cbTypeCourtProc.setItemText(3, _translate("MainWindow", "Материалы"))
        self.label.setText(_translate("MainWindow", "Вид судебного производства"))
        self.label_2.setText(_translate("MainWindow", "Дата принятия решения"))
        self.label_3.setText(_translate("MainWindow", "C"))
        self.label_4.setText(_translate("MainWindow", "По"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Реквизиты БД и сайта судебного участка"))
        self.label_5.setText(_translate("MainWindow", "Номер СУ"))
        self.label_6.setText(_translate("MainWindow", "Адрес СУ"))
        self.label_7.setText(_translate("MainWindow", "Адрес сервера"))
        self.label_8.setText(_translate("MainWindow", "(IP, либо имя хоста)"))
        self.label_9.setText(_translate("MainWindow", "Путь к БД"))
        self.label_13.setText(_translate("MainWindow", "(либо алиас)"))
        self.label_10.setText(_translate("MainWindow", "Результат сравнения"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Итог"))
        self.label_11.setText(_translate("MainWindow", "На сайте"))
        self.label_12.setText(_translate("MainWindow", "В БД"))
        self.lblSiteTotal.setText(_translate("MainWindow", "TextLabel"))
        self.lblSiteTotal_2.setText(_translate("MainWindow", "TextLabel"))
        self.btnCompare.setText(_translate("MainWindow", "Сравнить!\n"
"Compare!\n"
"Vergleichen!\n"
"比較!"))
        self.btnExit.setText(_translate("MainWindow", "Тут есть\n"
"Выход!"))
        self.mnuMenu.setTitle(_translate("MainWindow", "Меню"))
        self.mnuService.setTitle(_translate("MainWindow", "Сервис"))
        self.mnuDBset.setText(_translate("MainWindow", "Настройки подключения к БД"))
        self.mnuListDB.setText(_translate("MainWindow", "Список БД"))
        self.mnuExit.setText(_translate("MainWindow", "Выход"))
