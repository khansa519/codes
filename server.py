'''
    Simple socket server using threads
'''

import socket
import sys
from thread import *
global conn
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
conn = [0, 0]

# Function for handling connections. This will be used to create threads
def clientthread(i):
    # Sending message to connected client
    #conn[i].send('Welcome to the server. Type something and hit enter\n')  # send only takes string

    # infinite loop so that function do not terminate and thread do not end.
    #for i in range (0,3):
        #conn[i].send('Welcome to the server. Type something and hit enter\n')
        while True:
            if (conn[i]):
                data = conn[i + 1].recv(1024)
                print ('sending data to other ')
                reply = 'client1:' + data
                print (reply)
                if not data:
                    print ('there is no more message')
                    break


                    conn[i + 1].sendall(reply)
            elif conn[i + 1]:

                data1 = conn[i].recv(1024)
                print ('sending data to other ')
                reply1 = 'client2:' + data1
                print (reply1)
                if not data1:
                    print ('there is no more message')
                    break

                    conn[i].sendall(reply1)
        conn[i].close()
        #conn[1].close()


# now keep talking with the client
for i in range(0, 3):
    # wait to accept a connection - blocking call
    conn[i], addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    conn[i].send('Welcome to the server. Type something and hit enter\n')

    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (i,))

s.close()
