def largest(A):
    """Функция находит наибольшее значение в списке"""
    my_max = A[0]
    for idx in range(1, len(A)):
        if my_max < A[idx]:
            my_max = A[idx]
    print(f"Наийбольшее значение в списке: {my_max}")

if __name__ == "__main__":
    largest([1, 12, -1, 0, 16])
