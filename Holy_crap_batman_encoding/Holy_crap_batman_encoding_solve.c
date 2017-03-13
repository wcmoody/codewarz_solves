#include <stdio.h>
#include <netdb.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>


long long count1s(long long number) {
	long long count, val;
	count = 0;
	val = number;
	while (val > 0) {
		count += val % 2;
		val = val >> 1;
	}
	return count;
}

int main(int argc, char *argv[])
{
	int sockfd, portno, n;	
	struct sockaddr_in serv_addr;
	struct hostent *server;
	char *hostname;
	char buffer[1024];
	char flag[1024];
	char *wordtokens, *lettertokens, *endword, *endletter;
	int i;
	long long j;
	FILE *file;
	char payload[32] = "ZZZ\n";
	char letters[27] = "ZYXWVUTSRQPONMLKJIHGFEDCBA";

	if (argc<2) {
		fprintf(stderr, "usage: %s filename\n", argv[0]);
		exit(-1);
	}

	file = fopen(argv[1],"r");
	if (file == NULL) {
		perror ("Error opening file");
		return(-1);
	}
	i = 0;
	while (fgets(buffer,1024,file) != NULL) {
		wordtokens = strtok(buffer," ");
		while (wordtokens != NULL) {
			if (i==0) { hostname = wordtokens; i++;}
			else { portno = atol(wordtokens); }
			wordtokens = strtok(NULL, " ");
		}
	}

	sockfd = socket(AF_INET, SOCK_STREAM, 0);

	if (sockfd < 0) {
		perror("Error opening socket");
		exit(-1);
	}

	server = gethostbyname(hostname);

	if (server==NULL) {
		fprintf(stderr,"No such host\n");
		exit(-1);
	}

	bzero(&serv_addr, sizeof (serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(portno);
	bcopy((char*)server->h_addr, (char*)&serv_addr.sin_addr.s_addr, server->h_length);

	if (connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
		perror("Error Connecting");
		exit(-1);
	}

	bzero(buffer,1024);
	n = read(sockfd, buffer, 1024);
	write(sockfd,payload,strlen(payload));
	bzero(buffer,1024);
	n = read(sockfd, buffer, 1024); /* ZZZ encoded */
	n = read(sockfd, buffer, 1024); /* now decode this ...*/
	i = 0;
	while (buffer[i] != ':') { i++; }
	wordtokens = strtok_r(buffer+i+2,"||",&endword);
	i = 0;
	while (wordtokens != NULL) {
		lettertokens = strtok_r(wordtokens,".",&endletter);
		while (lettertokens != NULL) {
			j = atoll(lettertokens);
			j = count1s(j);
			flag[i] = letters[j-1];
			lettertokens = strtok_r(NULL,".",&endletter);
			i ++;
		}
		flag[i] = ' ';
		i ++;
		wordtokens = strtok_r(NULL,"||",&endword);
	}
	flag[i-1]='\0';
	write(sockfd,flag,strlen(flag));
	write(sockfd,"\n",1);
	bzero(buffer,1024);
	n = read(sockfd, buffer, 1024); /* I am just going to leave... */
	bzero(buffer,1024);
	n = read(sockfd, buffer, 1024); /* I am just going to leave... */
	printf("%s",buffer+1);
	close(sockfd);

	return(0);

}
