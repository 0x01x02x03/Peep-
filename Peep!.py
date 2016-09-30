#Produced by Dator-Coding
#Produced on 30/09/2016
import os
import socket
import sys #Currently not in use
import subprocess
selection = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Peep!')
print('     Dator-Coding accepts no liability for any damage cause by this script')
print('     Email DatorCoding@gmail.com for any questions')
ACCEPT = input('Continue running script? Y/N: ')
if not ACCEPT ==('Y'):  #FailSafe
    print('exiting script')
    exit()
def SSHscan():
    IP = input('Enter IP to scan: ')
    connect = sock.connect_ex((IP, 22)) #Non-Passive contact
    if connect ==(0):
        sock.close()
        print(IP,' is available for SSH connection')
        os.system('pause')
    sock.close()
    if connect ==(10064):
        print(IP,' is not available for SSH connections')
        os.system('pause')
    if not connect ==(0) or connect ==(10064):
        print(IP,' does not appear to be open for SSH connections')
        os.system('pause')
    body()
def TELNETscan():
    IP = input('Enter IP to scan: ')
    connect = sock.connect_ex((IP, 25)) #Non-Passive contact
    if connect ==(0):
        sock.close()
        print(IP,' is available for Telnet connection')
        os.system('pause')
    sock.close()
    if connect ==(10064):
        print(IP,' is not available for Telnet connections')
        os.system('pause')
    else:
        print(IP,' does not appear to be open for Telnet connections')
        os.system('pause')
    body()
def body():
    print('Which script would you like to run?')
    print('     1: SSH checker')
    print('     2: Telnet checker')
    selection = input('Enter a choice: ')
    if selection == '1':
        SSHscan()
    if selection == '2':
        TELNETscan()
    if not selection =='1' or selection =='2':
        print('Please choose from the list of values')
        body() 
body()
