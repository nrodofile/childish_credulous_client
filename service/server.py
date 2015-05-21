__author__ = 'Nicholas Rodofile'

"""
More information can be found here:
https://docs.python.org/2/library/socketserver.html
"""

import SocketServer

# replace my_service with your service
from my_service import my_service

HOST = "10.0.3.2"   # Change this to your server's IP address
PORT = 10222


class MyTCPHandler(SocketServer.BaseRequestHandler):

    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        print "Connection with", self.client_address[0]
        while True:
            # self.request is the TCP socket connected to the client
            request = self.request.recv(1024).strip()

            #   if the client has closed connection break the while loop
            if not request:
                break

            #   Process Response using your own function
            response = my_service(request)

            #   Send back response
            self.request.sendall(response)

        print "Closing connection with", self.client_address[0]

if __name__ == "__main__":
    print "Starting Service..."
    print HOST, "Waiting for Client to connect to port", PORT
    print "Stop Server by pressing Ctrl-C"

    # Create the server, binding to localhost on port 10222
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print "Server is Stopping!"
        server.shutdown()