import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print(GPIO.input(4))

loops = 100

for i in range(loops):
    time.sleep(1)
    
    print("INPUT 4:  " + str(GPIO.input(4)))
    print("Only " + str(loops - i) + " left.")
    print("")
    

        

##GPIO.add_event_detect(4, GPIO.RISING)
##
##def my_callback(event):
##    print('PUSHED!')
##    print(GPIO.input(4))
##
##GPIO.add_event_callback(4, my_callback)

