#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

// Создает отсортированную последовательность из элементов, встречающихся в обеих последовательностях – [first1, last1) и [first2, last2).
int main() {
    std::vector<int> v1{1, 2, 3, 4, 5, 6, 7, 8};
    std::vector<int> v2{5, 7, 9, 10};
    std::sort(v1.begin(), v1.end());
    std::sort(v2.begin(), v2.end());

    std::vector<int> v_intersection;

    std::set_intersection(v1.begin(), v1.end(), v1.begin(), v2.end(),
    std::back_inserter(v_intersection));

    for(int n : v_intersection)
        std::cout << n << ' ';

}