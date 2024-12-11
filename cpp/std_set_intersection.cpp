#include <iostream>
#include <vector>
#include <algorithm>


// Функция std::set_intersection из заголовка <algorithm> позволяет найти пересечение двух отсортированных контейнеров. 
// Результат записывается в другой контейнер.
int main() {
    std::vector<int> set1 = {1, 2, 3, 4};
    std::vector<int> set2 = {3, 4, 5, 6};
    std::vector<int> result;

    // Находим пересечение
    std::set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(), std::back_inserter(result));

    // Выводим результат
    std::cout << "Общие элементы: ";
    for (int n : result) {
        std::cout << n << " ";
    }

    return 0;
}