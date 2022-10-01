import sys

class FileLoader:

    def __init__(self):
        self.trg_dir = ""            ## target directory -> BUGGGG rimuovere / alla fine della stringa
        self.mrr_dir = ""            ## mirror directory -> BUGGGG rimuovere / alla fine della stringa
        self.cpu_load = 60           ## maximum accepted load on cpu
        self.cpu_scan_time = 10      ## cpu probing time
        self.cpu_rescan_interval = 15    ## time for recheck sistem
        self.fs_wt = 15              ## filesistem watch time
        self.h0 = 0
        self.h1 = 4
        config_file = open("config.txt")
        lines = config_file.readlines()
        processed_lines = []
        for line in lines:
            if line[0] != '#' and line != "":
                processed_line = line.split(": ")
                processed_lines.append(processed_line)
        for line in processed_lines:
            if line[0] == "target_directory":
                self.trg_dir = line[1].replace("\n",'')
                print("Correctly loaded target directory")
            elif line[0] == "mirror_directory":
                self.mrr_dir = line[1].replace("\n",'')
                print("Correctly loaded mirror direcotory")
            elif line[0] == "cpu_load_threshold":
                self.cpu_load = int(line[1])
                print("Correctly loaded cpu load threshold")
            elif line[0] == "cpu_scan_time":
                self.cpu_scan_time = int(line[1])
                print("Correctly loaded cpu scan time")
            elif line[0] == "cpu_rescan_interval":
                self.cpu_rescan_interval = int(line[1])
                print("Correctly loaded cpu rescan time")
            elif line[0] == "low_load_period":
                hours = line[1].split("-")
                self.h0 = int(hours[0])
                self.h1 = int(hours[1])
                print("Correctly loaded low load period interval")
                print("\033[91m {}\033[00m" .format("Warning: ignoring h0, h1 params.\nReason : not implemented yet"))
            elif line[0] == "filesystem_watch_timeout":
                self.fs_wt = int(line[1])
                print("Correctly loaded filesystem watch timeout")
            else:
                print("\033[91m {}\033[00m" .format("Warning: ignoring param "+line[0]+"\nReason : unknown param"))
                sys.exit()
        config_file.close()
