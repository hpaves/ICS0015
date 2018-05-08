import socket
import threading
import sys
import tkinter
from tkinter import *
from tkinter import messagebox, scrolledtext

# I'm relying on a lot of example code from the lectures by Tauseef Ahmed

# Define main window
root = Tk()
root.geometry("720x400")
root.title("chat.py gui")

# Create a frame for the text area
textFrame = Frame(root)
textFrame.pack()

# Use ScrolledText widget
scr = scrolledtext.ScrolledText(root, wrap = tkinter.WORD)
scr.pack(side = LEFT, fill = BOTH, expand = YES)

# followed the howCode simple python chat server tutorial https://www.youtube.com/watch?v=D0SLpD7JvZI

port = 10000

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # using ipv4 and tcp
    connections = []
    def __init__(self): # constructor
        self.sock.bind(("0.0.0.0", port)) # bind socket to an address:port
        self.sock.listen(1)
        print("Server running...")

    def handler(self, c, a):
        while True:
            data = c.recv(1024) # when we receive data on the connection (data size)
            for connection in self.connections:
                if connection == c:
                    pass
                else:
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
        self.sock.connect((address, port))

        # we put sendMsg to run in the background
        iThread = threading.Thread(target=self.sendMsg) # new thread for sending data
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data: # when client is disconneted
                break
            print(str(data, "utf-8"))

# class GUI(threading):
#     def __init__(self, tk_root):
#         self.root = tk_root
#         threading.Thread.__init__(self)
#         self.start()


if (len(sys.argv) > 1): # if more than one command line argument
    loop_active = True # https://gordonlesti.com/use-tkinter-without-mainloop/
    while loop_active:
        root.update()
        client = Client(sys.argv[1]) # connect  to second variable
else:
    server = Server()
    server.run()
