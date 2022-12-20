#Thread
from threading import Thread
from time import sleep

def threaded_function(arg):
    for i in range(arg, 0, -1):
        print('Hello from thread %s' % i)
        sleep(1)

if __name__ == '__main__':
    t = Thread(target=threaded_function, args=(10,))
    t.start()
    t.join()
    print('Thread finished...exiting')
