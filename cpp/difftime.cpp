#include <iostream>
#include <ctime>

int main() {
	time_t startTime, endTime;
	time(&startTime);	// Получаем текущее время в startTime
	// Некоторые операции или задержки
	time(&endTime);		// Получаем текущее время в endTime
	
	double difference = difftime(endTime, startTime);	// Вычисляем разницу времени
	
	std::cout << "Пришло " << difference << " секунд." << std::endl;
	return 0;
}
