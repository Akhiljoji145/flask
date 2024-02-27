import socket
from tkinter import *
def send(listbox,entry):
	message=entry.get()
	listbox.insert('end',"Client:"+message)
	entry.delete(0,END)
	s.send(bytes(message, 'utf-8'))
def recieve(listbox):
	cli_message=s.recv(100)
	listbox.insert('end',"Server"+cli_message.decode('utf-8'))
root=Tk()
entry=Entry()
entry.pack(side=BOTTOM)
listbox=Listbox(root)
listbox.pack()
button=Button(root,text='Send',command=lambda :send(listbox,entry))
button.pack(side=BOTTOM)
rbutton=Button(root,text='Recieve',command=lambda :recieve(listbox))
rbutton.pack(side=BOTTOM)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.connect((HOST_NAME,PORT))
root.mainloop()