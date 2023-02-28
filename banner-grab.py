# This script will help to grab banner of a service. Also helps to grab its version.
import socket
print("Usage: python3 bind_connection.py")
print("Prompt 1-> Enter Remote IP Address: 192.168.122.141")
print("Prompt 2-> Enter Remote Port Number: 8080")

print("\n")

# give target IP and port number
ip=input("Enter Target IP Address here: ")
port=int(input("Enter Target Port Number here: "))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
message=s.recv(2048)
print(message)

print("Mission Successful!")
