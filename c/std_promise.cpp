#include <iostream>
#include <future>

int main() {
	std::promise<int> promise;
	std::future<int> future = promise.get_future();

	// Поставщик
	std::thread producer([&promise] {
		promise.set_value(42);
	});

	// Потребитель
	std::thread consumer([&future] {
		int value = future.get();
		std::cout << "Потребитель получил значение: " << value << std::endl;
	});

	producer.join();
	consumer.join();

	return 0;
}
