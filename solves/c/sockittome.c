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
	int i;
	char flag[4096];
	char payload[32];

	if (argc<3) {
		fprintf(stderr, "usage: %s hostname portnumber\n", argv[0]);
		exit(-1);
	}
	for (i=0; i<8192; i++) {

		portno = atoi(argv[2]);
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
		sprintf(payload,"givechar %d\n",i);
		write(sockfd,payload,strlen(payload));
		bzero(buffer,256);
		n = read(sockfd, buffer, 255);
		flag[i] = buffer[0];
		if (flag[i] == '}') { break; }
		close(sockfd);

	}
	flag[i+1] = '\0';
	printf("%s\n",flag);
	return(0);

}
