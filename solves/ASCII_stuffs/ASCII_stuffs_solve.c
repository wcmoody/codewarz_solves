#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	if (argc!=2) {
		perror("usage: ascii_stuff <input_file>");
		return(-1);
	}
	FILE *file;
	char str[1024];
	char *tokens, chr;
	file = fopen(argv[1],"r");
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}	
	while (fgets(str,1024,file) != NULL) {
		tokens = strtok(str, " ");
		while (tokens != NULL) {
			chr = (char)strtol(tokens,NULL,16);
			printf ("%c",chr);
			tokens = strtok(NULL, " ");
		}
	}
	fclose(file);
	return(0);

}
