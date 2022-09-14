from threading import Thread
import time

class Timer:
    def __init__(self, duration):
        self.duration = duration*60
        self.lapsed = 0
        self.elapsed = False
        self.thread = Thread(target = Timer.count, args = self)
        
    def isFinished(self):
        return self.elapsed

    def start(self):
        self.thread.start()

    def stop(self):
        self.thread.join()

    def count(self):
        time.sleep(1)
        self.lapsed+=1
        if self.lapsed == self.duration:
            self.elapsed = True
            self.stop()


timer = Timer(1)
timer.start()
time.sleep(0.95)
while not timer.isFinished():
    print("tempo non ancora finito")

