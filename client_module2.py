import socket
import sys
from thread import *

s = socket.socket()
HOST = socket.gethostname()
PORT = 5812  # Reserve a port for your service.


def cthread():
    while True:
        received = s.recv(1024)
        print  received

s.connect((HOST, PORT))
start_new_thread(cthread, ())

while True:
    msg = raw_input()
    s.sendall(msg)
   # print ('message sent\n')


s.close  # Close the socket when done
