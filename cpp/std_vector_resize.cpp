#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // Уменьшаем размер вектора
    numbers.resize(3);

    std::cout << "После уменьшения размера: ";
    for (int n : numbers) {
        std::cout << n << " ";
    }
    // Вывод: После уменьшения размера: 1 2 3

    // Увеличиваем размер вектора
    numbers.resize(6, 99);

    std::cout << "\nПосле увеличения размера: ";
    for (int n : numbers) {
        std::cout << n << " ";
    }
    // Вывод: После уувеличения размера: 1 2 3 99 99 99

    return 0;
}