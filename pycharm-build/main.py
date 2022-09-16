from DirectoryWatcher import DirectoryWatcher
from FileLoader import FileLoader
import SyncManager as sync
import threading
import time

flMngr = FileLoader()
dW = DirectoryWatcher(flMngr.trg_dir)
thread = threading.Thread(target=dW.watch)
thread.start()
while True:
    while not dW.isFileTailed():
        time.sleep(flMngr.fs_wt*60)
    sync.sync(dW.getPendingFiles(), flMngr)
