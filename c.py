import threading
# Echo client program
import socket
from time import gmtime, strftime
import time

HOST = '127.0.0.1'    # The remote host
PORT = 50007          # The same port as used by the server



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


# when we send data to the server, we are using a colon
# at the end of a sentence to mark the end of the current sentence
# later when the input comes back, we will then be breaking the input
# into individual parts using the colon : to separate the lines
nickname =''
def readInputThreaded(so):
    print " set your nickname"
    global nickname
    nick = raw_input()
    nickname = nick
    print nickname + "==> "
    while 1:


        text = raw_input()



        so.sendall(str(text))




t = threading.Thread(target=readInputThreaded, args = (s,))
t.start()



'''
Thread to read from the server
'''
def readFromServer(s):
    global nickname

    while 1:
        data = s.recv(100)
        #:User Name-"Message">
        if ":" in data:
            time = strftime("( %H:%M:%S) ", gmtime())
            Nmess= data.replace(':','')
            Nmess= Nmess.split('-')
            #global nickname
            nickname = Nmess[0]
            print(""+ str(time)+"" + nickname + "-> " + Nmess[1])
        elif "<getservertime>" in data:
            print "command in data.."
            formatted= strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            print(str(formatted))
        elif "<time>" in data:
            time= strftime(" %H:%M:%S +0000", gmtime())
            print(str(time))
        elif "<dates>" in data:
            dates=strftime("%a, %d %b %Y", gmtime())
            print(str(dates))
        #elif "<leave>" in data:
        #    s.close()
        elif "ping" in data:
            print("pong")
        elif "<change>" in data:# cant figure out how to change nickname
            print " set your new nickname"
            nick = raw_input()
            nickname = nick
        #    new = nickname
            print nickname + " want to change "
        #nickname = new
            #print("Old nickname = " + nickname + " new nickname = " + NewNick)






t = threading.Thread(target=readFromServer, args = (s,))
t.start()



#s.close()
