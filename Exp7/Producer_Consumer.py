#Producer consumer problem


import threading
import time
import random

queue=[]
condition=threading.Condition()

def producer():
    global queue
    while True:
        condition.acquire()
        if len(queue)>=10:
            print("Queue is full, producer is waiting")
            condition.wait()
            print("Space in queue, Consumer notified the producer")
        num=random.randint(0,100)
        queue.append(num)
        print("Produced",num)
        condition.notify()
        condition.release()
        time.sleep(random.random())

def consumer():
    global queue
    while True:
        condition.acquire()
        if not queue:
            print("Nothing in queue, consumer is waiting")
            condition.wait()
            print("Producer added something to queue and notified the consumer")
        num=queue.pop(0)
        print("Consumed",num)
        condition.notify()
        condition.release()
        time.sleep(random.random())

producerThread=threading.Thread(target=producer)
consumerThread=threading.Thread(target=consumer)

producerThread.start()
consumerThread.start()


