#include <stdio.h>

// Функция для реализации бинарного поиска
int binarySearch(int arr[], int low, int high, int target) {
    while (low <= high) {
        int mid = low + (high - low) / 2;

        // Если элемент найден, возвращаем его индекс
        if (arr[mid] == target)
            return mid;

        // Если искомый элемент меньше, чем средний элемент,
        // ищем в левой половине
        if (arr[mid] > target)
            high = mid - 1;

        // Иначе ищем в правой половине
        else
            low = mid + 1;
    }

    // Если элемент не найден, возвращаем -1
    return -1;
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 23;
    int result = binarySearch(arr, 0, n - 1, target);

    if (result == -1)
        printf("Элемент не найден");
    else
        printf("Элемент найден по индексу %d\n", result);

    return 0;
}
