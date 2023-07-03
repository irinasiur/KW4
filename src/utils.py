from src.api import SuperJobAPI, HeadHunterAPI
from src.vacancies import SJVacanciesFileIO, HHVacanciesFileIO


def bubble(array):
    """
    Функция для сортировки пузырьком.
    """
    for i in range(len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j].__lt__(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def user_interaction():
    """
    Функция для взаимодействия с пользователем через консоль.
    """

    my_list = []
    my_list1 = []
    my_list2 = []
    search_query = "bla"
    while search_query not in ["1", "2", "12"]:
        search_query = input("Выберите интересующий Вас сайт: superjob.ru (1) или headhunter.ru (2)"
                             " и введите соответствующие цифры. "
                             "Если необходима информация с обоих сайтов введите цифру 12 ")
    top_n_str = "bla"
    while not top_n_str.isdigit():
        top_n_str = (input("Введите количество вакансий для вывода в топ N: "))
    top_n = int(top_n_str)
    vacancy_name = input("Введите название вакансии: ")
    search_city = input("Введите название города, в котором необходимо найти вакансии ").title()

    if not vacancy_name:
        print("Нет вакансий, соответствующих заданным критериям.")
    elif not search_city:
        print("В выбранном Вами городе нет интересующих Вас вакансий.")
    else:
        if search_query == '1':
            data1 = SuperJobAPI(vacancy_name, search_city)
            SJVacanciesFileIO.to_json('sj_site_data.json', data1.get_page())
            my_list = SJVacanciesFileIO.load_vacancy()
            filename1 = '/home/irinka/PycharmProjects/KW4/src/vacancies1.json'
            SJVacanciesFileIO.load_vacancy_file(filename1, my_list)
        elif search_query == '2':
            data2 = HeadHunterAPI(vacancy_name, search_city)
            HHVacanciesFileIO.to_json('hh_site_data.json', data2.get_page())
            my_list = HHVacanciesFileIO.load_vacancy()
            filename2 = '/home/irinka/PycharmProjects/KW4/src/vacancies2.json'
            HHVacanciesFileIO.load_vacancy_file(filename2, my_list)
        elif search_query == '12':
            data1 = SuperJobAPI(vacancy_name, search_city)
            SJVacanciesFileIO.to_json('sj_site_data.json', data1.get_page())
            my_list1 = SJVacanciesFileIO.load_vacancy()
            data2 = HeadHunterAPI(vacancy_name, search_city)
            HHVacanciesFileIO.to_json('hh_site_data.json', data2.get_page())
            my_list2 = HHVacanciesFileIO.load_vacancy()
            filename1 = '/home/irinka/PycharmProjects/KW4/src/vacancies1.json'
            SJVacanciesFileIO.load_vacancy_file(filename1, my_list1)
            filename2 = '/home/irinka/PycharmProjects/KW4/src/vacancies2.json'
            HHVacanciesFileIO.load_vacancy_file(filename2, my_list2)
            my_list = my_list1 + my_list2
        else:
            print("Сайт не найден.")

    sorted_list = bubble(my_list)

    i = 0
    user_input_number_vacancy = top_n

    if top_n > len(sorted_list):
        top_n = len(sorted_list)
        print(f"Вы хотели вывести {user_input_number_vacancy} вакансий, "
              f"что превышает их количество, поэтому будут выведены все.")

    for entry in sorted_list:
        print(str(entry))
        if i < top_n - 1:
            i += 1
        else:
            break






















