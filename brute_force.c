#include <stdio.h>

int main() {
int password[5]; // массив для хранения пароля
int i, j, k, m, n;#include <stdio.h>

int main() {
int password[5]; // массив для хранения пароля
int i, j, k, m, n;

// перебор всех возможных комбинаций пароля
for (i = 0; i < 10; i++) {
    for (j = 0; j < 10; j++) {
        for (k = 0; k < 10; k++) {
            for (m = 0; m < 10; m++) {
                for (n = 0; n < 10; n++) {
                    password[0] = i;
                    password[1] = j;
                    password[2] = k;
                    password[3] = m;
                    password[4] = n;

                    // вывод найденного пароля
                    printf("Password: %d%d%d%d%d\n", password[0], password[1], password[2], password[3], password[4]);
                }
            }
        }
    }
}

return 0;
}

