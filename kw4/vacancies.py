from abc import ABC, abstractmethod


class VACANCIES(ABC):


    @abstractmethod
    def add_vacancies_to_file(self):
        """Добавляет и сохраняет вакансии в файл."""
        pass

    @abstractmethod
    def get_data_from_file(self):
        """Возвращает данные из файла по указанным критериям."""
        pass

    @abstractmethod
    def delete_information_about_vacancies(self):
        """Удаляет информацию о вакансиях."""
        pass
