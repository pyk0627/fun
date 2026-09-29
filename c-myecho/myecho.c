#include <stdio.h>
#include <stdlib.h>
int main(int argc,char *argv[])
{
    argv++;
    while(*argv)
    {
        fputs(*argv,stdout);
        argv++;
        if(*argv)
        {
            putchar(' ');
        }
    }
    putchar('\n');
    return EXIT_SUCCESS;
}
