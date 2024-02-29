def alternative(A):
    """"Функция находит наибольшее значение в списке A"""
    for v in A:
        for x in A:
            if v < x:
                break
            else:
                return v
    return None
