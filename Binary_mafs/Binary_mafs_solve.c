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
	char *tokens; 
	file = fopen(argv[1],"r");
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}	
	while (fgets(str,1024,file) != NULL) {
		tokens = strtok(str, " ");
		int sum = 0;
		int val;
		while (tokens != NULL) {
			val = strtol(tokens+2,NULL,2);
			sum += val;
			tokens = strtok(NULL, " ");
		}
		printf("%d\n",sum);
	}
	fclose(file);
	return(0);

}
