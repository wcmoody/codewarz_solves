#include <stdio.h>

int main(int argc, char *argv[])
{
    if (argc!=2) {
        perror("usage: Find_random_stuff <inputfile>");
        return(-1);
    }
    FILE *file;
    char str[256] ;
    int start, stop;
    int i, first;
    file = fopen(argv[1],"r");
    if (file == NULL) {
        perror("Error opening file");
        return(-1);
    }
    while (fgets(str,256,file) != NULL) {
        sscanf(str, "%d %d\n", &start, &stop);
        first = 1; 
        for (i=start; i<=stop; i++) {
            if ((i%7 == 0) && (i%5 != 0)) {
                if (first==1) first = 0;
                else printf(",");
                printf("%d",i);
            }
        }
        printf("\n");
	}
    return(0);

}
