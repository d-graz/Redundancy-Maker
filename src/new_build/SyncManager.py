import subprocess
import psutil
import time

#  def copy(file_name, trg_dir, mrr_dir):
#      cloned_dir = file_name[0].replace(trg_dir, "")
#      #DEBUG
#      print("directory cloned :" + cloned_dir)
#      #DEBUG ENDS
#      if cloned_dir != "":
#          cloned_dir = mrr_dir + cloned_dir
#          if file_name[2] == False:
#              subprocess.run(["mkdir", "-p", cloned_dir], stdout=subprocess.PIPE, text=True)
#      else:
#          cloned_dir = mrr_dir
#      print("directory cloned final :" + cloned_dir)
#      file = file_name[0]+file_name[1]
#      print("file :"+file)
#      if file_name[2] == True:
#          subprocess.run(["rm", "-r", cloned_dir+file_name[1]], stdout=subprocess.PIPE, text=True)
#      else:
#          subprocess.run(["cp", "-r", file, cloned_dir], stdout=subprocess.PIPE, text=True)
#      print("copy succeded")

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
    subprocess.run(["rm", "-r", file[0]+'/'+file[1]], stdout=subprocess.PIPE, text=True)

def sync(not_synch_files,trg_dir,mrr_dir):
    remove_list = []
    sync_list = []
    for file in not_synch_files:
        print("processing file :"+ str(file))
        if(trg_dir in file[0]):
            sync_list.append(file)
            print("file to be synched")
        else:
            remove_list.append(file)
            print("file to be removed")
    for file in sync_list:
        copy(file, trg_dir, mrr_dir)
    for file in remove_list:
        remove(file)