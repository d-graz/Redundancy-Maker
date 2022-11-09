import subprocess
import psutil
import time

def copy(file, trg_dir, mrr_dir):
    working_dir = file[0].replace(trg_dir, "")
    if working_dir != "":
        working_dir = mrr_dir + working_dir
        subprocess.run(["mkdir", "-p", working_dir], stdout=subprocess.PIPE, text=True)
    else:
        working_dir = mrr_dir
    file_name = file[0]+'/'+file[1]
    subprocess.run(["cp", "-r", file_name, working_dir], stdout=subprocess.PIPE, text=True)

def remove(file):
    subprocess.run(["rm", "-rf", file[0]+'/'+file[1]], stdout=subprocess.PIPE, text=True)

def sync(not_synch_files,trg_dir,mrr_dir,exceptions):
    remove_list = []
    sync_list = []
    for file in not_synch_files:
        todo = True
        for direcotory in exception:
            if direcotory in file[0]:
                todo = False
        if trg_dir in file[0] and todo == True:
            sync_list.append(file)
        elif todo == True:
            remove_list.append(file)
    for file in sync_list:
        copy(file, trg_dir, mrr_dir)
    for file in remove_list:
        remove(file)