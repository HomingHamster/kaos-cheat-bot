import csv
import socket

HOST="127.0.0.1"
PORT=6667
readbuffer=""
diction = {}
inplay = True

reader = csv.reader(open("kaos.db"), [], delimiter="*")
for line in reader:
    diction[line[0]] = line[1:]

print diction

cb=socket.socket( )
cb.connect((HOST, PORT))
cb.send("NICK cheatbot\r\n" )
cb.send("USER cheatbot cheatbot bla :CHEATBOT\r\n" )
cb.send("JOIN #games\r\n")

while 1:
    data = cb.recv ( 4096 )
    
    if data.find ( 'PING' ) != -1:
        cb.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
        
    if data.find ( '!cheatbot stop' ) != -1:
        inplay = False
        cb.send("PRIVMSG #games : NOT PLAYING\r\n")
        
    if data.find ( '!cheatbot start' ) != -1:
        inplay = True
        cb.send("PRIVMSG #games : PLAYING\r\n")
        

    if inplay == True:
        data = data.lower()
        for i in diction:
            if data.find( i.lower() ) != -1:
                for item in diction[i]:
                    cb.send("PRIVMSG #games :" + item + "\r\n")
                    print item
                    
        
    print data
