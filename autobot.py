import subprocess
from threading import Thread

# Run another script and provide input
port = [123,725,1928,5263]
player=["Powerpoint_ranger", "starbucks wars", "Harry Plotter",'autobot']
matricules=[1234,2341,1565,2563]

def launch(i):
    
    launch = subprocess.run(
        ['python', 'PI2CChampionship_BOT/communication.py', str(port[i]), player[i], "LOCALHOST", "3000", str(matricules[i])],
        text=False
    )

for i in range(4):
    thread = Thread(target=launch, args=(i,))
    thread.start()
    
    

