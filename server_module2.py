
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
j = 0
i = 0
d = []
a = []
k = 0
arr = ['client1', 'client2']

def clientthread (conn):
    conn.send('Welcome to the server. Type something and hit enter\n')  # send only takes string
    for j in range(i-1):
     conn.sendall('connect to : ' + b[j]+ '\n')
     a[j].sendall(' other clients are :' + str(com))

    conn.sendall(' to whom u want to chat ...?')
    ask = conn.recv(1024)
    d.append(conn)

    for k in range(i):
     if ask ==  b[k]:
         b[k] = a[k]
         d.append(a[k])
    while True:
                data = conn.recv(1024)
                if conn == d[0]:
                    conn = d[1]
                   # print str(arr[0]) + ": " + data
                    print data
                    conn.sendall(data)
                    conn = d[0]

                elif conn == d[1]:
                    conn = d[0]
                    #print str(arr[1]) + ": " + data
                    print data
                    conn.sendall(data)
                    conn = d[1]

                if not data:
                     break
        # came out of loop
    conn.close()
b =[]
i = 0
com=0
# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    a.append(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    b.append(str(addr[1]))
    com = addr[1]
    # start nb.append(str(addr[1]))ew thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (conn,))
    i= i+ 1

s.close()
