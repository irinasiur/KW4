import json
from abc import ABC, abstractmethod


class Vacancy(ABC):
    """
    Класс для работы с вакансиями.
    """
    pass

    @abstractmethod
    def __init__(self):
        """
        Инициализация экземпляров класса для работы с вакансиями.
        """
        pass

    @abstractmethod
    def __lt__(self, other):
        """
        Сравнивает вакансии между собой по зарплате (строго меньше).
        """
        pass


class SJVacancy(Vacancy):
    """Класс для работы с вакансиями с сайта superjob.ru."""

    def __init__(self, id_vacancy: int, vacancy_name: str,
                 vacancy_salary_from: int, vacancy_salary_to: int, vacancy_url: str):
        """
        Инициализация экземпляров класса для работы с вакансиями с сайта superjob.ru.
        """
        self.id_vacancy = id_vacancy
        self.__vacancy_name = vacancy_name
        self.vacancy_salary_from = vacancy_salary_from
        self.vacancy_salary_to = vacancy_salary_to
        self.vacancy_url = vacancy_url

    @property
    def vacancy_name(self):
        """
        Геттер
        """
        return self.__vacancy_name

    @vacancy_name.setter
    def vacancy_name(self, a):
        """
        Сеттер
        """
        self.__vacancy_name = a

    def __str__(self) -> str:
        """
        Возвращает id вакансии, название вакансии, начальный уровень зарплаты в рублях,
        верхний уровень зарплаты в рублях и ссылку на данную вакансию.
        """
        return f'{{"id_vacancy": "{self.id_vacancy}", "vacancy_name": "{self.vacancy_name}", ' \
               f' "vacancy_salary_from": {self.vacancy_salary_from}, "vacancy_salary_to": {self.vacancy_salary_to}, ' \
               f' "vacancy_url": "{self.vacancy_url}"}},'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False,
                          sort_keys=True, indent=4)

    def __lt__(self, other: Vacancy) -> bool:
        """
        Сравнение по атрибуту vacancy_salary_to (строго меньше).
        """
        if other == self:
            return NotImplemented
        if not isinstance(other, Vacancy):
            return NotImplemented
        if self.vacancy_salary_from is None:
            self.vacancy_salary_from = 0
        if self.vacancy_salary_to is None:
            self.vacancy_salary_to = 0
        if other.vacancy_salary_from is None:
            other.vacancy_salary_from = 0
        if other.vacancy_salary_to is None:
            other.vacancy_salary_to = 0
        return self.vacancy_salary_to < other.vacancy_salary_to


class HHVacancy(Vacancy):
    """Класс для работы с вакансиями с сайта headhunter.ru."""

    def __init__(self, id_vacancy: str, vacancy_name: str,
                 vacancy_salary_from: int, vacancy_salary_to: int, vacancy_url: str):
        """
        Инициализация экземпляров класса для работы с вакансиями с сайта headhunter.ru.
        """
        self.id_vacancy = id_vacancy
        self.__vacancy_name = vacancy_name
        self.vacancy_salary_from = vacancy_salary_from
        self.vacancy_salary_to = vacancy_salary_to
        self.vacancy_url = vacancy_url

    @property
    def vacancy_name(self):
        """
        Геттер
        """
        return self.__vacancy_name

    @vacancy_name.setter
    def vacancy_name(self, a):
        """
        Сеттер
        """
        self.__vacancy_name = a

    def __str__(self) -> str:
        """
        Возвращает id вакансии, название вакансии, начальный уровень зарплаты в рублях,
        верхний уровень зарплаты в рублях и ссылку на данную вакансию.
        """
        return f'{{"id_vacancy": "{self.id_vacancy}", "vacancy_name": "{self.vacancy_name}", ' \
               f'"vacancy_salary_from": {self.vacancy_salary_from}, "vacancy_salary_to": {self.vacancy_salary_to}, ' \
               f'"vacancy_url": "{self.vacancy_url}"}},'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False,
                          sort_keys=True, indent=4)

    def __lt__(self, other: Vacancy) -> bool:
        """
        Сравнение по атрибуту vacancy_salary_to (строго меньше).
        """
        if other == self:
            return NotImplemented
        if not isinstance(other, Vacancy):
            return NotImplemented
        if self.vacancy_salary_from is None:
            self.vacancy_salary_from = 0
        if self.vacancy_salary_to is None:
            self.vacancy_salary_to = 0
        if other.vacancy_salary_from is None:
            other.vacancy_salary_from = 0
        if other.vacancy_salary_to is None:
            other.vacancy_salary_to = 0
        return self.vacancy_salary_to < other.vacancy_salary_to

