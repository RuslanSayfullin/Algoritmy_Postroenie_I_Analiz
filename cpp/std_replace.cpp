#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> numbers = {1, 2, 3, 2, 4, 2, 5};

    // Заменяем все 2 на 99
    std::replace(numbers.begin(), numbers.end(), 2, 99);

    std::cout << "После замены: ";
    for (int n : numbers) {
        std::cout << n << " ";
    }
    // Вывод: После замены: 1 99 3 99 4 99 5
    return 0;
}