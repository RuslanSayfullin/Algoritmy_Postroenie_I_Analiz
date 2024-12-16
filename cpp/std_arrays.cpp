#include <iostream>
#include <array>
#include <algorithm>
//using namespace std;

template <typename Type, std::size_t... sizes>
auto concatenate(const std:array<Type, size>&... arrays)
{
    std::array<Type, (size + ...)> result;
    std::size_t index{};

    ((std::copy_n(arrays.begin(), sizes, result.begin() + index), index += sizes), ...);

    return result;
}

int main() {
    std::array<int, 3> first = {{1, 2, 3}};
    std::array<int, 2> second = {{4, 5}};

    auto result = concatenate(first, second);
    for (auto &i: result) {
        std::cout << i << ' ';
    }

    return 0;
}