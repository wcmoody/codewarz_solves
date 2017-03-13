#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

int isfloat(char *p) {
	char *c = p;
	while (*c != '\0') {
		if (*c == '.') {
			return (1);
		}
		c += 1;	
	}
	return (0);
}

int iswhole(float f) {
	int i = (int)f;
	if ((f-i) != 0) {
		return (0);
	}
	else {
		return (1);
	}
}

void printfloat(float f){
	char str[256];
	int i = 0;
	sprintf(str,"%f",f);
	while (str[i] != '.') {
		printf("%c",str[i]);
		i++;
	}
	printf("\n");
}


int main(int argc, char* argv[])
{
	if (argc!=2) {
		perror("usage: evenly <inputfile>");
		return(-1);
	}
	FILE *file;
	char str[256] ;
	char p1[256], p2[256];
	int fp1, fp2;
	int i;
	double j;
	file = fopen(argv[1],"r");
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}
	while (fgets(str,256,file) != NULL) {	
		sscanf(str, "%s %s\n", p1, p2);
		fp1 = isfloat(p1);
		fp2 = isfloat(p2);
		int count = 0;
		if (!fp1 && !fp2) {
			for (i=abs(atoi(p1)); i<=atoi(p2); i+= abs(atoi(p1))) {
				printf("%d\n",i);
				count++;
			}		
		}
		/*if (!fp1 && fp2) { */
		else {
			for (j=fabs(atof(p1)); j <= atoi(p2); j += fabs(atof(p1))) {
				if (iswhole(j)) {
					printfloat(j);
					count ++;
				}
			}
		}
		if (count > 0) {
			printf("\n");
		}

	}
	return(0);

}
