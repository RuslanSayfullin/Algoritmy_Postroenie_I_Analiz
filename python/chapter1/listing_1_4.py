#поиск двух максимумов с помощью отредоктированной функции largest_two()

def largest_two(A):
    my_max, second = A[:2]
    if my_max < second:
        my_max, second = second, my_max

    for idx in range(2, len(A)):
        if my_max < A[idx]:
            my_max, second = A[idx], my_max
        elif second < A[idx]:
            second = A[idx]
    print(my_max, second)

if __name__ == "__main__":
    array = [1, 4, 0, 10, 8, 16]
    largest_two(array)
