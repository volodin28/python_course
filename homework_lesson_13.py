from datetime import datetime

# Написати клас та реалізувати його методи: (основа – ДЗ № 10)
# 1. Ініціалізація класу з одним параметром – ім'я файлу.

# 2. Написати метод екземпляра класу, який створює атрибут екземпляра класу
# у вигляді списку рядків (назви повертати без крапки)

# 3. Написати метод екземпляра класу, який повертає список усіх прізвищ із файлу.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"
#
# 4. Написати метод екземпляра класу, який повертає список
# словників виду {"date": date} у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
#
# 5* (*здавати не обов'язково).
# Написати метод екземпляра класу, отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date_original": date_original, "date_modified": date_modified}
# у яких date_original - це дата з рядка (якщо є),
# а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyy" (d-день, m-місяць, y-рік)
# Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]


class GetFile:

    def __init__(self, file_name):                  # 1. Ініціалізація класу з одним параметром
        self.file_name = file_name

    def get_domains(self):                          # 2.
        with open(self.file_name, 'r') as self.my_file:
            return [self.my_file.read().replace(".", "").split("\n")]

    def get_names(self):                            # 3.
        names_list = []
        with open(self.file_name, 'r') as f:
            for line in f:
                names_list.append(line.split()[1])
        return names_list

    def get_dates(self):                            # 4.
        dates_list = []
        with open(self.file_name, 'r') as f:
            for line in f:
                line_data = line.split()
                if len(line_data) > 3:
                    dates_list.append(' '.join(line_data[:3]))
        dict_dates = []
        for i in dates_list:
            dict_dates.append({"date": i})

        return dict_dates

    def get_dates_2(self):                          # 5.
        dates_list = []
        dates_list_full = []
        with open(self.file_name, 'r') as f:
            for line in f:
                line_data = line.replace("1st", '1').replace("2nd", '2').replace("th", '').replace("3rd", '3').split()
                line_data_full = line.split()
                if len(line_data) > 3:
                    dates_list.append(' '.join(line_data[:3]))
                    dates_list_full.append(' '.join(line_data_full[:3]))
        dict_dates = []
        for i, j in zip(dates_list_full, dates_list):
            if i[-1].isnumeric():
                dict_dates.append(
                    {"date_original": i, "date_modified": datetime.strptime(j, '%d %B %Y').strftime("%d/%m/%Y")})
            else:
                dict_dates.append(
                    {"date_original": i[:-2], "date_modified": datetime.strptime(j[:-2], '%B %Y').strftime("%m/%Y")})
        return dict_dates


my_file = GetFile("domains.txt")
print(my_file.get_domains())

my_file_2 = GetFile("names.txt")
print(my_file_2.get_names())

my_file_3 = GetFile("authors.txt")
print(my_file_3.get_dates())
print(my_file_3.get_dates_2())
