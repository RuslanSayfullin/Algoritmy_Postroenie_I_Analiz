#include <stdio.h>

typedef struct {
    int value;
    // Дополнительные поля структуры
} MyStruct;

void swap(MyStruct* a, MyStruct* b) {
    MyStruct temp = *a;
    *a = *b;
    *b = temp;
}

int partition(MyStruct arr[], int low, int high) {
    MyStruct pivot = arr[high];
    int i = low - 1;
  
    for (int j = low; j <= high - 1; j++) {
        if (arr[j].value < pivot.value) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(MyStruct arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    MyStruct arr[] = {
        {10},
        {7},
        {8},
        {9},
        {1},
        {5}
    };
    int n = sizeof(arr) / sizeof(arr[0]);
  
    printf("Исходный массив:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i].value);
    }
  
    quickSort(arr, 0, n - 1);
  
    printf("\nОтсортированный массив:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i].value);
    }
  
    return 0;
}
