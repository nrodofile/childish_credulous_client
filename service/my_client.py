__author__ = 'Nicholas Rodofile'

from client import *
import time

port = 10222
ip_address = "10.0.3.2"
top_passwords = ['1234567', 'dragon', 'baseball', '1234',
                   '123456789', 'qwerty', '12345678', '12345',
                   'password', '123456']


if __name__ == "__main__":
    print "-------------------------------------------"
    print "# MD5 hash service: 2014 top 10 passwords #"
    print "==========================================="
    print " Password : MD5 Hash"
    print "==========================================="
    client = Client(port, ip_address)
    client.connect()
    for password in top_passwords:
        response = client.send(password)
        print password, ":", response

        #remove below to speed up requests
        time.sleep(.5)
    client.close()
