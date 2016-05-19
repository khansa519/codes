
import socket
import sys
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
HOST = socket.gethostname()
PORT = 5812                # Reserve a port for your service.

s.connect((HOST, PORT))
while True:
    s.sendall(raw_input(data))
    print ('message is being sending')

    received = str(s.recv(1024))  
    print ('received : ' , received)
s.close                     # Close the socket when done
