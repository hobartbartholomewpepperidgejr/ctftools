from pynput import keyboard
from time import time, sleep

latest=[0,0]

aup=True
apress=0
dup=True
dpress=0
ingame=False
fromstart=0
controls=eval(open("controls.txt", "r").read())

def on_press(key):
    global aup, dup, apress, dpress, fromstart
    presstime=time()-fromstart
    try:
        if key.char==controls["L"] and aup==True:
            aup=False
            apress=presstime
        if key.char==controls["R"] and dup==True:
            dup=False
            dpress=presstime
    except:
        pass

def on_release(key):
    global aup, dup, apress, dpress, fromstart, ingame
    unpresstime=time()-fromstart
    try:
        nkey=key.char
    except:
        nkey=str(key)[4:]
    try:
        if nkey==controls["J"] and unpresstime>=200 and ingame==False:
            fromstart=time()-(unpresstime-200)*0.025
            ingame=False
            aup=True
            apress=0
            dup=True
            dpress=0
        if nkey==controls["L"] and aup==False:
            latest[0]=int((unpresstime-apress)/0.025)
            aup=True
        if nkey==controls["R"]  and dup==False:
            latest[1]=int((unpresstime-dpress)/0.025)
            dup=True
    except:
        pass
    

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    sleep(0.0125)
    print("\033[;H\033[J", end="")
    if latest[0]==3:
        print("\033[1;42mL", str(latest[0])+"\033[0m")
    else:
        print("\033[1;41mL", str(latest[0])+"\033[0m")

    if latest[1]==3:
        print("\033[1;42mR", str(latest[1])+"\033[0m")
    else:
        print("\033[1;41mR", str(latest[1])+"\033[0m")

    if latest[0]!=latest[1]:
        print("\n\033[1;41mdesynchronized!\033[0m", "\ntry tapping lighter/harder until the values match and turn green!")