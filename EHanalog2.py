import signal
import explorerhat
import time

loops = 100

for i in range(loops):
    time.sleep(1)
    
    print("INPUT 1:  " + str(explorerhat.analog.one.read()))
    print("Only " + str(loops - i) + " left.")
    print("")
    


