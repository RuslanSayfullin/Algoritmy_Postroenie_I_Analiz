#include <algorithm>
#include <iostream>

int main() {
	int arr[] = {1, 5, 3, 2, 4};

	// Сортируем диапозон элементов arr в порядке возрастания
	std::sort(arr, arr + 5);

	// Выводим отсортированный диапозон элементов.
	for (int i = 0; i < 5; ++i) {
		std::cout << arr[i] << " ";
	}

	std::cout << std::endl;

	return 0;
}
