#include <stdio.h>
#include<string.h>
#include<stdlib.h>


int single_lowercase(char *word) {
    int res = 0;
    int i;
    for (i=0;i<strlen(word);i++) {
        if (word[i]<65 || word[i]>90) res = 1; 
    }
    return (res);
}

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
        tokens = strtok(str, " ");
        first = 1;
        while (tokens != NULL) {
            if (tokens[0] >= 65 && tokens[0] <= 90 &&
                    single_lowercase(tokens+1)) {
                if (first==1) first = 0;
                else printf(" ");
                printf("%s", tokens);
            }
            tokens = strtok(NULL, " ");
        }
        printf("\n");
	}
    return(0);

}
