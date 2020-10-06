import socket
import os
os.system("pkg install cowsay")
os.system("apt-get install cowsay")
os.system("clear")
os.system("cowsay follow me:mr_mobin_dan | lolcat")
GREEN = '\033[92m'
print GREEN
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip =raw_input("ip:")
port =input("port:")

try:
        s.connect((ip,port))
        print("open port")
except:
         print("closr port")
