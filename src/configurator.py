
def conf_loader():
    params = [4]
    config_file = open("config.txt")
    lines = config_file.readlines()
    for line in lines:
        line = line.split(": ")
    for line in lines:
        if line[0] == "target_directory":
            params[0] = line[1]
        else if line[0] == "mirror_directory":
            params[1] = line[1]
        else if line[0] == "cpu_trashold":
            params[2] = line[1]
        else if line[0] == "low_load_period:":
            params[3] = line[1]
    config_file.close()
    return params
