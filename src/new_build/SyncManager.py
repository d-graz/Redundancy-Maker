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


def remove(file):
    subprocess.run(["rm", "-r", file[0]+'/'+file[1]], stdout=subprocess.PIPE, text=True)

def sync(not_synch_files,trg_dir,mrr_dir):
    remove_list = []
    sync_list = []
    for file in not_synch_files:
        if(trg_dir in file[0]):
            sync_list.append(file)
        else:
            remove_list.append(file)
    for file in sync_list:
        copy(file, trg_dir, mrr_dir)
    for file in remove_list:
        remove(file)