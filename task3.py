# Программа по созданию списка из кортежей, замены порядковых номеров в кортежах на сумму очков
# и подсчету общей суммы очков

languages = ["python", "c#", "c", "c++", "java"]
numbers = list(range(1, len(languages) + 1))

points = {
    0: 482,
    1: 102,
    2: 67,
    3: 353,
    4: 290
}

def tuples(list_1, list_2):
    """Функуия по созданию списка кортежей из двух пользовательских списков.
    Аргументы list_1, list_2: списки, один из которых содержит наименования языков программирования,
    а второй - порядковые номера"""
    res_tuple = tuple()
    res_list = list()
    for i in range(0, len(list_1)):
        list_2[i] = list_2[i].upper()
        res = (list_1[i], list_2[i])
        res_list.append(res)
    return res_list

def sum_of_points(sum_list, point):
    """Фукнция по замене порядковых номеров суммой очков наименования языка программирования,
    удаления из списка кортежей, в которых порядковый номер не является делителем суммы очков,
    а также подсчета общей суммы очков.
    Аргументы: sum_list - список, содержащий кортежи; point - словарь, содержащий количество очков"""
    new_list = list()
    count = 0
    for i in range(0, len(sum_list) - 1):
        element = list(sum_list[i])
        temp = point.get(i)
        if temp % element[0] == 0:
            element[0] = point.get(i)
            count = count + point.get(i)
            new_list.append(tuple(element))
    return new_list, count

user_tuple = tuples(numbers, languages)
print(user_tuple)
result = sum_of_points(user_tuple, points)
print(result)