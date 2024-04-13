#include <iostream>
#include <future>

int main() {
	std::future<int> future = std::async(std::launch::async, [] () {
			return  1 / 0;
	});

	try {
		int value = future.get();
	} catch (std::future_error& e) {
		std::cout << e.what() << std::endl;
	}
	return 0;
}

