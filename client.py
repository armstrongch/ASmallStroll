import socket

class client:

    client = None
    hostname = None
    port = None
    server_status_string = None
    client_status_string = "client status"

    def open_socket(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.hostname, int(self.port)))

    def send_status(self):
        self.client.send(self.client_status_string.encode())
        new_server_status = self.client.recv(1000).decode()
        if new_server_status:
            self.server_status_string = new_server_status
