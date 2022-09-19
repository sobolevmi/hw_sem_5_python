# Программа по реализации RLE-алгоритма

def count_duplicates(any_string):
    """Функция по удалению повторяющихся элементов в строке.
    Аргумент - введенная пользователем строка"""
    result = list()
    any_string = list(any_string)
    if any_string:
        previous_element = any_string.pop(0)
        count = 1
        for item in any_string:
            if item == previous_element:
                count += 1
            else:
                result.append((count, previous_element))
                previous = item
                count = 1
        result.append((count, previous_element))
    return str(result)

with open("input_task_4.txt", "w") as input_file:
    user_string = str(input("Введите исходную строку: "))
    user_string.strip()
    input_file.write(user_string)

with open("output_task_4.txt", "w") as output_file:
    result_string = count_duplicates(user_string)
    output_file.write(result_string)