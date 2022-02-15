import socket

class server:

    server = None
    hostname = None
    port = None

    def open_socket(self):
        self.hostname = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.hostname, 0))
        self.port = self.server.getsockname()[1]
        self.server.listen(1)
        

    def listen(self):
        conn, addr = self.server.accept()
        print("listening")
        client_message = conn.recv(1000)
        if client_message:
            server_response = "server response"
            conn.send(server_response.encode())
            return client_message.decode()

            
            
#s = server()
#s.open_socket()
#print()
#while True:
    #client_message = s.listen()
    #print(client_message)
