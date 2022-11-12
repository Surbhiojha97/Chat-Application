import socket
import os
s_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 12534
s_socket.bind((ip,port))
print("Sender waiting for request!!")
s_socket.listen()
r_socket,r_add = s_socket.accept()

while True:
    
    smsg = input("\n\n Sender--> ")
    r_socket.send(smsg.encode())
    if smsg.lower().strip()=="decline":
        print("No such file exists!!!")
        s_socket.close()
        r_socket.close()
        break
    else:
        rsmsg = r_socket.recv(1024)
        if rmsg.decode().lower().strip()=="done":
            print("Task completed!!!")
            s_socket.close()
            r_socket.close()
            break
        else:
        #d = os.walk("c:/Users/DELL/Desktop")
            path = rsmg
            with open("c:/Users/DELL/Desktop",'rb') as file:
                if os.path.exists():
                    filedata = file.read()
                    r_socket.send(filedata)
                    file.close()
            #if filename in d:
                #r_socket.send(filedata)
                else:
                    print("No such file !!")
                    s_socket.close()
                    r_socket.close()
                    break
