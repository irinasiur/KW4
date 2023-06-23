import json
import os
from abc import ABC, abstractmethod

import requests


class API(ABC):

    @abstractmethod
    def get_anything(self, endpoint):
        """
        Метод принимает endpoint API
        возвращает json объект.
        """
        pass

    @abstractmethod
    def get_areas(self):
        """
        Метод для получения словаря, в котором ключем является название города,
        значение это id этого города.
        """
        pass

    # @abstractmethod
    # def get_city_id(self):
    #     """
    #     Метод для получения значения id города для фильтрации по городам.
    #     """
    #     pass

    @abstractmethod
    def get_page(self):
        """
        Метод для получения страницы со списком вакансий.
        """
        pass


class SuperJobAPI(API):

    def get_anything(self, endpoint):
        pass

    def get_areas(self):
        pass

    def get_page(self):
        """Получить ключ для API."""
        pass
        # api_key = "v3.r.137612923.2247e6538f590bf270ce403d0e542669af0ae8ee.b7a1ff95d758e6f8182c93c6db3b5a23d2513be2"
        # return build('superjob', 'v3', developerKey=api_key)


class HeadHunterAPI(API):
    get_tag: str

    def __init__(self, vacancy_name, search_city):
        self.vacancy_name = vacancy_name
        self.city = search_city

    def get_anything(self, get_tag):
        """
        Метод принимает endpoint API
        возвращает json объект.
        """
        site = "https://api.hh.ru/"
        return json.loads(requests.get(site + get_tag).content.decode())

    def get_areas(self):
        """
        Метод для получения словаря, в котором ключем является название города,
        значением является id этого города.
        """
        ar_dict = {}
        for k in self.get_anything("areas"):
            for i in range(len(k['areas'])):
                if len(k['areas'][i]['areas']) != 0:  # Если у зоны есть внутренние зоны
                    for j in range(len(k['areas'][i]['areas'])):
                        ar_dict[k['areas'][i]['areas'][j]['name']] = k['areas'][i]['areas'][j]['id']
                else:  # Если у зоны нет внутренних зон
                    ar_dict[k['areas'][i]['name']] = k['areas'][i]['id']
        return ar_dict


    def get_page(self):
        """
        Метод для получения страницы со списком вакансий.
        Аргументы:
            page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
        """
        params = {
            'text': 'NAME:' + self.vacancy_name,  # Текст фильтра. В имени должно быть название указанной вакансии
            'area': self.get_areas().get(self.city),  # Поиск ощуществляется по вакансиям выбранного города
            'page': 0,  # Индекс страницы поиска на HH - 0
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        return json.loads(data)


a = HeadHunterAPI("аналитик", "Москва")
print(a.get_page())

