
import subprocess
import psutil
import time


def copy(file_name, trg_dir, mrr_dir):
    cloned_dir = file_name[0].replace(trg_dir, "")
    if cloned_dir != "":
        cloned_dir = mrr_dir + cloned_dir
        subprocess.run(["mkdir", "-p", cloned_dir], stdout=subprocess.PIPE, text=True)
    else:
        cloned_dir = mrr_dir
    file = file_name[0]+file_name[1]
    subprocess.run(["cp", "-r", file, cloned_dir], stdout=subprocess.PIPE, text=True)


def sync(not_synch_files, fileManager):
    while psutil.cpu_percent(fileManager.cpu_scan_time*60) > fileManager.cpu_load:
        time.sleep(fileManager.cpu_await_time)
    last_check = time.perf_counter()
    for file in not_synch_files:
        ct = time.perf_counter()
        if ct - last_check > fileManager.cpu_rescan_time:
            while psutil.cpu_percent(fileManager.cpu_scan_time * 6) > fileManager.cpu_load:
                time.sleep(fileManager.cpu_await_time)
            last_check = time.perf_counter()
        copy(file, fileManager.trg_dir, fileManager.mrr_dir)


