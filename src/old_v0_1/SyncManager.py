
import subprocess
import psutil
import time

def copy(file_name, trg_dir, mrr_dir):
    cloned_dir = file_name[0].replace(trg_dir, "")
    #DEBUG
    print("directory cloned :" + cloned_dir)
    #DEBUG ENDS
    if cloned_dir != "":
        cloned_dir = mrr_dir + cloned_dir
        if file_name[2] == False:
            subprocess.run(["mkdir", "-p", cloned_dir], stdout=subprocess.PIPE, text=True)
    else:
        cloned_dir = mrr_dir
    print("directory cloned final :" + cloned_dir)
    file = file_name[0]+file_name[1]
    print("file :"+file)
    if file_name[2] == True:
        subprocess.run(["rm", "-r", cloned_dir+file_name[1]], stdout=subprocess.PIPE, text=True)
    else:
        subprocess.run(["cp", "-r", file, cloned_dir], stdout=subprocess.PIPE, text=True)
    print("copy succeded")


def sync(not_synch_files, fileManager):
    #DEBUG
    print("Cheching cpu load")
    #DEBUG_ENDS
    while psutil.cpu_percent(fileManager.cpu_scan_time*60) > fileManager.cpu_load:
        pass
    last_check = time.perf_counter()
    #DEBUG
    print("Cpu load is enought low")
    print("start copy procedure")
    #DEBUG_ENDS
    for file in not_synch_files:
        ct = time.perf_counter()
        if ct - last_check > fileManager.cpu_rescan_time:
            while psutil.cpu_percent(fileManager.cpu_scan_time * 6) > fileManager.cpu_load:
                pass
            last_check = time.perf_counter()
        #DEBUG
        print("copyng file :"+ file[1])
        #DEBUG_ENDS
        copy(file, fileManager.trg_dir, fileManager.mrr_dir)


