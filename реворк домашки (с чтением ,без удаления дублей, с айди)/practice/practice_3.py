# 1. Создайте класс с базовыми-абстрактными функциями. Класс должен иметь аргументы. Настройте поведение экземпляра
# класса с помощью дандер методов

# 2. Дано целое число x, вернуть x с обратными цифрами
# Пример 1:
#  Вход: x = 123
#  Выход: 321

# Пример 2:
# Вход: x = -123
# Выход: -321
#
# Пример 3:
# Вход: x = 120
# Выход: 21

def reverse_int(st: int):
    if st >= 0:
        return int(str(st)[::-1])
    else:
        num = '-'+str(st)[::-1].replace('-', '')
        return int(num)


reverse_int(123)
reverse_int(-109)
reverse_int(120)
e = reverse_int(120)

# 3. Напишите функцию, принимающую в качестве аргументов 2 списка. Функция должна соединить и отсортировать их.
#
# Пример 1:
# Вход: список1 = [1,2,4], список2 = [1,3,4]
#  Выход: [1,1,2,3,4,4]
#
# Пример 2:
# Ввод: список1 = [], список2 = []
#  Вывод: []
#
# Пример 3:
# Ввод: список1 = [], список2 = [0]
#  Вывод: [0]


def merge_lists(list1: list, list2: list):
    list1.extend(list2)
    return sorted(list1)

print(merge_lists([1,2,2,3,5,6,123,3], [1,1,1,1,8]))
