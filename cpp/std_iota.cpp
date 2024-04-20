#include <iostream>
#include <vector>
#include <numeric>	// Для std::iota

int main() {
	std::vector<int> numbers(10);
	int startValue = 1;

	// Заполняет вектор последовательными числами, начиная с startValue
	std::iota(numbers.begin(), numbers.end(), startValue);

	// Выводит заполненный вектор
	std::cout << "Заполненный вектор: ";
	for (const auto& num : numbers) {
		std::cout << num << " ";
	}
	std::cout << std::endl;
}
