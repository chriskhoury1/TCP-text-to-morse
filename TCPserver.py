from socket import *
class TCPserver:
    def __init__(self, port=16000):
        self.port = port

    def runServer(self):
        morseMsg = 1  # set morseMsg to 1 before receiving any signal
        serverSocket = socket(AF_INET, SOCK_STREAM)  # create a socket with second parameter SOCK_STREAM (unlike SOCK_DGRAM in UDP)
        serverSocket.bind(('Chris', self.port))  # binding the server to a port number
        serverSocket.listen(1)  # the server waits for incoming connections
        print("The server is ready to receive")
        while 1:
            (connectionSocket, addr) = serverSocket.accept()  # when the server recives a connection request, it accepts it
            print("Connection established with ", addr)  # prints the address of which user the server established the connection with
            if morseMsg == 1:
                morseMsg = connectionSocket.recv(1024)  # if there is no prior connection (ie no str value for morseMsg) then the server must receive the message)
            else:     # ie if morse message has an actual string value, it should send it
                connectionSocket.send(morseMsg)  # use send function (only in TCP) to send the string morseMsg to the other client
                morseMsg = 1  # after sending, the msg must be reset to 1 so that there are no errors and duplicates
            connectionSocket.close()  # closing the connection socket


server = TCPserver()
server.runServer()
