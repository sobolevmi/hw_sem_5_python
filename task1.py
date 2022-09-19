# Программа по удалению из текста всех слов, содержащих "абв"

def delete_text(input_string):
    """Функция по удалению из текста всех элементов, содержащих 'абв'.
    Аргумент - введенная пользователем строка"""
    any_list = list(input_string.split())
    result_list = list()
    for i in any_list:
        if "абв" not in i:
            result_list.append(i)
    res_string = ""
    for i in result_list:
        res_string = res_string + i + " "
    return res_string

user_string = str(input("Введите строку: "))
result_string = delete_text(user_string)
print(f"{user_string} -> {result_string}")