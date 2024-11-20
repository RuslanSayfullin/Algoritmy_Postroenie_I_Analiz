#include <iostream>
#include <vector>
#include <algorithm>

int main() {
	std::vector<int> numbers = {1, 2, 3, 4, 5};

	// Сдвигаем элементы, начиная с третьего
	std::rotate(numbers.begin(), numbers.begin() + 2, numbers.end());

	// Выводим результат
	std::cout << "После сдвига: ";
	for (int n : numbers) {
		std::cout << n << " ";
	}
	// Вывод: После сдвига: 3 4 5 1 2
	return 0;
}
