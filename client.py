
import socket
imp sys
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
HOST = socket.gethostname()
PORT = 5812                # Reserve a port for your service.

s.connect((HOST, PORT))
try:
    s.sendall(bytes(data))
    print ('message is being sending')

    received = str(s.receive(1024))  
    print ('received "/s" ' % data)
s.close                     # Close the socket when done
