#include <stdio.h>
#include <time.h>

void permute(char *str, int start, int end)
{
    if (start == end)
    {
        printf("%s\n", str); // Выводим каждую перестановку
        return;
    }
    
    for (int i = start; i <= end; i++)
    {
        // Меняем символы местами
        char temp = str[start];
        str[start] = str[i];
        str[i] = temp;
        
        // Рекурсивный вызов для подстроки с увеличенным индексом
        permute(str, start + 1, end);
        
        // Возвращаем символы на свои места
        temp = str[start];
        str[start] = str[i];
        str[i] = temp;
    }
}

int main()
{
    char str[] = "code";
    int n = sizeof(str) - 1; // Вычисляем длину строки
    
    clock_t begin = clock(); // Замер времени начинается
    
    permute(str, 0, n - 1);
    
    clock_t end = clock(); // Замер времени заканчивается
    
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Время работы: %f секунд\n", time_spent);
    
    return 0;
}
