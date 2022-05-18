#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
	print "Usage: VRFY.py <username>"
	sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket
connect = s.connect(('192.168.31.215', 25)) #connect to the server
banner = s.recv(1024)
print banner
s.send('VRFY ' + sys.argv[1] + '\r\n') #VRFY a user
result = s.recv(1024)
print result
s.close() #close the socket
