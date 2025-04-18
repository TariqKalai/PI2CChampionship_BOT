import socket
import threading
import json
import sys

class Client():

    def __init__(self):
        
        self.s2 = socket.socket()
        client_port = int(input("entrez le numéro du port du serveur : "))
        clientname = input("pseudo : ")
        self.myadress = (('0.0.0.0',client_port))
        self.s2.bind((self.myadress))

        self.s1 = socket.socket()
        self.s1.bind(("0.0.0.0", 0))


        server_IP = input("entrez le numero du serbeur : ")
        server_port = int(input("entrez le numéro du port du serveur : "))
        self.server_adress = ((server_IP, server_port))
        

        self.inscription = False


        
        Txet = {
                    "request": "subscribe",
                    "port": client_port,
                    "name": clientname,
                    "matricules": ["12345", "67890"]}
        print (Txet)
        
        intro = json.dumps(Txet)
        message= intro.encode()
        totalsent = 0
        while totalsent < len(message) : 
            self.s1.connect(self.server_adress)
            send = self.s1.sendto(message[totalsent:], self.server_adress)
            totalsent += send


    
    def _listen(self):

        while self.running == True :
            if self.inscription is False:

                try:

                    data, address = self.s1.recvfrom(1024)

                    info = json.loads(data.decode())

                    print(f" {address[0]} : {info}")

                    if info["response"] == "ok":
                        

                        self.inscription = True
                        
                except json.JSONDecodeError :
                    pass
            
            if self.inscription is True:

                try:
                    
                    self.s2.listen()
                    self.s3_client , self.s3_address = self.s2.accept()

                    data = self.s3_client.recv(1024)

                    info = json.loads(data.decode())

                    print(f" {address[0]} : {info}")

                    if info["request"] == "ping":

                        txet = {"response": "pong"}
                        message= json.dumps(txet).encode()                      

                        self.s3_client.sendall(message)



                except json.JSONDecodeError :

                    print('oohh')

                    pass

            



    
    def _send(self, data):

        if self.address is not None:

            message = data.encode()

            totalsent = 0
            
            while totalsent < len(message) : 
                send = self.s.sendto(message[totalsent:], self.address)
                totalsent += send
                
    def run(self):

        self.running = True
        self.address = None

        threading.Thread(target= self._listen).start()

        handlers = {

            "/send" : self._send,
        }

        
        while self.running : 
                line = sys.stdin.readline().rstrip()+' '
                command = line [:line.index(' ')]
                param = line[line.index(' ')+1:].rstrip()
                if command in handlers : 
                    handlers[command]() if param == '' else handlers[command](param)
                else : 
                    print("unkown command")
                    




Client().run()