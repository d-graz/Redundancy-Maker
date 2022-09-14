class FileLoader:

    def __int__(self):
        config_file = open("config.txt")
        lines = config_file.readlines()
        for line in lines:
            line = line.split(": ")
        for line in lines:
            if line[0] == "target_directory":
                self.trg_dir = line[1]
            elif line[0] == "mirror_directory":
                self.mrr_dir = line[1]
            elif line[0] == "cpu_threshold":
                self.cpu = int(line[1])
            elif line[0] == "low_load_period:":
                hours = line[1].split("-")
                self.h1 = int(hours[0])
                self.h1 = int(hours[1])
            else:
                pass # todo handle config file error
        config_file.close()

