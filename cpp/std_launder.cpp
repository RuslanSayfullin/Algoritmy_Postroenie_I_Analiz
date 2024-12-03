#include <new>
#include <iostream>

struct MyClass {
	const int value;
	MyClass(int v) : value(v) {}
};

int main() {
	alignas(MyClass) char buffer[sizeof(MyClass)];
	new(buffer) MyClass(42);

	MyClass* p = reinterpreter_cast<MyClass*>(buffer);
	std::cout << p->value << std::endl;	// Может привести к неопределенному поведению
	
	p = std::launder(reinterpreter_cast<MyClass*>(buffer));
	std::cout << p->value << std::endl;	// Всё ok
	return 0;
}
