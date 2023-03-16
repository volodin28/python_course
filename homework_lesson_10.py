# 1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
# та повертає їх у вигляді списку рядків (назви повертати без крапки).


def get_domains(file_name="domains.txt"):
    with open(file_name, 'r') as my_file:
        domains = [my_file.read().replace(".", "").split("\n")]
        return domains


print(get_domains())


# 2. Написати функцію, яка отримує як параметр ім'я файла (names.txt)
# і повертає список усіх прізвищ із нього.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"


def get_names(file_name="names.txt"):
    names_list = []
    with open(file_name, 'r') as f:
        for line in f:
            line_data = line.split()
            names_list.append(line_data[1])

    return names_list


print(get_names())


# 3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date": date}
# у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]


def get_dates(file_name="authors.txt"):
    dates_list = []
    with open(file_name, 'r') as f:
        for line in f:
            line_data = line.split()
            if len(line_data) > 3:
                dates_list.append(' '.join(line_data[:3]))
    dict_dates = []
    for i in dates_list:
        dict_dates.append({"date": i})

    return dict_dates


print(get_dates())


# 4* (*здавати не обов'язково).
# Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date_original": date_original, "date_modified": date_modified}
# у яких date_original - це дата з рядка (якщо є),
# а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
# Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]


from datetime import datetime

def get_dates_2(file_name="authors.txt"):
    dates_list = []
    dates_list_full = []
    with open(file_name, 'r') as f:
        for line in f:
            line_data = line.replace("1st", '1').replace("2nd", '2').replace("th", '').replace("3rd", '3').split()
            line_data_full = line.split()
            if len(line_data) > 3:
                dates_list.append(' '.join(line_data[:3]))
                dates_list_full.append(' '.join(line_data_full[:3]))
    dict_dates = []
    for i, j in zip(dates_list_full, dates_list):
        dict_dates.append({"date_original": i, "date_modified": datetime.strptime(j, '%d %B %Y').strftime("%d/%m/%y")})
    return dict_dates


print(get_dates_2())





# print(datetime.strptime("8 February 1828", '%d %B %Y').strftime("%d/%m/%y"))
