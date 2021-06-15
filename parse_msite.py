"""
Задача по выборке опубликованных решений по административным делам одного участка
и сравнение с рабочей БД судебного участка, а именно из БД выбираются номера административных
дел, решения которых были выгружены для публикации.
"""

import time

import bs4
from requests import get, exceptions, Response
from firebird.driver import connect

from msud_gui import *

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
"""
start_params - словарь, содержащий стартовые параметры для выборки
определяем фильтр по дате решения - 'ADM_DOCUMENT__RESULT_DATE1D': '01.01.2020' (можно поставить своё значение)
т.е. будут выбраны все решения по административным делам, у которых дата вынесения решения больше либо равна
заявленной в фильтре
"""


class StatusCodeError(Exception):
    def __init__(self, text):
        self.text = text


def data_db_collect(host, db, type_sud_delo, set_year):
    """
    Подключаем к базе, получаем выборку, закидываем в словарь
    Сравниваем файл со списком
    Результат отработки будет выведен на экран - либо список номеров дел, если что-то пропущено,
    либо будет выведено сообщение о завершении работы
    """
    with connect(':'.join([host, db]), user='sysdba', password='masterkey', charset='win1251') as con:
        cur = con.cursor()
        cur.open('select dn."Num" from "DocumentFile" as df '
                 'join "Document" dc on df."Document" = dc."OID" '
                 'join "CaseMaterial" cm on dc."ParentCaseMaterial" = cm."OID" '
                 'join "DocNum" dn on cm."DocNum" = dn."Id" where df."IsPubl" = 1 and dn."Num" like \''
                 + str(type_sud_delo) + '%/' + str(set_year) + '\'')
        document = cur.fetchall()
        base_lst = []
        for itm in document:
            base_lst.append(itm[0])
    return base_lst


class ParserMS:
    def __init__(self, url, start_params):
        self.Ui_MainWindow = None
        self.url = url
        self.start_params = start_params

    @staticmethod
    def _get_response(url: str, **kwargs):
        """
        Метод _get_response проверки доступности сайта
        """
        while True:
            try:
                response = get(url, **kwargs)
                if response.status_code == 200:
                    return response
                raise StatusCodeError(f'{response.status_code} -> {response.text}')
            except (exceptions.HTTPError,
                    exceptions.ConnectTimeout,
                    StatusCodeError
                    ):
                time.sleep(0.25)

    @staticmethod
    def _get_soup(response: Response) -> bs4.BeautifulSoup:
        """
        Метод _get_soup для обрабтоки статусов и повторных запросов
        """
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        return soup

    def data_site_collect(self):
        """
        метод запуска
        получаем start_data(начальные данные) со страницы
        определяем количество страниц count_page
        """
        data_site_lst = []
        start_data = self._get_soup(self._get_response(self.url, headers=headers, params=self.start_params))
        for tag in start_data.find_all('tr'):
            if tag.contents[1].text != 'Номер дела':
                data_site_lst.append(tag.contents[1].text.strip())
        if start_data.find('ul', {'class': 'paging'}):
            page_lst = list(start_data.find('ul', {'class': 'paging'}))
            count_page = max([int(i.text) for i in page_lst if i.text.isdigit()])

            # отправляем первую партию данных на запись
            # обрабатываем все страницы
            print('Обрабатываем записи с сайта...')
            for num_str in range(1, count_page):
                # добавим новый элемент pageNum_Recordset1 в стартовый словарь
                self.start_params['pageNum_Recordset1'] = num_str
                data = self._get_soup(self._get_response(self.url, headers=headers, params=self.start_params))
                for tag in start_data.find_all('tr'):
                    if tag.contents[1].text != 'Номер дела':
                        data_site_lst.append(tag.contents[1].text.strip())

        return data_site_lst
