A. Steps to create the socket program on word transfer from client to server with Ubuntu on VM as the server:
1. While creating the server file on Ubuntu(SERVER):
	a. First created a socket
	b. Took an arbitary port number greater than 1023(in this case it is 1024) for the transfer of infromation
	c. Binded the ports of the client and server
	d. Sent a message to the client
	e. Ended the connection
4. While creating the client file on Windows(CLIENT):
	a. First created a socket
	b. Took the same port number as in the server(in this case 1024)
	c. Looked for the ip address in the Ubuntu on VM
	d. Entered the ip address for connecting with the server
	e. Received the message from the server
	f. Displayed it to the client
	g. Ended the connection
