#Создаём пустой словарь
num = []
#Прописываем функцию для словаря (через диапозон с 1 до 16)
for x in range(1, 16):
    num.append(x)
#Создаём фильтрацию (с использованем ламбда функии), делим без остатка на два и сравниваем полоученные значения
even_numbers = list(filter(lambda x: x % 2 == 0, num))
print(even_numbers)

#Болеее коротки вариант (без использования append, filter и приобразования (list))
even_numbers = [x for x in range(1, 16) if x % 2 == 0]
print(even_numbers)
