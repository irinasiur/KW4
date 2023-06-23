from abc import ABC, abstractmethod


class VACANCY(ABC):
    pass

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        '''сравнивает вакансии ежду собой по зарплате'''
        pass

class HH_Vacancy(VACANCY):
    def __init__(self, id_hh_vacancy):
        self.id_hh_vacancy = id_hh_vacancy
        self.hh_vacancy_name
        self.hh_vacancy_url
        self.hh_vacancy_salary




#, vacancy_name, vacancy_url, salary, description