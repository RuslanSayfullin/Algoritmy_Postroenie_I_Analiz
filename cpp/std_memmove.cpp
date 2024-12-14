#include <iostream>
#include <cstring>

// Функция memmove используется для копирования блока памяти из одного места в другое. 
int main() {
    char str[] = "1234567890";
    std::cout << str << '\n';
    std::memmove(str + 4, str + 3, 3);  // копируем из [4, 5, 6] в [4, 6, 7]
    std::cout << str << '\n';
}
