#include <glaze/glaze.hpp>
#include <iostream>

// Использование библиотеки Glaze для сериализации данных в C++
struct Person {
    std::string name;
    int age;
}

int main() {
    Person p{"Alice", 30};
    std::string json = glaze:serialize(p);
    std::cout << json << std:endl;
}