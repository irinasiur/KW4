import os

from src.vacancies import HHVacanciesFileIO, SJVacanciesFileIO
from utils import user_interaction

user_interaction()

# Delete by id_vacancy
if os.path.isfile('/home/irinka/PycharmProjects/KW4/src/vacancies1.json'):
    SJVacanciesFileIO.delete_information_about_vacancies("40834470") # id_vacancy = 40834470 существует
if os.path.isfile('/home/irinka/PycharmProjects/KW4/src/vacancies2.json'):
    HHVacanciesFileIO.delete_information_about_vacancies("82319579") # id_vacancy = 82319579 существует

