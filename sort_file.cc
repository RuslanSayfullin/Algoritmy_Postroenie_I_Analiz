    #include <stdio.h>
    #include <string.h>
    #include <conio.h>
    #include <stdlib.h>
     
    void bubble(char *i, int n);
     
    int main(void)
    {
        char *text = NULL;
        int size = 0;
        FILE *f;
        f = fopen("c:\\in.txt", "r");
        if (f != NULL)
        {
            fseek(f, 0, SEEK_END);
            size = ftell(f);
            fseek(f, 0, SEEK_SET);
            text = (char*)malloc(size * sizeof(char)+1);
            fread(text, size, 1, f);
        }
        text[size-1]='\0';
        fclose(f);
        bubble(text, strlen(text));
        printf("%s", text);
        f = fopen("c:\\out.txt", "w");
        fwrite(text, 1, size, f);
     
        free(text);
        fclose(f);
        _getch();
    }
     
    void bubble(char *i, int n)
    {
        int a, b;
        char t;
     
        for (a = 0; a < n-1; a++)
            for (b = n - 2; b >= a; b--)
            {
                if (i[b] > i[b+1])
                {
                    t = i[b];
                    i[b] = i[b+1];
                    i[b+1] = t;
                }
            }
    }


