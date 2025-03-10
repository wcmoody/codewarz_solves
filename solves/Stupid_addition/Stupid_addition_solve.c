#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>


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

void nozeros(float f) {
	int i, last;
	char str[256];
	sprintf(str,"%f",f);
	for (i=0; i < strlen(str); i++) {
		if (str[i] != '0') { last = i; }
	}
	for (i=0; i <= last; i++) {
		printf("%c",str[i]);
	}	
	printf ("\n");
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


int main(int argc, char* argv[])
{
	if (argc!=2) {
		perror("usage: stupid <inputfile>");
		return(-1);
	}
	FILE *file;
	char str[256] ;
	int rc;
	float x, y, sum;
	file = fopen(argv[1],"r");
	if (file == NULL) {
		perror("Error opening file");
		return(-1);
	}
	while (fgets(str,256,file) != NULL) {	
		rc = sscanf(str, "%f %f\n", &x, &y);
		if (rc!=2) {continue;}
		sum = x + y;
		if (iswhole(sum)) { printfloat(sum); }
		else { nozeros(sum); }

		
	}
	return(0);

}
