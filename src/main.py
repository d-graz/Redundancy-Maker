from DirectoryWatcher import DirectoryWatcher
from FileLoader import FileLoader
from CpuWatcher import CpuWatcher
from Logger import Logger
import SyncManager as sync
import threading
import time

logger = Logger()
flMngr = FileLoader(logger)
logger.log("Config loaded succesfully")
dW = DirectoryWatcher(flMngr.trg_dir,flMngr.mrr_dir)
cpuW = CpuWatcher(flMngr.cpu_rescan_interval, flMngr.cpu_scan_time)
thread1 = threading.Thread(target=dW.watch)
thread2 = threading.Thread(target=cpuW.watch)
thread1.start()
thread2.start()
while True:
    while dW.getElapsedTime()<(flMngr.fs_wt*60) or cpuW.last_cpu_load>flMngr.cpu_load:
        if logger.isEnabled():
            logger.log("CPU usage is to higth or directory is currently in use. Going to sleep for "+str(flMngr.fs_wt)+"m")
        time.sleep(flMngr.fs_wt*60)
    if logger.isEnabled():
        logger.log("Starting synchronization")
    sync.sync(dW.watch_diff(),flMngr.trg_dir,flMngr.mrr_dir)
    if logger.isEnabled():
        logger.log("Synchronization completed succesfully. Now rest for "+str(flMngr.fs_wt*2)+"m")
    time.sleep(flMngr.fs_wt*60)
