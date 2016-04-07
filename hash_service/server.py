__author__ = 'Nicholas Rodofile'

"""
More information can be found here:
https://docs.python.org/2/library/socketserver.html
"""

import threading
import SocketServer

# replace my_service with your service
from my_service import my_service

HOST = "172.19.1.114"   # Change this to your server's IP address
PORT = 20001


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

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    server = ThreadedTCPServer((HOST, PORT), MyTCPHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Starting Service..."
    print HOST, "Waiting for Client to connect to port", PORT
    print "Stop Server by pressing Ctrl-C"
    print "Server loop running in thread:", server_thread.name
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print "Server is Stopping!"
        server.shutdown()