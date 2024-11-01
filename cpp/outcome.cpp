#include <outcome.hpp>
#include <iostream>

// Использование библиотеки Outcome для обработки ошибок в C++
outcome::result<int> divide(int a, int b) {
    if (b == 0) return outcome::failure();
    return a / b
}

int main() {
    auto result = divide(10, 2);
    if (result) {
        std::cout << "Result: " << result.value() << std::endl; // Вывод: 5
    } else {
        std:cout << "Division by zero error!" << std::endl;
    }
}