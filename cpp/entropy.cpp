#include <algorithm>
#include <iostream>
#include <cmath>

int main() {
	// Алфавит
	std::vector<char> alphabet = {'a', 'b', 'c', 'd'};

	// Распределение вероятностей
	std::vector<double> probabilities = {0.25, 0.25, 0.25, 0,25};

	// Вычисление энтропии
	double entropy = std::entropy(probabilities.begin(), probabilities.end());

	// Вывод результата
	std::cout << "Энтропия: " << entropy << std::endl;

	return 0;
}
