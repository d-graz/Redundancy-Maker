import time

class Timer:

    def __int__(self, duration):
        self.duration = duration * 60
        self.elapsed = False

    def isFinished(self):
        return self.elapsed

    def start(self):
        self.elapsed = False
        time.sleep(self.duration)
        self.elapsed = True
