#server
import socket
import time
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 9994
serversocket.bind((host, port))
serversocket.listen(5)
while True:
 clientsocket,addr = serversocket.accept()
 print("Got a connection from %s" % str(addr))
 currentTime = time.ctime(time.time()) + "\r\n"
 clientsocket.send(currentTime.encode('ascii'))
 clientsocket.close()

#client
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 9994
s.connect((host, port))
tm = s.recv(1024)
s.close()
print("The time got from the server is %s" % tm.decode('ascii'))
