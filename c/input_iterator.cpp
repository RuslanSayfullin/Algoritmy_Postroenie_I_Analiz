#include <iostream>
#include <vector>

int main() {
	std::vector<int> v = {1, 2, 3, 4, 5};

	// Итератоп на первый элемент контейнера
	auto it = v.begin();


	// Вывод значения первого элемента
	std::cout << *it << std::endl;

	// Перемещение итератора на следующий элемент
	it++;

	// Вывод значения второго элемента
	std::cout << *it << std::endl;

	return 0;
}
