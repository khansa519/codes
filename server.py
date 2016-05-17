'''
    Simple socket server using threads
'''
 
import socket
import sys
 
HOST = ''  
PORT = 5812 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print ('Socket bind complete')
 
s.listen(2)
print ('Socket now listening')
 

while 1:
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
while True:
    data = conn.recv(1024)
    print ('received "/s" ' % data)
    if not data:
        print ('there is no more message')
        break
    else
        print ('sending data to other ')
        conn.sendall(data)
conn.close()    
s.close()
