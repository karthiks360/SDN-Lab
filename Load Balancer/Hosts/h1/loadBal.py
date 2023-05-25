import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
sock.bind(("10.0.0.1", 8080))

# Listen for incoming connections
sock.listen(5)

i = 0
n = 3
arr = ["10.0.0.2","10.0.0.3", "10.0.0.4"]

while i<n:
    # Accept an incoming connection
    client_sock, client_addr = sock.accept()
    print("Received connection from", client_addr)

    # Choose a server to forward the connection to
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_sock.connect((arr[i], 8000))
    print("Req sent to", arr[i])
    i+=1
    if i==n:
        i = 0
    server_sock.sendall(client_sock.recv(1024))
    client_sock.sendall(server_sock.recv(1024))
    client_sock.close()
        
    server_sock.close()
