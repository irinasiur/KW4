import json
from api import SuperJobAPI, HeadHunterAPI
from vacancy import SJ_Vacancy, HH_Vacancy


def user_interaction():
    search_query = input("Выберите интересующий Вас сайт: superjob.ru (1) или headhunter.ru (2)"
                         " и введите соответствующие цифры. "
                         "Если необходима информация с обоих сайтов введите цифру 12 ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    vacancy_name = input("Введите название вакансии: ")
    search_city = input("Введите название города, в котором необходимо найти вакансии ")

    if not vacancy_name:
        print("Нет вакансий, соответствующих заданным критериям.")
    elif not search_city:
        print("В выбранном Вами городе нет интересующих Вас вакансий.")
    else:
        if search_query == '1':
            data1 = SuperJobAPI(vacancy_name, search_city)
            to_json('site_data.json', data1.get_page())
        elif search_query == '2':
            data2 = HeadHunterAPI(vacancy_name, search_city)
        elif search_query == '12':
            data12 = SuperJobAPI(vacancy_name, search_city) + HeadHunterAPI(vacancy_name, search_city)
        else:
            print("Сайт не найден.")


def to_json(filename, data):
    with open(filename, "w") as write_file:
        # my_string = json.dumps(self.info, ensure_ascii=False).encode('utf-8').decode()
        json.dump(data, write_file, ensure_ascii=False)
        write_file.close()


def SJ_load_vacancy():
    """
    Инициализирует экземпляры класса `SuperJobAPI` данными из файла _src/site_data.json.
    """
    # cls.all.clear()
    filename = '/home/irinka/PycharmProjects/KW4/kw4/site_data.json'
    vacancy_data = []
    try:
        with open(filename, 'r') as jsonfile:
            data = json.load(jsonfile)
            for row in data["objects"]:
                vacancy = SJ_Vacancy(
                    row["id"],
                    row["profession"],
                    row["payment_from"],
                    row["payment_to"],
                    row["link"]
                )
                vacancy_data.append(vacancy)
    except FileNotFoundError:
        print(f"Отсутствует файл {filename}")

    # print(vacancy_data)
    return vacancy_data


# print(SJ_load_vacancy())

# a = HeadHunterAPI("аналик", "Мова")
# page_gotten = a.get_page()
# v1 = HH_Vacancy(page_gotten["items"][0]["id"])
# v1.hh_vacancy_name = page_gotten["items"][0]["name"]
# print(v1.id_hh_vacancy, "    ", v1.hh_vacancy_name)
#

# # print(sup_job.get_page())


user_interaction()
print(SJ_load_vacancy()[0].vacancy_name)
