#include <stdio.h>

// Функция для обмена элементов массива
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Рекурсивная функция для сортировки массива
void recursiveBubbleSort(int arr[], int n) {
    // Базовый случай: если массив состоит из одного элемента,
    // то он уже отсортирован
    if (n == 1) {
        return;
    }
    
    // Перебираем элементы массива
    for (int i = 0; i < n - 1; i++) {
        // Если следующий элемент больше текущего, меняем их местами
        if (arr[i] > arr[i + 1]) {
            swap(&arr[i], &arr[i + 1]);
        }
    }
    
    // Рекурсивно вызываем функцию для оставшейся части массива
    recursiveBubbleSort(arr, n - 1);
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    recursiveBubbleSort(arr, n);
    
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    
    return 0;
}
