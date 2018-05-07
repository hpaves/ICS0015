import socket
import threading
import sys

# follwed the howCode simple python chat server tutorial https://www.youtube.com/watch?v=D0SLpD7JvZI

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # using ipv4 and tcp
    connections = []
    def __init__(self): # constructor
        self.sock.bind(("0.0.0.0", 10000)) # bind socket to an address:port
        self.sock.listen(1)

    def handler(self, c, a):
        while True:
            data = c.recv(1024) # when we receive data on the connection (data size)
            for connection in self.connections:
                connection.send(data)
            if not data: # when client is disconneted
                print(str(a[0]) + ":" + str(a[1]), "disconnected") # break tuple into two
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.sock.accept() # accept the connection
            cThread = threading.Thread(target=self.handler, args=(c, a)) # put connection on a thread to receive data
            cThread.daemon = True # program can exit when a thread is running
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ":" + str(a[1]), "connected")

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), "utf-8"))

    def __init__(self, address):
        self.sock.connect((address, 10000))

        # we put sendMsg to run in the background
        iThread = threading.Thread(target=self.sendMsg) # new thread for sending data
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data: # when client is disconneted
                break
            print(str(data, "utf-8"))

if (len(sys.argv) > 1): # if more than one command line argument
    client = Client(sys.argv[1]) # connect client to second variable
else:
    server = Server()
    server.run()