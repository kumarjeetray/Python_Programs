Steps to create the socket program on word transfer from client to server with Ubuntu on VM as the server:
<br>
<b> While creating the server file on Ubuntu(SERVER):</b>
1. First created a socket.
2. Took an arbitary port number greater than 1023(in this case it is 1025) for the transfer of infromation.
3. Binded the ports of the client and server.
4. Sent a message to the client.
5. Ended the connection.

<b> While creating the client file on Windows(CLIENT):</b>
1. First created a socket.
2. Took the same port number as in the server(in this case 1025).
3. Looked for the ip address in the Ubuntu on VM.
4. Entered the ip address for connecting with the server.
5. Received the message from the server using loop.
6. Displayed it to the client.
7. Ended the connection.
