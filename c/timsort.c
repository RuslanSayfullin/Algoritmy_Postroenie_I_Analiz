#include <stdio.h>
#include <stdlib.h>

#define MIN_MERGE 32
#define MIN_GALLOP 7

void insertionSort(int arr[], int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void merge(int arr[], int left, int mid, int right) {
    int len1 = mid - left + 1;
    int len2 = right - mid;

    int* leftArr = (int*)malloc(len1 * sizeof(int));
    int* rightArr = (int*)malloc(len2 * sizeof(int));

    for (int i = 0; i < len1; i++)
        leftArr[i] = arr[left + i];
    
    for (int i = 0; i < len2; i++)
        rightArr[i] = arr[mid + i + 1];

    int i = 0, j = 0, k = left;

    while (i < len1 && j < len2) {
        if (leftArr[i] <= rightArr[j])
            arr[k++] = leftArr[i++];
        else
            arr[k++] = rightArr[j++];
    }

    while (i < len1)
        arr[k++] = leftArr[i++];
    
    while (j < len2)
        arr[k++] = rightArr[j++];

    free(leftArr);
    free(rightArr);
}

int minRunLength(int n) {
    int r = 0;
    while (n >= MIN_MERGE) {
        r |= n & 1;
        n >>= 1;
    }
    return n + r;
}

int binarySearch(int arr[], int key, int low, int high) {
    int mid;
    while (low <= high) {
        mid = (low + high) >> 1;
        
        if (arr[mid] < key)
            low = mid + 1;
        else if (arr[mid] > key)
            high = mid - 1;
        else
            return mid;
    }
    return low;
}

void timsort(int arr[], int n) {
    int minRun = minRunLength(MIN_MERGE);
    for (int i = 0; i < n; i += minRun) {
        int left = i;
        int right = (i + minRun - 1 < n) ? (i + minRun - 1) : (n - 1);
        insertionSort(arr, left, right);
    }
    for (int size = minRun; size < n; size <<= 1) {
        for (int left = 0; left < n; left += (size << 1)) {
            int mid = left + size - 1;
            int right = (left + (size << 1) - 1 < n) ? (left + (size << 1) - 1) : (n - 1);
            merge(arr, left, mid, right);
        }
    }
}

int main() {
    int arr[] = {5, 2, 1, 4, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Before sorting:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    
    timsort(arr, n);
    
    printf("After sorting:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}
