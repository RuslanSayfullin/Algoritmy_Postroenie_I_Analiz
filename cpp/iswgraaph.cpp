#include <iostream>
#include <cwtype>

int main() {
	wchar_t wideChar = L'Я';
	if (iswgraph(wideChar)) {
		std::wcout << L"Символ широкого графика" << std::endl;
	} else {
		std::wcout << L"Символ не является широким графическим символом" << std::endl;
	}

	return 0;
}
