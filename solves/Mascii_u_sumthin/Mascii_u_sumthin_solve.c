#include <stdio.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char *argv[])
{
    if (argc!=2) {
        perror("usage: Mascii_u_sumthin <inputfile>");
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
        tokens = strtok(str, " ");
        while (tokens != NULL) {
            if (tokens[0] == '0') {
                if (tokens[1] == 'x') val = strtol(tokens+2, NULL, 16);
                else if (tokens[1] == 'b') val = strtol(tokens+2, NULL, 2);
                else val = strtol(tokens+1,NULL, 8);
            } else val = atoi(tokens);
            tokens = strtok(NULL, " ");
            printf("%c",val);

        }
	}
    return(0);

}
