#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

// Сравнивает две последовательности и находит первую позицию, где элементы различны.
// Возвращается пара итераторов, каждый из которых указывает на эту позицию в соответствующей последовательности.
// Если все элементы одинаковы, то каждый итератор в паре указывает на элемент last в своем контейнере.

int main() {
    std::vector<int> myvector;
    for (int i=1; i<6; i++) myvector.push_back (i*10);  // myvector: 10 20 30 40 50

    int myints[] = {10,20,80,320,1024};                 // myints: 10 20 80 320 1024

    std::pair<std::vector<int>::iterator,int*> mypair;

    // using default comparison:
    mypair = std::mismatch (myvector.begin(), myvector.end(), myints);
    std::cout << "First mismatching elements: " << *mypair.first;
    std::cout << " and " << *mypair.second << '\n';

    ++mypair.first; ++mypair.second;

    // using predicate comparison:
    mypair = std::mismatch (myvector.begin(), myvector.end(), myints);
    std::cout << "Second mismatching elements: " << *mypair.first;
    std::cout << " and " << *mypair.second << '\n';


    return 0;
}

// First mismatching elements: 30 and 80
// Second mismatching elements: 40 and 320