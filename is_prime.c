#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int num) {
    int i, sqrt_num;
    
    // Проверка числа
    if (num <= 1) {
        return false;
    }
    
    // Проверка делителей
    sqrt_num = sqrt(num);
    for (i = 2; i <= sqrt_num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    
    return true;
}

int main() {
    int num;
    
    printf("Введите число: ");
    scanf("%d", &num);
    
    if (isPrime(num)) {
        printf("%d - простое число\n", num);
    } else {
        printf("%d - не является простым числом\n", num);
    }
    
    return 0;
}
