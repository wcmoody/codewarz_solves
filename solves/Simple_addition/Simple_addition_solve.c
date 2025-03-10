#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

int isfloat(char *p) {
    int res = 0;
	char *c = p;
	while (*c != '\0') {
		if (*c == '.') 
            res = 1;
		c += 1;	
	}
	return (res);
}

int iswhole(float f) {
    int res = 1;
	int i = (int)f;
	if ((f-i) != 0) 
        res = 0;
    return (res);
}

void printfloat(float f){
	char str[256];
	int i = 0;
	sprintf(str,"%f",f);
    int j=strlen(str)-1;
    while (str[j] == '0') j--;
    if (str[j-1] == '.') j++;
	while (i != j) {
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
	char str[1024] ;
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
		if (!fp1 && !fp2) 
            printf("%d\n",atoi(p1)+atoi(p2));
		else {
            printfloat(atof(p1)+atof(p2));
		}
	}
	return(0);

}
