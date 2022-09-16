class FileLoader:

    def __init__(self):
        self.trg_dir = ""
        self.mrr_dir = ""
        self.cpu = 60
        self.cpu_await_time = 10
        self.cpu_scan = 10
        self.cpu_scan_freq = 15
        self.fs_wt = 15
        self.h0 = 0
        self.h1 = 4
        config_file = open("config.txt")
        lines = config_file.readlines()
        processed_lines = []
        for line in lines:
            processed_line = line.split(": ")
            processed_lines.append(processed_line)
        for line in processed_lines:
            if line[0] == "target_directory":
                self.trg_dir = line[1]
            elif line[0] == "mirror_directory":
                self.mrr_dir = line[1]
            elif line[0] == "cpu_threshold":
                self.cpu = int(line[1])
            elif line[0] == "cpu_await_time":
                self.cpu_await_time = int(line[1])
            elif line[0] == "cpu_scan":
                self.cpu_scan = int(line[1])
            elif line[0] == "cpu_scan_frequency":
                self.cpu_scan_freq = int(line[1])
            elif line[0] == "low_load_period":
                hours = line[1].split("-")
                self.h0 = int(hours[0])
                self.h1 = int(hours[1])
            elif line[0] == "fs_watch_timeout":
                self.fs_wt = int(line[1])
            else:
                pass # todo handle config file error
        config_file.close()
