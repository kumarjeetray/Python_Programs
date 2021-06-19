import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2000))
s.listen(5)
name = ""
while True:
    clt_soc, clt_add = s.accept()
    print(f"Connection to {clt_add} established")
    name = clt_soc.recv(1024).decode()
    complete_msg = "You have successfully connected to the server:" + name
    clt_soc.send(bytes(complete_msg, "utf-8"))
    clt_soc.close()
