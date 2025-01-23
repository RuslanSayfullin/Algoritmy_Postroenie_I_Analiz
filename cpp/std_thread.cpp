#include <iostream>
#include <thread>

/* std::thread является частью стандартной библиотеки C++ и 
предоставляет возможность создания и управления потоками выполнения. */

// Функция, которая будет выполняться в отдельном потоке
void threadFunction(int id) {
    std::cout << "Hello from thread " << id << std::endl;
}

int main() {
    // Создание объекта std::thread и запуск потока
    std::thread t1(threadFunction, 1);

    // ожидание завершения потока
    t1.join();

    std::cout << "Main thread continues... \n";

    return 0;
}