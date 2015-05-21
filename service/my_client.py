__author__ = 'Nicholas Rodofile'

from client import *
import time

port = 10222
ip_address = "10.0.3.2"
boy_names_2015 = ['Liam', 'Noah', 'Mason', 'Ethan',
                   'Logan', 'Lucas', 'Jackson', 'Jacob',
                   'Aiden', 'Oliver']

client = Client(port, ip_address)
client.connect()
for name in boy_names_2015:
    response = client.send(name)
    print response
    time.sleep(4)
client.close()
