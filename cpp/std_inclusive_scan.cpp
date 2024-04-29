#include <iostream>
#include <numeric>
#include <vector>

int main() {
	std::vector <int> numbers = {1, 3, 5, 2};
	std::vector <int> prefix_sums(numbers.size());

	std::inclusive_scan(numbers.begin(), numbers.end(), prefix_sums.begin(), 0);

	for (int sum : prefix_sums) {
		std::cout << sum << " ";
	}

	return 0;
}
