import socket
import time
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '192.168.1.118'
port = 900


try:
    server.bind((ip, port))
    server.listen(5)
    client_socket, address = server.accept()       #Receives connection parameters
    print  client_socket.recv(1024)                #Wait for some data and prints
except Exception as erro:
    print "Erro: " + str(erro)
    server.close()
