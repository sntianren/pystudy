#!/usr/bin/env python
# Filename: tsTserv.py

from socket import socket, AF_INET, SOCK_STREAM
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

try:
    while True:
        print 'waiting for connectin...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connected from: ', addr

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                tcpCliSock.close()
                break
            tcpCliSock.send('[%s] %s' % (ctime(), data))
except:
    print '...srv is shutting down...'
    tcpSerSock.close()
