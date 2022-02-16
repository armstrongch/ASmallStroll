import socket

class server:

    server = None
    hostname = None
    port = None
    conn = None
    server_status_string = "server status"
    client_status_string = None

    def open_socket(self):
        self.hostname = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.hostname, 0))
        self.port = self.server.getsockname()[1]
        self.server.listen(5)

    def set_conn(self):
        self.conn, addr = self.server.accept()

    def receive_message(self):
        new_client_status = self.conn.recv(1000).decode()
        self.conn.send(self.server_status_string.encode())
        if new_client_status:
           self.client_status_string = new_client_status
        

