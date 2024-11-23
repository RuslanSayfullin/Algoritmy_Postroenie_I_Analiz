#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // Меняем порядок элементов на обратный
    std::reverse(numbers.begin(), numbers.end());

    std::cout << "Элементы в обратном порядке: ";
    for (int n : numbers) {
        std::cout << n << " ";
    }
    // Вывод элементов в обратном порядке
    return 0;
}