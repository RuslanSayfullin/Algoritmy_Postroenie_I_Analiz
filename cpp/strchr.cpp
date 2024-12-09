#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char str[] = "This is a string";
    char * ch = strchr(str, 'a');
    cout << ch - str +1;
    return 0;

}

// Вывод: 9