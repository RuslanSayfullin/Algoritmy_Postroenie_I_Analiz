#include <stdio.h>
#include <stdbool.h>

int countUniqueObjects(char* str) {
   int count = 0;
   bool unique[256] = {false};

   for (int i = 0; str[i] != '\0'; i++) {
      if (unique[str[i]] == false) {
         count++;
         unique[str[i]] = true;
      }
   }

   return count;
}

int main() {
   char str[] = "abcaadefg";
   int uniqueCount = countUniqueObjects(str);

   printf("Количество уникальных объектов: %d\n", uniqueCount);

   return 0;
}
