import subprocess
import time

class DirectoryWatcher:

    def __init__(self,target_directory,mirror_directory):
        self.target = target_directory
        self.mirror = mirror_directory
        self.last_work = 0

    def watch_diff(self):
        raw_cmd_output = subprocess.run(["diff", "-qr", self.target, self.mirror], stdout=subprocess.PIPE, text=True)
        cmd_output = raw_cmd_output.stdout.split("\n")
        cmd_output.pop(len(cmd_output)-1)
        #DEBUG
        if len(cmd_output) == 0:
            print("Nessuna modifica al fs")
        #DEBUG-ENDS
        for i in range(len(cmd_output)):
            cmd_output[i] = cmd_output[i].split(" ")
            cmd_output[i].pop(0)
            cmd_output[i].pop(0)
            if cmd_output[i][0][len(cmd_output[i][0])-1] == ':':
                cmd_output[i][0] = cmd_output[i][0].replace(':', "")
            else:
                string = cmd_output[i][0]
                string = string.rsplit("/",1)
                cmd_output[i] = string
            #DEBUG    
            print("versione modificata delle stringhe :"+str(cmd_output[i]))
            #DEBUG-ENDS
        return cmd_output

    def watch(self):
        while True:
            self.last_work = time.perf_counter()
            subprocess.run(["inotifywait", "-r", "-e", "modify,move,create,delete", "-q", self.target], stdout=subprocess.PIPE, text=True)

    def getElapsedTime(self):
        return time.perf_counter()-self.last_work