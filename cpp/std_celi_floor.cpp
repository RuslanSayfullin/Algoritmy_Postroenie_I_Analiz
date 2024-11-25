#include <iostream>
#include <cmath>

// В C++ функции std::ceil и std::floor из заголовка <cmath> используются для округления числа вверх или вниз до ближайшего целого. 
// Это полезно для контроля направления округления.

int main() {
    double number1 = 5.7;
    double number2 = 5.2;

    // Округление вверх (celi)
    std::cout << "Округляем вверх " << number1 << ": " << std::ceil(number1) << std::endl; // 6
    std::cout << "Округляем вверх " << number2 << ": " << std::ceil(number2) << std::endl; // 6

    // Округление вниз (floor)
    std::cout << "Округляем вниз " << number1 << ": " << std::floor(number1) << std::endl; // 5
    std::cout << "Округляем вниз " << number2 << ": " << std::floor(number2) << std::endl; // 5

}