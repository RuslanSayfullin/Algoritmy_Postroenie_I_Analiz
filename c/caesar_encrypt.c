#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Функция для шифрования текста шифром Цезаря
void caesarEncrypt(char* text, int shift) {
    int i = 0;
    while (text[i] != '\0') {
        // Проверяем, является ли символ буквой английского алфавита
        if ((text[i] >= 'A' && text[i] <= 'Z') || (text[i] >= 'a' && text[i] <= 'z')) {
            // Вычисляем сдвиг для текущего символа
            int offset = (text[i] >= 'a') ? 'a' : 'A';
            // Применяем сдвиг и заменяем символ в тексте
            text[i] = ((text[i] - offset + shift) % 26) + offset;
        }
        i++;
    }
}

int main() {
    // Входной текст для шифрования
    char text[100];
    printf("Введите текст для шифрования: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0'; // Удаляем символ новой строки из входного текста
    
    // Сдвиг для шифра Цезаря
    int shift;
    printf("Введите сдвиг: ");
    scanf("%d", &shift);
    
    // Шифруем текст
    caesarEncrypt(text, shift);
    
    // Вывод зашифрованного текста
    printf("Зашифрованный текст: %s\n", text);
    
    return 0;
}
