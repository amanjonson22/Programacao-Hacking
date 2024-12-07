import socket

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error:
    print("Erro durante a criação do socket")
    exit()


host = '' #127.0.0.1
port = 9999

tcp_socket.bind((host, port)) #listening to connections
tcp_socket.listen(1)

while True:
    c, addr = tcp_socket.accept()
    print('Connection from {}:{}'.format(addr[0], addr[1]))
    c.close()

tcp_socket.close() #fecha o server