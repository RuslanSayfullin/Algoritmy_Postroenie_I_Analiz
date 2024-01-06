#include <stdio.h>

// Define the structure
struct Student {
    int id;
    char name[50];
};

void insertionSort(struct Student arr[], int n) {
    int i, j;
    struct Student key;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        // Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while (j >= 0 && arr[j].id > key.id) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void printArray(struct Student arr[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        printf("ID: %d, Name: %s\n", arr[i].id, arr[i].name);
    }
}

int main() {
    struct Student students[] = {
        {4, "John"},
        {2, "Alice"},
        {1, "Bob"},
        {3, "Charlie"},
    };
    int n = sizeof(students) / sizeof(students[0]);

    printf("Array before sorting:\n");
    printArray(students, n);

    insertionSort(students, n);

    printf("\nArray after sorting:\n");
    printArray(students, n);

    return 0;
}
