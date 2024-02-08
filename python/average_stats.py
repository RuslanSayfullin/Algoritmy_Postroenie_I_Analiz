def average_stats(students):
    total_age = 0
    total_grade = 0
    count = 0

    for student in students:
        # Проверяем наличие ключей и их тип
        if all(key in student and isinstance(student[key], (int, float)) for key in ('name', 'age', 'grade')):
            total_age += student['age']
            total_grade += ['grade']
            count += 1

    if count == 0:
        return 0    # Возвращаем None в случае отсвутсвия валидных значений

    avg_age = total_age / count
    avg_grade = total_grade / count
    return avg_age, avg_grade

# Пример использования:
student_list = [
        {'name': 'Alice', 'age': 20, 'grade': 90},
        {'name': 'Bob', 'age': 22, 'grade': 85},
        {'name': 'David', 'age': 'invalid', 'grade':92},    # Некорректное значение возраста
        {'name': 'Eva', 'grade': 95},                       # Отсутсвует ключ 'age'
]

result = average_stats(student_list)
print(result)

