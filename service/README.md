# Creating a systemd daemon
The tool is designed to be lauched within the boot of the OS. There are several ways to achive so; one of them is to create a *Systemd service*.\
To do so:
1. move `init.sh` to the dirctory where *Redundancy-Maker* is.\
**Important :** you could place `init.sh` wherever you want, and then change the script like
  ```
  python <path/to/your/RedMaker/direcotry>/main.py
  ```
2. On line `6` of `redmaker.service` change directory to point to `init.sh` file.
3. move `redmaker.service` to `/etc/systemd/system/`
4. `sudo systemctl daemon-reload`
5. `sudo systemctl enable redmaker.service` to run RedMaker at boot
6. `sudo systemctl start redmaker.service` to run *Redundancy-Maker* rigth now (whitouth system reboot)
