#include <stdio.h>
#include <stdbool.h>
#include <string.h>

void sieveOfEratosthenes(int n) {
    // Создаем массив для хранения простых чисел
    bool prime[n + 1];
    memset(prime, true, sizeof(prime));

    // Значения 0 и 1 не являются простыми числами
    prime[0] = prime[1] = false;

    // Проверяем каждое число от 2 до sqrt(n)
    for (int p = 2; p * p <= n; p++) {
        // Если prime[p] не изменено, оно простое
        if (prime[p] == true) {
            // Обновляем все кратные p числа, начиная с p*p
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }

    // Выводим все простые числа
    for (int p = 2; p <= n; p++) {
        if (prime[p])
            printf("%d ", p);
    }
}

int main() {
    int n = 30;
    printf("Простые числа до %d: ", n);
    sieveOfEratosthenes(n);
    return 0;
}
