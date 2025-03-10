#include <stdio.h>
#include <netdb.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	int sockfd, portno, n;	
	struct sockaddr_in serv_addr;
	struct hostent *server;
	char buffer[256];
	char key[256];
	int i,j;
	char flag[512];
	char payload[512];
	char allchar[76] = "{}_!@#$%^&*()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

	if (argc<3) {
		fprintf(stderr, "usage: %s hostname portnumber\n", argv[0]);
		exit(-1);
	}

	memset(flag,'?',511);
	flag[511]='\0';

	portno  = atoi(argv[2]);
	sockfd = socket(AF_INET, SOCK_STREAM, 0);

	if (sockfd < 0) {
		perror("Error opening socket");
		exit(-1);
	}
	server = gethostbyname(argv[1]);
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
	bzero(key,256);
	n = read(sockfd, key, 255);
	sprintf(payload,"getkey\n");
	write(sockfd,payload,strlen(payload));
	bzero(key,256);
	n = read(sockfd, buffer, 255);
	for (i=0; i<strlen(buffer); i++) {
		if (buffer[i] == ':') { strcpy(key,buffer+i+2); break; }
	}
	close(sockfd);
	int k = 0;

	for (i=0; i<strlen(allchar); i++) {
		sleep(2);
		sockfd = socket(AF_INET, SOCK_STREAM, 0);

		if (sockfd < 0) {
			perror("Error opening socket");
			exit(-1);
		}

		server = gethostbyname(argv[1]);

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

		bzero(buffer,256);
		n = read(sockfd, buffer, 255);
		sprintf(payload,"givechar %c %s\n",allchar[i], key);
		write(sockfd,payload,strlen(payload));
		bzero(buffer,256);
		n = read(sockfd, buffer, 255);
		if (buffer[0] == 's' && buffer[1] == 'u') {continue;}
		char *tokens = strtok(buffer,",");
		while (tokens != NULL) {
			k++;
			j = atoi(tokens);
			flag[j] = allchar[i];
			tokens = strtok(NULL, ",");
		}
		close(sockfd);

	}
	flag[k] = '\0';
	printf("%s\n",flag);
	return(0);

}
