#include <stdio.h>

void drawTree(int height) {
    int i, j;
    
    // Выводим каждую строку ёлки
    for (i = 0; i < height; i++) {
        
        // Выводим пробелы перед каждой строкой
        for (j = 0; j < height - i - 1; j++) {
            printf(" ");
        }
        
        // Выводим звездочки для каждой строки
        for (j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        
        // Переходим на следующую строку
        printf("\n");
    }
    
    // Выводим ствол ёлки (только одну звездочку)
    for (i = 0; i < height - 1; i++) {
        printf(" ");
    }
    printf("*\n");
}

int main() {
    int height;
    
    printf("Введите высоту ёлки: ");
    scanf("%d", &height);
    
    drawTree(height);
    
    return 0;
}
