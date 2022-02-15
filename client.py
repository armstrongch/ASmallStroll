import socket

#create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server address/port
client.connect(('192.168.0.27', 62282))
print('opened connection')

#send message
client_message = "client message"
client.send(str.encode(client_message))

#receive response
server_response = client.recv(4096)
print(server_response.decode())

#close connection
client.close()
print('closed connection')
