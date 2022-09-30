from DirectoryWatcher import DirectoryWatcher
from FileLoader import FileLoader
from CpuWatcher import CpuWatcher
import SyncManager as sync
import threading
import time

print("Loading config file")
flMngr = FileLoader()
print("Config loaded succesfully")
dW = DirectoryWatcher(flMngr.trg_dir,flMngr.mrr)
cpuW = CpuWatcher(flMngr.cpu_rescan_time, flMngr.cpu_scan_time)
thread1 = threading.Thread(target=dW.watch)
thread2 = threading.Thread(target=cpuW.watch)
thread1.start()
thread2.start()
while True:
    while dW.getElapsedTime()<(flMngr.fs_wt*60) or cpuW.last_cpu_load>flMngr.cpu_load:
        time.sleep(flMngr.fs_wt*60)
    sync.sync(dw.watch_diff())
