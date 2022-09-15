import subprocess
import threading
import time

class DirectoryWatcher:

    def __int__(self, dir):
        self.dir = dir
        self.pending_files = []
        self.lock = threading.Lock()
        self.time =  time.perf_counter()

    def watch(self):
        while True:
            cmd_output = subprocess.run(["inotifywait", "-r", "-e", "modify,move,create,delete", "-q", "--format", "%f", self.dir], stdout=subprocess.PIPE, text=True)
            cmd_raw_output = cmd_output.stdout
            cmd_output = ""
            for i in range(len(cmd_raw_output)-1):
                cmd_output = cmd_output + cmd_raw_output[i]
            self.lock.acquire()
            self.time =  time.perf_counter()
            if cmd_output not in self.pending_files:
                self.pending_files.append(cmd_output)
            self.lock.release()

    def getPendingFiles(self):
        self.lock.acquire()
        files = self.pending_files.copy()
        self.lock.release()
        return files

    def removePendingFiles(self, list):
        self.lock.acquire()
        for element in list:
            self.pending_files.remove(element)
        self.lock.release()

    def getElapsedTime(self):
        time = time.perf_counter() - self.time
        return time

watcher = DirectoryWatcher("/home/davide/git")
thread = threading.Thread(target = watcher.watch())
sleep(5)
print("Time dall'ultima modifica" + watcher.getElapsedTime())
sleep(25)

        

    