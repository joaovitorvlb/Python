#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import thread

def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024) 
        if msg:
            print addr[0], ' >> ', msg
            #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
            clientsocket.send(msg) 
    clientsocket.close()

s = socket.socket()         # Create a socket object

host = socket.gethostname() # Get local machine name
port = 500                  # Reserve a port for your service.

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.
   thread.start_new_thread(on_new_client,(c,addr))
s.close()
