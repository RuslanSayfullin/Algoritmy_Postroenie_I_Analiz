#include <iostream>
#include <future>

/* В C++ std::async - это шаблон функции, предоставляемый стандартной библиотекой <future>. 
Он используется для асинхронного выполнения функции или вызываемого объекта и 
получения объекта future, представляющего результат вычислений
*/

int AddNumbers(int a, int b) {
    return a + b;
}

int main() {
    // Asynchronously execute AddNumbers(5, 10)
    std::future<int> futureSum = std::async(AddNumbers, 5, 10);

    // Perfoms other tasks concurrently with AddNumbers

    // Retrive the result when needed
    int result = futureSum.get();

    std::cout << "Sum: " << result << std::endl;

    return 0;
}