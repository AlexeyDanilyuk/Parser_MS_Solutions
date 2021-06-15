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


def createConfig(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "number_su", "")
    config.set("Settings", "subdomain_url_su", "")
    config.set("Settings", "local_server_ip", "")
    config.set("Settings", "path_db_amirs", "")

    with open(path, "w") as config_file:
        config.write(config_file)


def updateConfig(path, number_su, subdomain_url_su, path_db_amirs, local_server_ip):
    """
    Update a config file
    """
    config = configparser.ConfigParser()
    config.read(path)
    config.set("Settings", "number_su", number_su)
    config.set("Settings", "subdomain_url_su", subdomain_url_su)
    config.set("Settings", "local_server_ip", path_db_amirs)
    config.set("Settings", "path_db_amirs", local_server_ip)

    with open(path, "w") as config_file:
        config.write(config_file)


def readConfig(path):
    """
    Create, read, update, delete config
    """
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    number_su = config.get("Settings", "number_su")
    subdomain_url_su = config.get("Settings", "subdomain_url_su")
    local_server_ip = config.get("Settings", "local_server_ip")
    path_db_amirs = config.get("Settings", "path_db_amirs")

    with open(path, "w") as config_file:
        config.write(config_file)

    return [number_su, subdomain_url_su, path_db_amirs, local_server_ip]


def get_ip_server():
    ipv4_addresses = [i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None) if i[0] == socket.AF_INET]
    ipv4_addresses = ipv4_addresses[0].split('.')
    ipv4_addresses[3] = '2'
    ipv4_addresses = '.'.join(ipv4_addresses)

    return ipv4_addresses


class ClientWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, number_su, subdomain_url_su, path_db_amirs, local_server_ip, config_path):
        super().__init__()
        self.number_su = number_su
        self.subdomain_url_su = subdomain_url_su
        self.path_db_amirs = path_db_amirs
        self.config_path = config_path
        self.setupUi(self)
        self.dtBegin.setDate(QDate(datetime.datetime.now().year, 1, 1))
        self.dtEnd.setDate(QDate(datetime.datetime.now().year, 12, 31))
        self.lnNumSU.setText(number_su)
        self.lnSubDomain.setText(subdomain_url_su)
        if not self.lnNumSU.text().isspace() and not self.lnSubDomain.text().isspace():
            self.num_su_change()
        else:
            self.txtSiteSU.setText('')
        self.lnPathDB.setText(path_db_amirs)
        self.lnNumSU.textChanged.connect(self.num_su_change)
        self.lnSubDomain.textChanged.connect(self.num_su_change)
        if local_server_ip == '':
            self.lnHost.setText(get_ip_server())
        else:
            self.lnHost.setText(local_server_ip)
        self.btnCompare.clicked.connect(self.btn_compare)
        self.btnExit.clicked.connect(self.client_exit)
        self.mnuExit.triggered.connect(self.client_exit)

    def client_exit(self):
        number_su = self.lnNumSU.text()
        subdomain_url_su = self.lnSubDomain.text()
        local_server_ip = self.lnHost.text()
        path_db_amirs = self.lnPathDB.text()
        updateConfig(config_path, number_su, subdomain_url_su, local_server_ip, path_db_amirs)
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
        start_url = f'{self.txtSiteSU.text()}/modules.php?name=sud_delo&op=rd'
        parser_data_site = ParserMS(url=start_url, start_params=start_params)
        data_site = parser_data_site.data_site_collect()
        db_data = parse_msite.data_db_collect(host=self.lnHost.text(),
                                              db=self.path_db_amirs,
                                              type_sud_delo=type_proc_data[2],
                                              set_year=self.dtBegin.date().year())
        self.lblSiteTotal.setText(str(len(data_site)))
        self.lblDBTotal.setText(str(len(db_data)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    config_path = 'settings.ini'
    attrs = readConfig(config_path)
    attrs.append(config_path)

    w = ClientWindow(*attrs)
    w.show()
    sys.exit(app.exec())
