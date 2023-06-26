from abc import ABC, abstractmethod


class Vacancy(ABC):
    pass

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        '''сравнивает вакансии ежду собой по зарплате'''
        pass


class SJ_Vacancy(Vacancy):
    def __init__(self, id_vacancy, vacancy_name, vacancy_salary_from, vacancy_salary_to, vacancy_url):
        self.id_vacancy = id_vacancy
        self.vacancy_name = vacancy_name
        self.vacancy_salary_from = vacancy_salary_from
        self.vacancy_salary_to = vacancy_salary_to
        self.vacancy_url = vacancy_url

    def __eq__(self, other):
        '''сравнивает вакансии ежду собой по зарплате'''
        pass


class HH_Vacancy(Vacancy):
    def __init__(self, id_hh_vacancy, vacancy_name, vacancy_salary):
        self.id_hh_vacancy = id_hh_vacancy
        self.__hh_vacancy_name = vacancy_name
        self.hh_vacancy_salary = vacancy_salary
        self.hh_vacancy_url = "https://api.hh.ru/" + self.id_hh_vacancy



    @property
    def hh_vacancy_name(self):
        return self.__hh_vacancy_name

    @hh_vacancy_name.setter
    def hh_vacancy_name(self, actual_name):
        self.__hh_vacancy_name = actual_name


    def __eq__(self, other):
        '''сравнивает вакансии ежду собой по зарплате'''
        pass





#, vacancy_name, vacancy_url, salary, description