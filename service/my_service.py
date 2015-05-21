__author__ = 'Nicholas Rodofile'

import hashlib

def my_service(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

