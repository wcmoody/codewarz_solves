#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char* argv[])
{
	if (argc!=2) {
		perror("usage: my_buckets <inputfile>");
		return(-1);
	}
	int MAXSIZE = 4096;
	int i;
	int counts[MAXSIZE];
	int max;
	for (i=0; i<MAXSIZE; i++) {
		counts[i] = 0;
	}
	FILE *file;
	char str[256] ;
	file = fopen(argv[1],"r");
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}
	while ((fgets(str,256,file)) != NULL) {
		if (strlen(str) > 0) {
			counts[atoi(str)/10]++;	
		}
	}
	fclose(file);
	for (i=0; i<MAXSIZE; i++) {
		if (counts[i]!=0) {
			max = i;
		}	
	}
	for (i=0; i<=max; i++) {
		printf("%d",counts[i]);
	}
	printf("\n");
	return(0);

}
