#include <stdio.h>
#include <netdb.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	int sockfd=0, n;	
	struct sockaddr_in serv_addr;
	struct hostent *server;
	char buffer[4096], payload[128];
	char *tokens, hostname[256];
	int i=0, portno;

	if (argc<2) {
		fprintf(stderr, "usage: %s URL\n", argv[0]);
		exit(-1);
	}
	sockfd = socket(AF_INET, SOCK_STREAM, 0);

	if (sockfd < 0) {
		perror("Error opening socket");
		exit(-1);
	} 

	strcpy(hostname, "temp");

	tokens = strtok(argv[1], "://");
	while (tokens != NULL) {
		if (strcmp(tokens, "http")) {
			if (i==1) { strcpy(hostname, tokens); }
			else if (i==2) { portno = atoi(tokens); }
		}
		i++;
		tokens = strtok(NULL,"://");
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

	bzero(buffer,4096);
	sprintf(payload,"GET / HTTP/1.1\r\n\r\n");
	write(sockfd,payload,strlen(payload));
	bzero(buffer,4095);
	n = read(sockfd, buffer, 4095);
	close(sockfd);

	for (i=0; i<strlen(buffer); i++) {
			if (buffer[i] == '<') {
				tokens = buffer+i;
				break;
			}
	}

	printf("%s\n",tokens);
	return(0);


}
