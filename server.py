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
 
conn={}
addr={}
while 1:
    conn[0], addr[0] = s.accept()
    conn[1], addr[1] = s.accept()
   # print ('Connected with ' + addr[0] + ':' + str(addr[1]))
while True:
    
    data = conn[0].recv(1024)
    if not data:
        print ('there is no more message')
        break
    else:
        print ('sending data to other ')
        reply= +data
        print (reply)
        
        conn[0].sendall(reply)

    data1 = conn[1].recv(1024)
    if not data1:
        print ('there is no more message')
        break
    else:
        print ('sending data to other ')
        reply1= +data1
        print (reply1)
        
        conn[1].sendall(reply1)
        
conn[0].close()
conn[1].close()
s.close()

