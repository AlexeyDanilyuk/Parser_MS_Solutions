import datetime
import os
import socket

import sys

from PyQt6.QtCore import QDate

import parse_msite
from msud_gui import *
from parse_msite import ParserMS

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

delo_dict = {
    'Уголовные дела': ['U1', '1540006', '1'],
    'Гражданские дела': ['G1', '1540005', '2'],
    'Административные дела': ['ADM', '1500001', '5'],
    'Материалы': ['M', '1610001', '9']
}


def create_config(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "number_su", "")
    config.set("Settings", "subdomain_url_su", "")
    config.set("Settings", "address_server", "")
    config.set("Settings", "path_db_amirs", "")
    config.set("Settings", "user", "")
    config.set("Settings", "password", "")

    with open(path, "w") as config_file:
        config.write(config_file)


def update_config(path, number_su, subdomain_url_su, address_server, path_db_amirs, user, password):
    """
    Update a config file
    """
    config = configparser.ConfigParser()
    config.read(path)
    config.set("Settings", "number_su", number_su)
    config.set("Settings", "subdomain_url_su", subdomain_url_su)
    config.set("Settings", "address_server", address_server)
    config.set("Settings", "path_db_amirs", path_db_amirs)
    config.set("Settings", "user", user)
    config.set("Settings", "password", password)

    with open(path, "w") as config_file:
        config.write(config_file)


def read_config(path):
    """
    Create, read, update config
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)

    number_su = config.get("Settings", "number_su")
    subdomain_url_su = config.get("Settings", "subdomain_url_su")
    address_server = config.get("Settings", "address_server")
    path_db_amirs = config.get("Settings", "path_db_amirs")
    user = config.get("Settings", "user")
    password = config.get("Settings", "password")

    with open(path, "w") as config_file:
        config.write(config_file)

    return [number_su, subdomain_url_su, address_server, path_db_amirs, user, password]


def get_ip_server():
    ipv4_addresses = [i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None) if i[0] == socket.AF_INET]
    ipv4_addresses = ipv4_addresses[0].split('.')
    ipv4_addresses[3] = '2'

    return '.'.join(ipv4_addresses)


class ClientWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, number_su, subdomain_url_su, address_server, path_db_amirs, user, password, conf_path):
        super().__init__()
        self.number_su = number_su
        self.subdomain_url_su = subdomain_url_su
        self.path_db_amirs = path_db_amirs
        self.config_path = conf_path
        self.user = user
        self.password = password
        self.setupUi(self)
        self.dtBegin.setDate(QDate(datetime.datetime.now().year, 1, 1))
        self.dtEnd.setDate(QDate(datetime.datetime.now().year, 12, 31))
        self.lnNumSU.setText(number_su)
        self.lnSubDomain.setText(subdomain_url_su)
        self.lnUser.setText(user)
        self.lnPassword.setText(password)
        if not self.lnNumSU.text().isspace() and not self.lnSubDomain.text().isspace():
            self.num_su_change()
        else:
            self.txtSiteSU.setText('')
        self.lnPathDB.setText(path_db_amirs)
        self.lnNumSU.textChanged.connect(self.num_su_change)
        self.lnSubDomain.textChanged.connect(self.num_su_change)
        if address_server == '':
            self.lnHost.setText(get_ip_server())
        else:
            self.lnHost.setText(address_server)
        self.btnCompare.clicked.connect(self.btn_compare)
        self.btnExit.clicked.connect(self.client_exit)
        self.mnuExit.triggered.connect(self.client_exit)

    def client_exit(self):
        update_config(config_path, self.lnNumSU.text(), self.lnSubDomain.text(), self.lnHost.text(),
                      self.lnPathDB.text(), self.lnUser.text(), self.lnPassword.text())
        self.close()

    def num_su_change(self):
        self.txtSiteSU.setText(f'http://{self.lnNumSU.text()}.{self.lnSubDomain.text()}')

    def btn_compare(self):
        type_proc_data = delo_dict[self.cbTypeCourtProc.currentText()]
        start_params = {
            'name': 'sud_delo',
            type_proc_data[0] + '_DOCUMENT__RESULT_DATE1D': self.dtBegin.text(),
            type_proc_data[0] + '_DOCUMENT__RESULT_DATE2D': self.dtEnd.text(),
            'op': 'rd',
            'delo_table': type_proc_data[0] + '_DOCUMENT',
            'delo_id': type_proc_data[1],
        }
        self.statusbar.showMessage('Обработка записей с сайта...', 3000)
        start_url = f'{self.txtSiteSU.text()}/modules.php?name=sud_delo&op=rd'
        parser_data_site = ParserMS(url=start_url, start_params=start_params)
        data_site = parser_data_site.data_site_collect()
        self.statusbar.showMessage('Обработка записей с БД...', 3000)
        db_data = parse_msite.data_db_collect(host=self.lnHost.text(),
                                              db=self.lnPathDB.text(),
                                              type_sud_delo=type_proc_data[2],
                                              set_year=self.dtBegin.date().year(),
                                              user=self.lnUser.text(),
                                              password=self.lnPassword.text(),
                                              begin=self.dtBegin.text(),
                                              finish=self.dtEnd.text())
        self.lblSiteTotal.setText(str(len(data_site)))
        self.lblDBTotal.setText(str(len(db_data)))
        self.statusbar.showMessage('Обработка завершена...', 3000)

        if len(db_data) > len(data_site):
            db_data, data_site = data_site, db_data
        print([i for i in data_site if i not in db_data])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    config_path = 'settings.ini'
    attrs = read_config(config_path)
    attrs.append(config_path)

    w = ClientWindow(*attrs)
    w.show()
    sys.exit(app.exec())
