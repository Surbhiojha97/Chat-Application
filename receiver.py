import socket
import os
r_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 12534
r_socket.connect((ip,port))
print(f"Got connected with {ip} : {port}")

while True:
    rmsg = input("\n\nReceiver--> ") 
    #r_socket.send(rmsg.encode())
    if rmsg.lower().strip()=="done":
        print("Thank you for sharing!!!")
        r_socket.close()
        break
    else:
        r_socket.send(rmsg.encode())
        break
    smsg = r_socket.recv(1024)
    if smsg.decode().lower().strip()=="decline":
        print("No such file to transfer!!!!")
        r_socket.close()
        break
    elif smsg.decode().lower().strip()=="accepted":
        file = open("d:\Files..",'wb')
        while smsg:
            r_socket.write(filedata)
            print("File is downloaded!!")
        file.close()
        #rmsg = input("\n\nReceiver--> ") 
        #r_socket.send(rmsg.encode())
        #if rmsg.lower().strip()=="done":
            #print("Thank you for sharing!!!")
            #r_socket.close()
            #break
    else:
        r_socket.send(rmsg)
