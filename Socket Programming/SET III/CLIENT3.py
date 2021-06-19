import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2000))
complete_msg = ''
name_client = input("Enter your name:")
s.send(bytes(name_client, "utf-8"))
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    complete_msg += msg.decode("utf-8")
print(complete_msg)
