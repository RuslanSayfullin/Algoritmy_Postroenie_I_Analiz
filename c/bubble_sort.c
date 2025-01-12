#include <stdio.h>
#include <string.h>

typedef struct {
    int id;
    char name[50];
} Person;

void bubbleSort(Person arr[], int n) {
    int i, j;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j].id > arr[j+1].id) {
                // Меняем местами две структуры
                Person temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int n;
    printf("Введите количество структур: ");
    scanf("%d", &n);

    Person persons[n];
    for (int i = 0; i < n; i++) {
        printf("Введите id и имя для структуры %d:\n", i+1);
        scanf("%d %[^\n]s", &persons[i].id, persons[i].name);
    }

    bubbleSort(persons, n);

    printf("Отсортированный список структур:\n");
    for (int i = 0; i < n; i++) {
        printf("id: %d, имя: %s\n", persons[i].id, persons[i].name);
    }

    return 0;
}
