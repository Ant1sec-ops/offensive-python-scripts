# create a two way communication channel. 
# use this scrtipt on target side and run netcat in kali: nc -nlvp 8080
# import socket and subprocess
import socket
import subprocess

print("Usage: python3 bind_connection.py")
print("Prompt 1-> Enter Remote IP Address: 192.168.122.141")
print("Prompt 2-> Enter Remote Port Number: 8080")

# allow User input and store in variables

ip = input("Enter Remote IP Address: ")
port = int(input("Enter Remote Port Number: "))

try:
    # Create a IPV4 socket here and store it in a variable called s
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # use connect function with defined variable and use given ip and port number
    s.connect((ip,port))
    # If successful and give a command promt as Connected$ 
    
    cmdlet = input("Conneted$ ")
    # Continue if its not equal to quit
    while cmdlet!='quit':
        
        #Send given command to remote host in encoded form
        s.send(cmdlet.encode())

        # Give 2048 byes that we want to receive. Note we can also use 1024
        result = s.recv(2048).decode()
        print(result)
        cmdlet = input("Connected$ ")
        
    s.close()
except:
    print("Oh No ..Session Terminated :(")
 
#EXAMPLE
 
#On Target side here we are connecting to kali and issuing hello command which will be reflect in kali
#└─$ python3 client.py
#Usage: python3 bind_connection.py
#Prompt 1-> Enter Remote IP Address: 192.168.122.141
#Prompt 2-> Enter Remote Port Number: 8080
#Enter Remote IP Address: 192.168.214.128
#Enter Remote Port Number: 8080
#Conneted$ Hello

 
#On Kali
# ┌──(kali㉿kali)-[~/Python-Tools-development]
#└─$ nc -nlvp 8080
#listening on [any] 8080 ...
#connect to [192.168.214.128] from (UNKNOWN) [192.168.214.131] 40908
#Hello 
