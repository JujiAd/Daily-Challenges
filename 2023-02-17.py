# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:05:58 2023

@author: jadle
"""

"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

from time import sleep

def scheduler(f,n):
    if type(n) == int:
        sleep(n)
        f()
    
    
# Provided answer
import threading
from time import sleep

class Scheduler:
    def __init__(self):
        pass

    def delay(self, f, n):
        def sleep_then_call(n):
            sleep(n / 1000)
            f()
        t = threading.Thread(target=sleep_then_call)
        t.start()
        
"""
While this works, there is a huge problem with this method: we spin off a new thread each time we call delay! That means the number of threads we use could easily explode. We can get around this by having only one dedicated thread to call the functions, and storing the functions we need to call in some data structure. In this case, we use a list. We also have to do some sort of polling now to check when to run a function. We can store each function along with a unix epoch timestamp that tells it when it should run by. Then we'll poll some designated tick amount and check the list for any jobs that are due to be run, run them, and then remove them from the list.
"""

from time import sleep
import threading

class Scheduler:
    def __init__(self):
        self.fns = [] # tuple of (fn, time)
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            sleep(0.01)

    def delay(self, f, n):
        self.fns.append((f, time() * 1000 + n))