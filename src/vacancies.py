from abc import ABC, abstractmethod
import json
from vacancy import SJVacancy, HHVacancy


class VacanciesFileIO(ABC):
    """
    Класс для сохранения информации о вакансиях в JSON-файл.
    """

    @abstractmethod
    def to_json(self, param1, param2):
        """
        Записывает в файл данные о вакансиях в формате json с сайта.
        """
        pass

    @abstractmethod
    def load_vacancy(self):
        """Инициализирует экземпляры класса данными из файла и сохраняет их в список."""
        pass

    @abstractmethod
    def load_vacancy_file(self, param1, param2):
        """Добавляет и сохраняет вакансии в  в JSON-файл."""
        pass

    @abstractmethod
    def get_data_from_file(self, filename):
        """Возвращает данные из файла по указанным критериям."""
        pass

    @abstractmethod
    def delete_information_about_vacancies(self, id_delete):
        """Удаляет информацию о вакансиях."""
        pass


class SJVacanciesFileIO(VacanciesFileIO):
    """
    Класс для сохранения информации о вакансиях в JSON-файл с сайта superjob.ru.
    """

    @classmethod
    def to_json(cls, filename: str, data: dict):
        """
        Записывает в файл _src/sj_site_data.json данные о вакансиях в формате json с сайта superjob.ru.
        filename - путь до файла, в котором необходимо сохранять информацию о ваканчиях
        data - информация о ваканчиях с сайта superjob.ru
        """
        with open(filename, "w") as write_file:
            json.dump(data, write_file, ensure_ascii=False)
            write_file.close()

    @classmethod
    def load_vacancy(cls) -> list:
        """
        Инициализирует экземпляры класса `SuperJobAPI` данными
        из файла _src/sj_site_data.json и сохраняет их в список vacancy_data.
        """
        filename = '/home/irinka/PycharmProjects/KW4/src/sj_site_data.json'
        vacancy_data = []
        try:
            with open(filename, 'r') as jsonfile:
                data = json.load(jsonfile)
                for row in data["objects"]:
                    vacancy = SJVacancy(
                        row["id"],
                        row["profession"],
                        row["payment_from"],
                        row["payment_to"],
                        row["link"]
                    )
                    vacancy_data.append(vacancy)
        except FileNotFoundError:
            print(f"Отсутствует файл {filename}")

        return vacancy_data

    @classmethod
    def load_vacancy_file(cls, filename: str, data: list):
        """Добавляет и сохраняет необходимую информацию о вакансиях в JSON-файл vacancies.json."""
        with open(filename, "w") as write_file:
            write_file.write("[")
            for i in range(len(data)):
                if i != len(data) - 1:
                    write_file.write(data[i].toJSON() + ",")
                if i == len(data) - 1:
                    write_file.write(data[i].toJSON())
            write_file.write("]")
            write_file.close()

    @classmethod
    def get_data_from_file(cls, filename):
        """Возвращает данные из файла по указанным критериям."""
        with open(filename, "r", encoding='utf-8') as jsonfile:
            return json.load(jsonfile)

    @classmethod
    def delete_information_about_vacancies(cls, id_delete):
        """Удаляет информацию о вакансиях."""
        vacancies_list = cls.get_data_from_file('/home/irinka/PycharmProjects/KW4/src/vacancies1.json')
        compiled_vacancy_list = []
        for entry in vacancies_list:
            vacancy = SJVacancy(
                entry['id_vacancy'],
                entry['_SJVacancy__vacancy_name'],
                entry['vacancy_salary_from'],
                entry['vacancy_salary_to'],
                entry['vacancy_url']
            )
            compiled_vacancy_list.append(vacancy)

        j = 0
        for entry in compiled_vacancy_list:
            if str(entry.id_vacancy) == id_delete:
                del compiled_vacancy_list[j]
            j += 1

        cls.load_vacancy_file('/home/irinka/PycharmProjects/KW4/src/sj_vacancies_with_deleted_entry.json', compiled_vacancy_list)


class HHVacanciesFileIO(VacanciesFileIO):
    """
    Класс для сохранения информации о вакансиях в JSON-файл с сайта с сайта headhunter.ru.
    """

    @classmethod
    def to_json(cls, filename: str, data):
        """
        Записывает в файл _src/hh_site_data.json данные о вакансиях в формате json с сайта headhunter.ru.
        filename - путь до файла, в котором необходимо сохранять информацию о ваканчиях
        data - информация о ваканчиях с сайта headhunter.ru
        """
        with open(filename, "w") as write_file:
            json.dump(data, write_file, ensure_ascii=False)
            write_file.close()

    @classmethod
    def load_vacancy(cls) -> list:
        """
        Инициализирует экземпляры класса `HHVacancy` данными
        из файла _src/hh_site_data.json и сохраняет их в список vacancy_data.
        """
        filename = '/home/irinka/PycharmProjects/KW4/src/hh_site_data.json'
        vacancy_data = []
        try:
            with open(filename, 'r') as jsonfile:
                data = json.load(jsonfile)
                for row in data["items"]:
                    try:
                        vacancy = HHVacancy(
                            row["id"],
                            row["name"],
                            row["salary"]["from"],
                            row["salary"]["to"],
                            row["alternate_url"]
                        )
                    except TypeError:
                        salary_from = 0
                        salary_to = 0
                        vacancy = HHVacancy(
                            row["id"],
                            row["name"],
                            salary_from,
                            salary_to,
                            row["alternate_url"]
                        )
                    if vacancy.vacancy_salary_to is None:
                        vacancy.vacancy_salary_to = 0
                    if vacancy.vacancy_salary_from is None:
                        vacancy.vacancy_salary_from = 0
                    vacancy_data.append(vacancy)

        except FileNotFoundError:
            print(f"Отсутствует файл {filename}")
        return vacancy_data

    @classmethod
    def load_vacancy_file(cls, filename: str, data: list):
        """Добавляет и сохраняет необходимую информацию о вакансиях в JSON-файл vacancies.json."""
        with open(filename, "w") as write_file:
            write_file.write("[")
            for i in range(len(data)):
                if i != len(data) - 1:
                    write_file.write(data[i].toJSON() + ",")
                if i == len(data) - 1:
                    write_file.write(data[i].toJSON())
            write_file.write("]")
            write_file.close()

    @classmethod
    def get_data_from_file(cls, filename):
        """Возвращает данные из файла по указанным критериям."""
        # filename = '/home/irinka/PycharmProjects/KW4/src/vacancies.json'
        with open(filename, "r", encoding='utf-8') as jsonfile:
            # return json.dump(jsonfile)
            return json.load(jsonfile)

    @classmethod
    def delete_information_about_vacancies(cls, id_delete):
        """Удаляет информацию о вакансиях."""
        vacancies_list = cls.get_data_from_file('/home/irinka/PycharmProjects/KW4/src/vacancies2.json')
        compiled_vacancy_list = []
        for entry in vacancies_list:
            vacancy = HHVacancy(
                entry['id_vacancy'],
                entry['_HHVacancy__vacancy_name'],
                entry['vacancy_salary_from'],
                entry['vacancy_salary_to'],
                entry['vacancy_url']
            )
            compiled_vacancy_list.append(vacancy)

        j = 0
        for entry in compiled_vacancy_list:
            if entry.id_vacancy == id_delete:
                del compiled_vacancy_list[j]
            j += 1

        cls.load_vacancy_file('/home/irinka/PycharmProjects/KW4/src/hh__vacancies_with_deleted_entry.json', compiled_vacancy_list)
