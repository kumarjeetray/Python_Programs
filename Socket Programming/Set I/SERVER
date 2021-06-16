import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5)
while True:
    clt_soc, clt_add = s.accept()
    print(f"Connection to {clt_add} established")
    clt_soc.send(bytes("Socket Programming", "utf-8"))
