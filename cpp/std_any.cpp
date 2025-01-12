#include <any>
#include <iostream>
#include <string>

/*
std::any 
Это функция C++17, которая предоставляет безопасный с точки зрения типов контейнер для единичных значений любого типа. 
*/

int main() {
    std::any val;

    val = 10;   // Store an int
    if (val.type() == typeid(int)) {
        std::cout << std::any_cast<int>(val) << std::endl;  // Retrieve and print the stored int
    }

    val = 3.14f;    // Store a float
    if (val.type() == typeid(float)) {
        std::cout << std::any_cast<float>(val) << std::endl;  // Retrieve and print the stored float
    }

    val = std::string("Hello, world!"); // Store a string
    if (val.type() == typeid(std::string)) {
        std::cout << std::any_cast<std::string>(val) << std::endl;  // Retrieve and print the stored string
    }

    try {
        std::cout << std::any_cast<int>(val) << std::endl;  // Accessing the wrong type throws std::bas_any_cast
    } catch (const std::bad_any_cast& ex) {
        std::cout << "Exception: " << ex.what() << std::endl;
    }
 
    return 0;
}