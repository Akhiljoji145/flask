import socket
from tkinter import * 
root=Tk()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.connect((HOST_NAME,PORT))
while True:
	msg=s.recv(100)
	print("Server:"+msg.decode("utf-8"))
	cli_to_ser=input("Client:")
	s.send(bytes(cli_to_ser,'utf-8'))