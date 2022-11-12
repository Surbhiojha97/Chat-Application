# Chat-Application
                                                              Socket programming
Sockets can be thought of as endpoints in a communication channel that is bi-directional and establishes communication between a server and one or more clients. 
Here, we set up a socket on each end and allow a client to interact with other clients via the server. The socket on the server side associates itself with some 
hardware port on the server-side. Any client that has a socket associated with the same port can communicate with the server socket. 

The server-side script will attempt to establish a socket and bind it to an IP address and port specified by the user. The script will then stay open and receive
connection requests.

The client-side script will simply attempt to access the server socket created at the specified IP address and port. Once it connects, it will continuously check 
as to whether the input comes from the server or from the client, and accordingly redirects output. If the input is from the server, it displays the message on the 
terminal. If the input is from the user, it sends the message that the user enters to the server for it to be broadcasted to other users.
