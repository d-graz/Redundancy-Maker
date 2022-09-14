import subprocess


def dir_watcher(directory):
    cmd_output = subprocess.run(["inotifywait","-r" ,"-e", "modify,move,create,delete", "-q", "--format", "%f", directory], stdout = subprocess.PIPE, text = True)
    cmd_raw_output = cmd_output.stdout
    cmd_output=""
    for i in range(len(cmd_raw_output)-1):
        cmd_output = cmd_output + cmd_raw_output[i]
    return cmd_output
