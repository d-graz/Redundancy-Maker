# Creating a systemd daemon
The tool is designed to be lauched within the boot of the OS. There are several ways to achive so; one of them is to create a *Systemd service*.\
To do so:
1. At line `6` of `redmaker.service` change directory to point to `main.py` file.
2. Once again on line `6` of `redmaker.service` specify a path to the log file. It's advised to create the logifle inside Redundancy-Maker's directory.\
**Note :** it's **mandatory** to specify a path to the log file even if you disable it in the config file. It has to be notice that the directory to the file must have user permissions (i.e. must be placed somewhere in your home directory)
3. At line `9` replace your user 
4. move `redmaker.service` to `/etc/systemd/system/`
5. `sudo systemctl daemon-reload`
6. `sudo systemctl enable redmaker.service` to run RedMaker at boot
7. `sudo systemctl start redmaker.service` to run *Redundancy-Maker* rigth now (whitouth system reboot)
