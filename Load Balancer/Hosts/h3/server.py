from socket import *

serverName= "10.0.0.3"
serverPort = 8000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    print("Received from :", addr)
    sentence = connectionSocket.recv(1024).decode() 
    l = "Hi " + sentence + " from " + serverName
    connectionSocket.send(l.encode())
connectionSocket.close()
