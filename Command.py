import os
import platform


class get_info():

    def ip():
        if platform.system() == 'Windows':
            msg = os.popen('ipconfig').read()
            print(msg)
        else:
            msg = os.popen('ip addr show').read()
            print(msg)
    def systeme():
        print(platform.uname())
    def platforme():
        print(platform.platform().replace('-', ' '))
    def pid():
        print("Process ID :", os.getpid())
    def rshell():
        print(platform.system(), 'System')
        print('Shell mode, type "noshell" to quit')
        commande = input()
        condi = True
        while commande != 'noshell' :
            if commande == 'assist' :
                print ('Shell mode, type "noshell" to quit')
            else :
                msg = os.popen(commande).read()
                #print('-')
                print(msg)
            commande = input()
        print ('Exiting Shell mode')


condi = True
while condi :
    msg = input()
    if msg == 'sysinfo':
        get_info.systeme()
    elif msg == 'ip':
        get_info.ip()
    elif msg == 'plateform':
        get_info.platforme()
    elif msg == 'pid':
        get_info.pid()
    elif msg == 'quit':
        condi = False
        print ('Exiting program')
    elif msg == 'shell':
        get_info.rshell()
    else :
        print('Unknown command')
