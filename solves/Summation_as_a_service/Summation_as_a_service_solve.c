#include <stdio.h>

int main(int argc, char* argv[])
{
	if (argc!=2) {
		perror("usage: summation <inputfile>");
		return(-1);
	}
	FILE *file;
	char str[256];
	file = fopen(argv[1],"r");
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}	
	while (fgets(str,sizeof str,file) != NULL) {
		int sum = 0;
		int i, x, y, min, max;
		sscanf(str, "%d %d", &x, &y);
		if (x > y) {
			max = x;
			min = y;
		}
		else {
			max = y;
			min = x;
		}
		for (i=min; i<=max; i++) {
			sum += i;
		}
		printf("%d\n",sum);
	}
	fclose(file);
	return(0);

}
