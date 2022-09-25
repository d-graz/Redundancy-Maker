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
        time.sleep(flMngr.fs_wt*60)
    sync.sync(dW.getPendingFiles(), flMngr)
