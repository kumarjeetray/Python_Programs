import pickle
import socket
a = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1030))
while True:
    complete_msg = b''
    rec_msg = True
    while True:
        mymsg = s.recv(16)
        if rec_msg:
            print(f"The message length:{mymsg[:a]}")
            x = int(mymsg[:a])
            rec_msg = False
        complete_msg += mymsg
        if len(complete_msg) - a  == x:
            print("Received the complete info")
            print(complete_msg[a:])
            m = pickle.loads(complete_msg[a:])
            print(m)
            rec_msg = True
            complete_msg = b''
print(complete_msg)