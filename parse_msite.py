"""
Задача по выборке опубликованных решений по уголовным, гражданским и административным делам одного участка
и сравнение с рабочей БД судебного участка, а именно из БД выбираются номера уголовных, гражданских и административных
дел, решения которых были выгружены для публикации.
"""

import time

import bs4
import fdb
from requests import get, exceptions, Response

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}


class StatusCodeError(Exception):
    def __init__(self, text):
        self.text = text


def data_db_collect(host, db, type_sud_delo, set_year, begin, finish, user, password):
    try:
        con = fdb.connect(dsn=':'.join([host, db]), user=user, password=password, sql_dialect=3)
        if con:
            cur = con.cursor()
            sql = f'select dn."Num" from "DocumentFile" as df join "Document" dc on df."Document" = dc."OID" ' \
                  f'join "CaseMaterial" cm on dc."ParentCaseMaterial" = cm."OID" ' \
                  f'join "DocNum" dn on cm."DocNum" = dn."Id" where df."IsPubl" = 1 and ' \
                  f'dn."Num" like \'{str(type_sud_delo)}%/{str(set_year)}\' ' \
                  f'and dc."CreateDate" between \'{begin}\' and \'{finish}\''
            cur.execute(sql)
            document = cur.fetchall()
            base_lst = [itm[0] for itm in document]
            return base_lst
    except BaseException as e:
        return print(f'{e}')


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
            for num_str in range(1, count_page):
                # добавим новый элемент pageNum_Recordset1 в стартовый словарь
                self.start_params['pageNum_Recordset1'] = num_str
                start_data = self._get_soup(self._get_response(self.url, headers=headers, params=self.start_params))
                for tag in start_data.find_all('tr'):
                    if tag.contents[1].text != 'Номер дела':
                        data_site_lst.append(tag.contents[1].text.strip())

        return data_site_lst
