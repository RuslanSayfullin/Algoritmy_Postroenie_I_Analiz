#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Определение структуры
struct Person {
    char name[50];
    int age;
};

// Функция для сравнения двух структур по возрасту
int compare(const void* a, const void* b) {
    struct Person* personA = (struct Person*)a;
    struct Person* personB = (struct Person*)b;

    return personA->age - personB->age;
}

// Функция для сортировки массива структур по возрасту
void selectionSort(struct Person arr[], int n) {
    int i, j, minIndex;
    struct Person temp;

    for (i = 0; i < n - 1; i++) {
        // Находим минимальный элемент в несортированной части массива
        minIndex = i;
        for (j = i + 1; j < n; j++) {
            if (compare(&arr[j], &arr[minIndex]) < 0) {
                minIndex = j;
            }
        }

        // Меняем местами текущий элемент с минимальным элементом
        temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

int main() {
    int i;

    struct Person people[] = {
        {"John", 25},
        {"Alice", 30},
        {"Bob", 20},
        {"Jane", 35},
    };

    int n = sizeof(people) / sizeof(people[0]);

    // Вывод исходного массива структур
    printf("Исходный массив:\n");
    for (i = 0; i < n; i++) {
        printf("%s - %d\n", people[i].name, people[i].age);
    }

    // Сортировка выбором
    selectionSort(people, n);

    // Вывод отсортированного массива структур
    printf("\nОтсортированный массив:\n");
    for (i = 0; i < n; i++) {
        printf("%s - %d\n", people[i].name, people[i].age);
    }

    return 0;
}
