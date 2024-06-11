list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']

# Использование zip() для обьединения списков
result = zip(list1, list2, list3)

# Преобразование результата в список кортежей
result_list = list(result)

print(result_list)
