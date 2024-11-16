#include <variant>
#include <iostream>
#include <string>


int main() {
    std::variant<int, double, std::string> var = 42;

    // Определяем посетителя с помощью лямбда-функции
    auto visitor = [](auto&& arg) {
        std:: cout << "Значение: " << arg << std::endl;
    };

    // Применяем к текщему значению варианта
    std::visit(visitor, var);

    // Изменяем значение варианта
    var = std::string("Привет, мир!");

    // повторно применяем visitor
    std::visit(visitor, var);

    return 0;
}
