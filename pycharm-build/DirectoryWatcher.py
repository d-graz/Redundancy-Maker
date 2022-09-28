import subprocess
import threading
import time

class DirectoryWatcher:

    def __init__(self, dir):
        self.dir = dir
        self.pending_files = []
        self.lock = threading.Lock()
        self.tmr = time.perf_counter()

    def watch(self):
        while True:
            print("DEBUG")
            print("Watching direcotry for changes")
            print("DEBUG-ENDS")
            cmd_output = subprocess.run(["inotifywait", "-r", "-e", "modify,move,create,delete", "-q", self.dir], stdout=subprocess.PIPE, text=True)
            print("DEBUG")
            print("inotifywait è ritornato con il valore :"+cmd_output.stdout)
            print("DEBUG-ENDS")
            cmd_raw_output = cmd_output.stdout
            cmd_raw_output = cmd_raw_output.split(" ")
            cmd_raw_output.pop(1)
            cmd_raw_output[1] = cmd_raw_output[1].replace('\n', "")
            cmd_output = cmd_raw_output
            self.lock.acquire()
            self.tmr = time.perf_counter()
            if cmd_output not in self.pending_files:
                self.pending_files.append(cmd_output)
            self.lock.release()
            print("DEBUG")
            print("Lista dei file in attesa di essere copiati :")
            for file in self.pending_files:
                print(file)
            print("DEBUG-ENDS")

    def getPendingFiles(self):
        self.lock.acquire()
        files = self.pending_files.copy()
        self.pending_files = []
        self.lock.release()
        return files

    def isFileTailed(self):
        self.lock.acquire()
        if len(self.pending_files) == 0:
            boolean = False
        else:
            boolean = True
        self.lock.release()
        return boolean

    def getElapsedTime(self):
        tmr = time.perf_counter() - self.tmr
        return tmr

    