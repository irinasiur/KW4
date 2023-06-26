import json
import os
from abc import ABC, abstractmethod
from vacancy import HH_Vacancy

import requests


class API(ABC):
    """
    Класс для работы с API.
    """

    @abstractmethod
    def __init__(self):
        """
        Магический метод для инициализации экземпляров класса.
        """
        pass

    @abstractmethod
    def get_page(self):
        """
        Метод для получения страницы со списком вакансий.
        """
        pass


class SuperJobAPI(API):
    """
    Класс для работы с API сайта superjob.ru.
    """
    get_tag: str

    def __init__(self, vacancy_name, search_city):
        """
        Магический метод для инициализации экземпляров класса SuperJobAPI.
        """
        self.sj_vacancy_name = vacancy_name
        self.sj_city = search_city

    def get_page(self):
        """
        Метод для получения страницы со списком вакансий.
        Аргументы:
            per_page - Количество вакансий на 1 странице, не может быть больше 100.
        Значение по умолчанию 100, т.е. максимально возможное количество.
        """
        api_key = "v3.r.137612923.2247e6538f590bf270ce403d0e542669af0ae8ee.b7a1ff95d758e6f8182c93c6db3b5a23d2513be2"
        headers = {'X-Api-App-Id': api_key}
        site = "https://api.superjob.ru"
        api_version = "/2.0/"
        get_tag = "vacancies/"
        params = f"?keyword={self.sj_vacancy_name}&town={self.sj_city}&page=0&count=100"  # Поиск ощуществляется по выбранной вакансии, выбранного города
        url = site + api_version + get_tag + params
        req = requests.get(url, headers=headers)  # Посылаем запрос к API
        data = req.content.decode()
        return json.loads(data)


class HeadHunterAPI(API):
    """
    Класс для работы с API сайта headhunter.ru.
    """
    get_tag: str

    def __init__(self, vacancy_name, search_city):
        """
        Магический метод для инициализации экземпляров класса.
        """
        self.hh_vacancy_name = vacancy_name
        self.hh_city = search_city

    def get_anything(self, get_tag):
        """
        Метод принимает endpoint API
        возвращает json объект.
        """
        site = "https://api.hh.ru/"
        if requests.get(site + get_tag).status_code == 200:
            return json.loads(requests.get(site + get_tag).content.decode())

    def get_areas(self):
        """
        Метод для получения словаря, в котором ключем является название города,
        значением является id этого города.
        """
        ar_dict = {}
        try:
            for k in self.get_anything("areas"):
                for i in range(len(k['areas'])):
                    if len(k['areas'][i]['areas']) != 0:  # Если у зоны есть внутренние зоны
                        for j in range(len(k['areas'][i]['areas'])):
                            ar_dict[k['areas'][i]['areas'][j]['name']] = k['areas'][i]['areas'][j]['id']
                    else:  # Если у зоны нет внутренних зон
                        ar_dict[k['areas'][i]['name']] = k['areas'][i]['id']
        except TypeError:
            print("get_tag не найден.")
        else:
            return ar_dict

    def get_page(self):
        """
        Метод для получения страницы со списком вакансий.
        Аргументы:
            page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
            per_page - Количество вакансий на 1 странице, не может быть больше 100.
        Значение по умолчанию 100, т.е. максимально возможное количество.
        """
        try:
            params = {
                'text': 'NAME:' + self.hh_vacancy_name,  # Текст фильтра. В имени должно быть название указанной вакансии
                'area': self.get_areas().get(self.hh_city),  # Поиск ощуществляется по вакансиям выбранного города
                'page': 0,  # Индекс страницы поиска на HH - 0
                'per_page': 100  # Кол-во вакансий на 1 странице
            }
        except AttributeError:
            print("get_tag не найден.")
        else:
            req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
            data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
            req.close()
            return json.loads(data)

#
# a = HeadHunterAPI("аналик", "Мова")
# page_gotten = a.get_page()
# v1 = HH_Vacancy(page_gotten["items"][0]["id"])
#
# print(v1.hh_vacancy_name)
#
# sup_job = SuperJobAPI("анитик", "скТ-ПЕтербург")
# # print(sup_job.get_page())


