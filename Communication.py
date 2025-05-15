import socket
import threading
import json
import sys
from sys import argv
from inputs import random_moves, tought_moves
from Algorithm import get_best_move

class Player():

    '''Player class made for the server Quarto available at https://github.com/qlurkin/PI2CChampionshipRunner to run you need to launch and write
    [your port][pseudo][IP][port server][matricule]'''

    def __init__(self):
        
        #Definition of all the argv variables
        player_port = int(argv[1])
        pseudo = argv[2]
        server_IP = argv[3]
        server_port = int(argv[4])
        matricules = argv[5]
        self.methode = argv[6]

        
        #Binding IPs and specific port to player
        self.s2 = socket.socket()
        self.s2.bind(('0.0.0.0',player_port))

        #Binding IPs and wichever port to the inscription socket s1
        self.s1 = socket.socket()
        self.s1.bind(("0.0.0.0", 0))


        self.server_adress = ((server_IP, server_port))
        
        
        self.inscription = False
        

        #Sending the subsciption request to the quarto client
        SUB_text = {
                    "request": "subscribe",
                    "port": player_port,
                    "name": pseudo,
                    "matricules": [matricules]
                    }
        
        message= json.dumps(SUB_text).encode()
        
        totalsent = 0
        #loop to ensure that all the bytes are sent , This will be replaced by sendall() from now on
        while totalsent < len(message) : 
            self.s1.connect(self.server_adress)
            send = self.s1.sendto(message[totalsent:], self.server_adress)
            totalsent += send


    
    def _listen(self):

        while self.running == True :
            #Checks if the player is signed in or not, if not it will try again. It is made just fir the s1 socket
            if self.inscription is False:

                try:

                    data, address = self.s1.recvfrom(1024)

                    info = json.loads(data.decode())
                    print(info)


                    if info["response"] == "ok":
                        

                        self.inscription = True
                        
                except json.JSONDecodeError :
                    pass
            
            #If the player is subscriped it will launch this if statement wich is made for the s2 socket
            if self.inscription is True:

                try:
                    
                    self.s2.listen()
                    self.s3_client , self.s3_address = self.s2.accept()

                    data = self.s3_client.recv(1024)

                    info = json.loads(data.decode())
                    print( info)

                    #this section checks what kind of request the client sent us,
                    #  for a ping it will respond a pong and for a play it will play.... what else
                    if info["request"] == "ping":

                        txet = {"response": "pong"}
                        message= json.dumps(txet).encode()                      

                        self.s3_client.sendall(message)
                    
                    if info["request"] == "play" :

                        if self.methode == "Think":
                            move= get_best_move(info["state"])

                            txet =  {
                                       "response": "move",
                                       "move": {"pos" : move[0], "piece": move[1]},
                                       "message": "Think AI THINK"
                                    }

                        
                        elif self.methode == "random":
                            txet = random_moves(info)
                            
                        message= json.dumps(txet).encode()                      

                        self.s3_client.sendall(message)



                except json.JSONDecodeError :

                    print('oohh JSON ERROR')

                    pass

    def run(self):

        '''Runs the program and threads....... what else should it do???'''

        self.running = True
        self.address = None

        threading.Thread(target= self._listen).start()
                    




Player().run()