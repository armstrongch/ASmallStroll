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
        print('listening')
        self.server.listen(5)

    def set_conn(self):
        print('accepting')
        self.conn, addr = self.server.accept()

    def receive_message(self):
        print('receiving')
        client_status = self.conn.recv(1000).decode()
        self.client_status_string = client_status
        print('sending')
        self.conn.send(self.server_status_string.encode())
        print('done')

