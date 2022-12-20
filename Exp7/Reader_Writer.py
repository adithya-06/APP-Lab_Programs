#Reader Writer

import threading as thread
import random

global x
x=0
lock=thread.Lock()

def Reader():
    global x
    print("Reader is reading")
    lock.acquire()
    print("Shared Data:",x)
    lock.release()
    print()

def Writer():
    global x
    print("Writer is writing")
    lock.acquire()
    x+=1
    print("Writer is Releasing the lock",x)
    lock.release()
    print()

if __name__=="__main__":
    for i in range(10):
        randomNumber=random.randint(0,100)
        if randomNumber>50:
            t1=thread.Thread(target=Reader)
            t1.start()
        else:
            t2=thread.Thread(target=Writer)
            t2.start()

t1.join()
t2.join()

print(x)
