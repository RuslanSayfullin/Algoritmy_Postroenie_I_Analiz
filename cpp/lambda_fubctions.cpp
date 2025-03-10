#include <iostream>
#include <vector>
#include <algorithm>

// Лямбда-функция (или просто лямбда) — это анонимная функция в C++, которая может быть определена непосредственно внутри кода.
int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // Используем лямбду для вывода каждого числа
    std::for_each(numbers.begin(), numbers.end(), [](int num) {
        std::cout << num << " ";
    });

    std::cout << std::endl;
    return 0;
}