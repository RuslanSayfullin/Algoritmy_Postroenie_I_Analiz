#include <stdio.h>
#include <string.h>

// Функция для шифрования методом перестановки
void encrypt(char* plaintext, int key) {
    int length = strlen(plaintext);
    char ciphertext[length];

    // Заполняем массив ciphertext пробелами
    for (int i = 0; i < length; i++) {
        ciphertext[i] = ' ';
    }

    // Заполняем массив ciphertext зашифрованными символами
    int index = 0;
    for (int i = 0; i < key; i++) {
        for (int j = i; j < length; j += key) {
            ciphertext[j] = plaintext[index++];
        }
    }

    // Выводим зашифрованный текст
    printf("Зашифрованный текст: %s\n", ciphertext);
}

int main() {
    char plaintext[100];
    int key;

    printf("Введите текст для шифровки: ");
    fgets(plaintext, 100, stdin);

    printf("Введите ключ шифрования: ");
    scanf("%d", &key);

    encrypt(plaintext, key);

    return 0;
}

