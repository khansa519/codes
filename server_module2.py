
'''
    Simple socket server using threads
'''

import socket
import sys
from thread import *

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5812  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# Start listening on socket
s.listen(2)
print 'Socket now listening'
j=0
i=0
c=[]
a = []
arr = ['client1', 'client2']
# Function for handling connections. This will be used to create threads
def clientthread (conn):
    # Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n')  # send only takes string
    for j in range(i-1):
        conn.sendall('connect to' + c[j])

       # infinite loop so that function do not terminate and thread do not end.
        while True:
            data = conn.recv(1024)
            if conn == a[0]:
                conn = a[1]
                print str(arr[0]) + ": " + data
                conn.sendall(data)
                conn = a[0]

            elif conn == a[1]:
                conn = a[0]
                print str(arr[1]) + ": " + data
                conn.sendall(data)
                conn = a[1]

            if not data:
                break
        # came out of loop
        conn.close()

i = 0
# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    b = [addr]
    b.append(addr[1])
    a.append(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (conn,))
    i= i+ 1

s.close()
