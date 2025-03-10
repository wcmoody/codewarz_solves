#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char* argv[])
{
	if (argc!=2) {
		perror("usage: forward <input_file>");
		return(-1);
	}
	FILE *file;
	char str[1024];
	int i;
	file = fopen(argv[1],"r");
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}	
	while (fgets(str,1024,file) != NULL) {
		bool match = true;
		int len = strlen(str);
		if (str[len-1] == '\n') { len --; }
		for (i=0; i < len; i++) {
			if (str[i] != str[len-1-i]) {
				match = false;
			}
		}
		if (match) {
			printf("True\n");
		} else {
			printf("False\n");
		}
		
	}
	fclose(file);
	return(0);

}
