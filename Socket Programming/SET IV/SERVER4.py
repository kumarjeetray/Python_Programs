import socket
import pickle
a = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1030))
s.listen(5)
while True:
    clt_soc, clt_add = s.accept()
    print(f"Connection to {clt_add} established")
    my_dic = {1:"One", 2:"Two", 3:"Three", 4:"Four",5:"Five"}
    serial = pickle.dumps(my_dic)
    serial = bytes(f'{len(serial):<{a}}', "utf-8") + serial
    clt_soc.send(serial)
