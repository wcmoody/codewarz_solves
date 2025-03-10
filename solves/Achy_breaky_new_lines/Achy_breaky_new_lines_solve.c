#include <stdio.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char *argv[])
{
    if (argc!=2) {
        perror("usage: Simple_cipher <inputfile>");
        return(-1);
    }
    FILE *file;
    char str[1024] ;
    int val;
    int i, first;
    char *tokens;
    file = fopen(argv[1],"r");
    if (file == NULL) {
        perror("Error opening file");
        return(-1);
    }
    while (fgets(str,1024,file) != NULL) {
        if (str[0] != '\n') {
            printf("%s",str);
        }
	}
    return(0);

}
