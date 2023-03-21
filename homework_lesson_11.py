import os

# Всі пункти є частиною одного завдання, тому можна використовувати функції кілька разів та не дублювати код.
# Якщо хочете, можете використовувати дефолтні значення та анотацію типів.
#
# 1. Написати функцію, яка отримує один параметр - ім'я директорії та повертає словник виду
# {'filenames': [список файлів у папці], 'dirnames': [список усіх підпапок у папці]}.
# Підпапки враховувати лише першого рівня вкладення. Папка в папці в папці - таке не брати))


def get_filenames_dirnames(directory):
    list_subdir = []
    list_files = []
    for i in os.scandir(directory):
        if i.is_dir():
            list_subdir.append(i.name)
        else:
            list_files.append(i.name)
    return {'filenames': list_files, 'dirnames': list_subdir}


my_dir = "../python_course"
print(get_filenames_dirnames(my_dir))

# 2. Написати функцію, яка отримує два параметри – словник, описаний у пункті 1
# і значення булю (True/False) - можна зробити за замовчуванням.
# Функція повертає той самий словник, але з відсортованими іменами файлів та папок у відповідних списках.
# Булеве значення True означає, що порядок сортування алфавітний, False – зворотний порядок.


def sort_filenames_dirnames(directory, issorted: bool):
    my_dict = get_filenames_dirnames(directory)
    for i in my_dict.values():
        if issorted:
            i.sort()
        else:
            i.sort(reverse=True)
    return my_dict


print(sort_filenames_dirnames(my_dir, False))


# 3. Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та рядок, який може бути
# або ім'ям файлу, або ім'ям папки. (У імені файлу має бути точка).
# Залежно від того, що функція отримала (ім'я файлу або ім'я папки) – записати його у відповідний список
# та повернути оновлений словник.


def add_name(my_dict: dict, add_file: str) -> dict:
    if "." in add_file:
        my_dict['filenames'].append(add_file)
    else:
        my_dict['dirnames'].append(add_file)
    return my_dict


print(add_name(get_filenames_dirnames(my_dir), 'test'))

# 4* (*здавати не обов'язково).
# Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та ім'я директорії.
# Функція перевіряє відповідність отриманого словника та реальної файлової системи в отриманій папці та,
# якщо треба, створює потрібні папки та порожні файли, відповідно до структури словника.