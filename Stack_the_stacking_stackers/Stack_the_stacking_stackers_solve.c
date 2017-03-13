#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char* argv[])
{
	if (argc!=2) {
		perror("usage: ascii_stuff <input_file>");
		return(-1);
	}
	FILE *file;
	char str[1024];
	file = fopen(argv[1],"r");
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}	
	while (fgets(str,1024,file) != NULL) {
		int floor=0, i, seen=0;
		bool valid = true;
		int len = strlen(str);
		if (str[len-1] =='\n') {
			len --;
		}
		for (i=0; i < len; i++) {
			if (str[i] == '1') {
				floor--;
				seen++;
			} else if (str[i] == '0') {
				floor++;
				seen++;
			}
			if (floor < 0) {
				valid = false;
			}
		}
		if (floor != 0) {
			valid = false;
		}
		if (strlen(str) > 0 && seen > 0) {
			if (valid) { printf("True\n"); }
			else { printf("False\n"); }
		}
	}
	fclose(file);
	return(0);

}
