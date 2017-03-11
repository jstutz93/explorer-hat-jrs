import explorerhat
loy
##def ohai(channel, event):
##    print("Oy... I got a touch on button: {}".format(channel))

def lightsOff():
    explorerhat.light.yellow.off()
    explorerhat.light.blue.off()
    explorerhat.light.red.off()
    explorerhat.light.green.off()

def handle(channel, event):
    print("Got {} on {}".format(event,channel))
         
def changeLights(color):
    if color == 1:
        explorerhat.light.blue.on()
    if color == 2:
        explorerhat.light.yellow.on()
    if color == 3:
        explorerhat.light.red.on()
    if color == 4:
        explorerhat.light.green.on()
        
def oy(channel, event):
    lightsOff()
    changeLights(channel)
    print("Oy... I got a touch on button: {}".format(channel))
    

   
explorerhat.touch.one.pressed(oy)
explorerhat.touch.two.pressed(oy)
explorerhat.touch.three.pressed(oy)
explorerhat.touch.four.pressed(oy)

explorerhat.touch.held(handle)
