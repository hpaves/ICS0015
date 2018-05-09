import socket
import threading
import sys
import tkinter
from tkinter import *
from tkinter import messagebox, scrolledtext

# I'm relying on a lot of example code from the lectures by Tauseef Ahmed

# Define main window
root = Tk()
root.title("chat.py gui")

# Create a frame for the text area
# textFrame = Frame(root)
# textFrame.pack()
# sframe = Frame(textFrame)
# sframe.pack(anchor='w')

# Use ScrolledText widget
# scr = scrolledtext.ScrolledText(root, wrap = tkinter.WORD)
# scr.pack()

# followed the howCode simple python chat server tutorial https://www.youtube.com/watch?v=D0SLpD7JvZI

port = 10001

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # using ipv4 and tcp
    connections = []
    def __init__(self): # constructor
        self.sock.bind(("0.0.0.0", port)) # bind socket to an address:port
        self.sock.listen(5)
        print("Server running...")

    def handler(self, c, a):
        while True:
            data = c.recv(1024) # when we receive data on the connection (data size)
            for connection in self.connections:
                if connection == c:
                    pass
                    print(str(data, "utf-8"))
                else:
                    connection.send(data)
                    print(str(data, "utf-8"))
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

# class Client:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     def sendMsg(self):
#         while True:
#             self.sock.send(bytes(input(""), "utf-8"))

#     def __init__(self, address):
#         self.sock.connect((address, port))

#         # we put sendMsg to run in the background
#         iThread = threading.Thread(target=self.sendMsg) # new thread for sending data
#         iThread.daemon = True
#         iThread.start()

#         while True:
#             data = self.sock.recv(1024)
#             if not data: # when client is disconneted
#                 break
#             print(str(data, "utf-8"))

class App(threading.Thread): # https://github.com/praven0894/Chat-with-tkinter-and-socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), "utf-8"))

    def __init__(self, address):
        threading.Thread.__init__(self)
        self.sock.connect((address, port))
        iThread = threading.Thread(target=self.Send) # new thread for sending data
        iThread.daemon = True
        iThread.start()

        frame = Frame()
        frame.pack()
        self.gettext = scrolledtext.ScrolledText(frame, height=30,width=80)
        self.gettext.pack()
        self.gettext.configure(state='disabled')
        sframe = Frame(frame)
        sframe.pack(anchor='w')
        self.sendtext = Entry(sframe,width=80)
        self.sendtext.focus_set()
        self.sendtext.bind(sequence="<Return>", func=self.Send)
        self.sendtext.pack(side=LEFT)

    def Send(self, args):
        self.gettext.configure(state='normal')
        text = self.sendtext.get()
        self.sock.send(bytes(text, "utf-8")) # send to server (broken)
        self.gettext.insert(END,'%s\n'%text) # print to chat
        print(text) # print to console for testing
        print(args)
        self.sendtext.delete(0,END)
        self.sendtext.focus_set()
        self.gettext.configure(state='disabled')
        self.gettext.see(END)

    def run(self):
        Receive(self.sock, self.gettext)

class Receive():
  def __init__(self, sock, gettext):
    self.sock = sock
    self.gettext = gettext
    while 1:
      try:
        text = self.sock.recv(1024)
        if not text: 
            break
        self.gettext.configure(state='normal')
        self.gettext.insert(END,'%s\n'%text)
        self.gettext.configure(state='disabled')
        self.gettext.see(END)
      except:
        break


if (len(sys.argv) > 1): # if more than one command line argument
    app = App(sys.argv[1]).start()
    loop_active = True # https://gordonlesti.com/use-tkinter-without-mainloop/
    while loop_active:
        root.update()
        # client = Client(sys.argv[1]) # connect  to second variable
else:
    server = Server()
    server.run()
