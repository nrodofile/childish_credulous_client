__author__ = 'Nicholas Rodofile'

import socket

"""
More information can be found here:
https://docs.python.org/2/library/socketserver.html
"""

class Client():
    def __init__(self, port, ip_address):
        self.port = port
        self.ip_address = ip_address

        # Create a socket (SOCK_STREAM means a TCP socket)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """
    Call this function to connect the client to the server
    """
    def connect(self):
        try:
            # Connect to server and send data
            self.sock.connect((self.ip_address, self.port))
        except socket.error as msg:
            print "Error", msg
            quit()

    """
    Pass your through this function to send it to the server
    """
    def send(self, data):
        try:
            # send data
            self.sock.sendall(data)

            # Receive data from the server
            received = self.sock.recv(1024)
            return received

        except socket.error as msg:
            print "Error", msg

    """
    Close the connection to the server
    """
    def close(self):
        #Close Connection
        self.sock.close()
