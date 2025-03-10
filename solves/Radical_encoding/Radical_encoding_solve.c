#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char* argv[])
{
	if (argc!=2) {
		perror("usage: radical <input_file>");
		return(-1);
	}
	FILE *file;
	char str[1024];
	char *tokens; 
	file = fopen(argv[1],"r");
	int val;
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}	
	while (fgets(str,1024,file) != NULL) {
		tokens = strtok(str, "x");
		while (tokens != NULL) {
			tokens[strlen(tokens)-1] = '\0';
			val = strtol(tokens,NULL,16);
			val = (int)sqrt((double)val);
			printf("%c",(char)val);
			tokens = strtok(NULL, "x");
		}
		printf("\n");
	}
	fclose(file);
	return(0);

}
