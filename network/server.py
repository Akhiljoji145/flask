import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.bind((HOST_NAME,PORT))
s.listen(4)
client,address=s.accept()

while True:
	message=input("Server:")
	client.send(bytes(message,"utf-8"))
	cli_message=client.recv(100)
	print("Client:"+cli_message.decode('utf-8'))