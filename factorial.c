#include <stdio.h>

int main() {
    int n, факториал = 1;
    
    printf("Введите число: ");
    scanf("%d", &n);
    
    if (n < 0) {
        printf("Ошибка! Факториал отрицательного числа не определен.\n");
        return 0;
    }
    
    if (n == 0 || n == 1) {
        printf("Факториал числа %d равен %d.\n", n, факториал);
        return 0;
    }
    
    for (int i = 1; i <= n; i++) {
        факториал *= i;
    }
    
    printf("Факториал числа %d равен %d.\n", n, факториал);
    
    return 0;
}
