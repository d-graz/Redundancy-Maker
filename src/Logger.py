import time

class Logger:

    def __init__(self):
        self.log_file = open("rm_log.txt", "w")
        self.header = ""
        self.log("Started up Redundancy-Maker")

    def log(self,string):
        self.update_header()
        self.log_file.write(self.header+string)

    def update_header(self):
        t = time.gmtime()
        self.header = str(t.tm_mday)+"/"+str(t.tm_mon)+"/"+str(t.tm_year)+" "+str(t.tm_hour)+":"+str(t.tm_min)+" >> "