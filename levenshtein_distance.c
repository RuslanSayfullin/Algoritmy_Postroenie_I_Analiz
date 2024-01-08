#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int min(int a, int b, int c) {
    if (a < b && a < c) {
        return a;
    } else if (b < a && b < c) {
        return b;
    } else {
        return c;
    }
}

int levenshteinDistance(char *s1, char *s2) {
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    
    int dp[len1+1][len2+1];
    int i, j;
    
    for (i = 0; i <= len1; i++) {
        for (j = 0; j <= len2; j++) {
            if (i == 0) {
                dp[i][j] = j;
            } else if (j == 0) {
                dp[i][j] = i;
            } else if (s1[i-1] == s2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]);
            }
        }
    }
    
    return dp[len1][len2];
}

int main() {
    char s1[] = "kitten";
    char s2[] = "sitting";
    
    int distance = levenshteinDistance(s1, s2);
    
    printf("Редакторское расстояние между строками '%s' и '%s' равно %d.\n", s1, s2, distance);
    
    return 0;
}
