#include <utility>
#include <iostream>

using namespace std;

struct C
{
    int i;
};

int main()
{
	C c1{ 1 };
	C c2{ 2 };

	C result = exchange(c1, c2);

	cout << "Старое значение с1: " << result.i << endl;
	cout << "Новое значение с1 после обновления: " << c1.i << endl;

	return 0;
}
