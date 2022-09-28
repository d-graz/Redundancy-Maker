from DirectoryWatcher import DirectoryWatcher
from FileLoader import FileLoader
import SyncManager as sync
import threading
import time

print("Loading config file")
flMngr = FileLoader()
print("Config loaded succesfully")
dW = DirectoryWatcher(flMngr.trg_dir)
thread = threading.Thread(target=dW.watch)
thread.start()
print("Redundancy maker is up and runnig")
while True:
    while not dW.isFileTailed():
        #print("DEBUG")
        print("No file was tailed...going to sleep for "+str(flMngr.fs_wt*60)+ " seconds")
        #print("DEBUG-ENDS")
        time.sleep(flMngr.fs_wt*60)
    ## BUGGGG FIX continuos iterations
    if dW.getElapsedTime() > flMngr.fs_wt*60:
        #print("DEBUG")
        print("Coping files")
        #print("DEBUG-ENDS")
        sync.sync(dW.getPendingFiles(), flMngr)
        #print("DEBUG")
        print("Files copied")
        #print("DEBUG-ENDS")
