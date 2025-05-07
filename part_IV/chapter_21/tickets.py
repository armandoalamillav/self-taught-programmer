import time
import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    # till_show is an int representing the number of seconds until the show starts
    # max_time the longest amount of time (in seconds) it takes for a person to buy a ticket
    def simulate_line(self, till_show, max_time):
        # Create a new empty queue
        pq = Queue()
        # create a new empty list
        tix_sold = []

        for i in range(100):
            # add to the queue 100 people with names "personi"
            pq.enqueue("person", + str(i))
            
            # time function returns a float that represents the number of seconds it has been since
            # epoch (Jan 1, 1970)
            t_end = time.time() + till_show
            now = time.time()
            
            # run while there is time or the queue is empty
            while now < t_end and not pq.is_empty():
                now = time.time()
                r = random.randint(0, max_time)
                # sleep is a built-in function that makes Python "wait" a random number of seconds
                # this simulates each ticket purchase take a random amount of time
                time.sleep(r)
                person = pq.dequeue()
                print(person)
                tix_sold.append(person)
            return tix_sold
        
        queue = Queue()
        sold = queue.simulate_line(5, 1)
        print(sold)
