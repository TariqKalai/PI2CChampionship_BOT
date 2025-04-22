import subprocess
from threading import Thread
from time import sleep

# Run another script and provide input
port = [123,725,1928,5263,1671,8735,1631]
player=["Powerpoint Ranger", "Starbucks wars", "Harry Plotter",'Autobotter', 'Bytes10', 'The green array']
matricules=["456","2341","1565","2563","1383","28731"]

def launch(i):
    '''Launches the client program in a Local server to enable the use of multiple bots for testing and debugging purposes.'''

    
    subprocess.run(
        ['python', 'PI2CChampionship_BOT/communication.py', str(port[i]), player[i], "LOCALHOST", "3000", matricules[i]],
        text=True
    )

#Launches the program 4 times
for i in range(6):

    print([str(port[i]), player[i], "LOCALHOST", "3000", str(matricules[i])])

    thread = Thread(target=launch, args=(i,))
    thread.start()
    sleep(2)
    
    

