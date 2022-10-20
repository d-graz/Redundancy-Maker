import time

class Logger:

    def __init__(self,logfile_path):
        if logfile_path[len(logfile_path)-1] == '/':
            self.logfile_string = logfile_path+"redMaker_log.txt"
        else:
            self.logfile_string = logfile_path+"/redMaker_log.txt"
        self.log_file = open(self.logfile_string, "w")
        self.header = ""
        self.log("Started up Redundancy-Maker")
        self.enabled = False
        self.log_file.close()

    def log(self,string):
        self.update_header()
        self.log_file = open(self.logfile_string, "a")
        self.log_file.write(self.header+string+"\n")
        self.log_file.close()

    def update_header(self):
        t = time.gmtime()
        self.header = str(t.tm_mday)+"/"+str(t.tm_mon)+"/"+str(t.tm_year)+" "+str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec)+" >> "
