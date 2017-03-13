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
	char str[1024], hex[3];
	file = fopen(argv[1],"r");
	int val, i;
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}	
	while (fgets(str,1024,file) != NULL) {
		for (i=0;i<strlen(str); i+=2)
		{
			hex[0] = str[i];
			hex[1]= str[i+1];
			hex[2]= '\0';
			val = (int)strtol(hex,NULL,16);
			printf("%c",(char)(val/2));
		}
		printf("\n");
	}
	fclose(file);
	return(0);

}
