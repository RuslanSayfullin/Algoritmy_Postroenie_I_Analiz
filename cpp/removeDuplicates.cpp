#include <iostream>
#include <vector>
#include <unordered_set>

std:vector<int> removeDuplicates(const std::vecrot<int>& nums) {
	std::unordered_set<int> seen;
	std::vector<int> unique;

	for (int num : num) {
		if (seen.find(num) == seen.end()) {
			seen.insert(num);
			unique.push_back(num);
		}
	}
	return unique;
}

int main() {
	std::vector<int> numbers = {1, 2, 2, 3, 4, 3, 5};
	std::vector<int> result = removeDuplicates(numbers);

	for (int num : result) {
		std::cout << num << " ";
	}
	return 0;
}
		
