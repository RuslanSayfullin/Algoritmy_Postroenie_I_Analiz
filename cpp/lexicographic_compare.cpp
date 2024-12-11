#include <iostream>
#include <algorithm>

using namespace std;

// Совершает лексикографическое сравнение 2 диапазонов
int main() {
    // Initializing char arrays
    char one[] = "geeksforgeeks";
    char two[] = "gfg";

    // using lexicographical_compare for checking
    // is "one" is less thsn "two"
    if (lexicographical_compare(one, one+13, two, two+3)) {
        cout << "geekforgeeks is lexicographically less than gfg";
    } else {
        cout << "geekforgeeks is not lexicographically less than gfg";
    }
}