import sys

class FileLoader:

    def __init__(self,logger):
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
                last_string_index = len(self.trg_dir) -1
                if(self.trg_dir[last_string_index] == '/'):
                    self.trg_dir = self.trg_dir.replace(self.trg_dir[last_string_index:],"")
                logger.log("Correctly loaded target directory")
            elif line[0] == "mirror_directory":
                self.mrr_dir = line[1].replace("\n",'')
                last_string_index = len(self.mrr_dir) -1
                if(self.mrr_dir[last_string_index] == '/'):
                    self.mrr_dir = self.mrr_dir.replace(self.mrr_dir[last_string_index:],"")
                logger.log("Correctly loaded mirror direcotory")
            elif line[0] == "cpu_load_threshold":
                self.cpu_load = int(line[1])
                logger.log("Correctly loaded cpu load threshold")
            elif line[0] == "cpu_scan_time":
                self.cpu_scan_time = int(line[1])
                logger.log("Correctly loaded cpu scan time")
            elif line[0] == "cpu_rescan_interval":
                self.cpu_rescan_interval = int(line[1])
                logger.log("Correctly loaded cpu rescan time")
            elif line[0] == "low_load_period":
                hours = line[1].split("-")
                self.h0 = int(hours[0])
                self.h1 = int(hours[1])
                logger.log("Correctly loaded low load period interval")
                logger.log("Warning: ignoring h0, h1 params.\nReason : not implemented yet")
            elif line[0] == "filesystem_watch_timeout":
                self.fs_wt = int(line[1])
                logger.log("Correctly loaded filesystem watch timeout")
            elif line[0] == "logger":
                value = line[1].upper()
                if value == "YES" or "TRUE" or "ENABLED":
                    logger.setLoggerActivity(True)
                elif value == "NO" or "FALSE" or "DISABLED":
                    logger.setLoggerActivity(False)
                else:
                    logger.log("Warning: ignoring param "+line[1]+"\nReason : unknown param. Default behavior is logger disabled")
            else:
                logger.log("Warning: ignoring param "+line[0]+"\nReason : unknown param")
                sys.exit()
        if self.trg_dir == "" or self.mrr_dir == "":
            logger.log("Warning: target dir or mirror dir not loaded")
            sys.exit()
        config_file.close()
