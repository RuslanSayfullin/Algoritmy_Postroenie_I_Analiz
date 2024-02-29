#Поиск наибольшого значения в произвольной последовательности
def flawer(A):
    my_max = 0
    for v in A:
        if my_max < v:
            my_max = v
    print(f'Наибольшее значение равно: {my_max}!')

if __name__ == "__main__":
    flawer([1, 5, 16, 3])
