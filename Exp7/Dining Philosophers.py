#Dining Philosophers
import threading
import time
import random

class Philosopher(threading.Thread):
    running=True
    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight
    def run(self):
        while self.running:
            print("Philosopher %s is hungry." % self.index)
            self.dine()
    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
        while self.running:
            fork1.acquire()
            locked=fork2.acquire()
            if locked:
                break
            fork1.release()
            print('Philosopher %s swaps forks' % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()
        fork1.release()
        fork2.release()
    def dining(self):
        print('Philosopher %s is eating.' % self.index)
        time.sleep(random.randint(1, 5))
        print('Philosopher %s finishes eating and leaves to think.' % self.index)

def main():
    forks=[threading.Semaphore() for i in range(5)]
    Philosophers=[Philosopher(i, forks[i%5], forks[(i+1)%5]) for i in range(5)]
    Philosopher.running=True
    for p in Philosophers:
        p.start()
    time.sleep(20)
    Philosopher.running=False
    print('Now we are finishing.')

if __name__ == '__main__':
    main()
