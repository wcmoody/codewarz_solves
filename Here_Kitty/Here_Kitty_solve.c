#include <stdio.h>

int main(int argc, char* argv[])
{
	if (argc!=2) {
		perror("usage: here_kitty <inputfile>");
		return(-1);
	}
	FILE *file;
	char str[80];
	file = fopen(argv[1],"r");
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}	
	while (fgets(str,80,file) != NULL) {
		fputs(str,stdout);
	}
	fclose(file);
	return(0);

}
