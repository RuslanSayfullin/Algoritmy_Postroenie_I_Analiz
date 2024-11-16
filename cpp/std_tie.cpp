#include <iostream>
#include <tuple>

std::tuple<int, double, std::string> getData() {
    return {42, 3.14, "Hello"};
}

int main() {
    int a;
    double b;
    std::string c;

    // Распаковываем значение из кортежа
    std::tie(a, b, c) = getData();

    std::cout << "a: " << a << ", b: " << b << ", c: " << c << std::endl;
    return 0; 
}