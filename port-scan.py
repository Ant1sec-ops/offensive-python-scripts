import socket 
ip = input("Enter Target IP address: ")
print('Hold on. It may take some time!')
for i in range(1,1024):

    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        

        port = i

        s.connect((ip,port))

        print(str(port)+" is opened")
        s.close()

    except:
        
        s.close()
