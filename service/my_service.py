__author__ = 'Nicholas Rodofile'

# Dictionary of keys and elements of data
dictionary = {
    "RAM": "A type of computer memory that can be accessed randomly; that is, any byte of memory can be "
           + "accessed without touching the preceding bytes.",
    "CPU": "is the abbreviation for central processing unit. Sometimes referred to simply as the central processor, "
           + "but more commonly called processor, the CPU is the brains of the computer where most "
           + "calculations take place.",
    "kernel": "The most basic level or core of an operating system, responsible for "
              + "Resource allocation, file management, and security.",
    "operating system": "the low-level software that supports a computer's basic functions, such as scheduling tasks "
                        + "and controlling peripherals.",
    "software": "The programs and other operating information used by a computer.",
    "hardware": "The machines, wiring, and other physical components of a computer or other electronic system.",
    "TCP/IP": "Transmission Control Protocol/Internet Protocol (TCP/IP) is the language a "
              + "computer uses to access the Internet. It consists of a suite of protocols designed "
              + "to establish a network of networks to provide a host with access to the Internet.",
}

# A service that checks if "data" is a key in the dictionary
# if the data is a key, then it will return the data that is held by the key
# if the key is not found then return the string "Not found"


def my_service(data):
    if data in dictionary:
        return dictionary[data] + "\n > "
    return "Not found! \n > "

