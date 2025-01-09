#include <iostream>
#include <unordered_map>
#include <string>

/*
std::unordered_map - это контейнерный класс, который предоставляет структуру данных, известную как хэш-карта или хэш-таблица. 
Контейнер std::unordered_map хранит элементы в виде пар ключ-значение, где каждый ключ уникален, а производительность зависит от качества хэш-функции, 
используемой для сопоставления ключей с базовыми корзинами.
*/

int main() {
    std::unordered_map<int, std::string> myMap;

    // Inserting key-value pairs
    myMap.insert({1, "John"});
    myMap.insert({2, "Alice"});
    myMap.insert({3, "Bob"});

    // Accessing elements
    std::cout << "value at key 2: " << myMap[2] << std::endl;

    // Updating  an element
    myMap[1] = "Mark";

    // Removing an element
    myMap.erase(3);

    // Iterating over the map
    for (const auto& pair : myMap) {
        std::cout << "Key: " << pair.first << ", Value: " << pair.second << std::endl;
    }

    // Checking if a key exists
    if (myMap.find(2) != myMap.end()) {
        std::cout << "Key 2 exist." << std::endl;
    }

    return 0;
}