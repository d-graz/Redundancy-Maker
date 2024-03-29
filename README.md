# Redundancy-Maker
Don't you want to mess up with ZFS?\
Your home-server isn't powerfull enought to virtualize a full Guest-OS like TrueNas?\
Do you need your data to be easily accessible?\
If the answers to one of the previous questions is yes and you want to find a "substitute" to the proprietary ZFS file-system, then maybe this tool is for you.
*Redundacy-Maker* is a **very** simple, flexible and lightweight tool that aims to replicate what is called *disk mirroring* or *RAID-1* on a "standard" filesystem, like *ext4*, so that your data is always accesible.

---

## Warning
You should **always** have an off-site backup of your important data in order to prevent natural disasters or hardware/software failure.\
**I will not take any responsibility for any data-loss caused by malfunction/not appropriate use of the softare**.

---

## Table of content
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Future updates](#future-update)
5. [Changelog](#changelog)

## Introduction
Even though ZFS is one of the most (if not the most) powerfull filesystem to manage large amounts of data, it may rise problem expecially when working on not-that-powerfull hardware. In fact, beside beeing poorly supported by some linux distro (like Arch Linux), it's also a filesystem that introduces great overheads on CPU side and even more on RAM side. This type of situation is not a very plesant one to the average user, which usually runs more than one service on his only, not so updated (HW side), home-server. Besides that, the average user does not need all the pletora of features that comes baked in the ZFS filesystem.\
Here *Redundacy-Maker* comes in, not eating up your ram and stressig up your CPU as much as you state in the config file( See config.Md in `src/` folder ). It only provides *mirroring* feature (this cuold change if requested) leaving your system for other process.

## Installation
*Redundacy-Maker* is meant to work in a configured evirorment as a system deamon.\
If you want you can do these step by yourself. Just check that the requirment are met to ensure that the tool will work properly
### Configuring the envirorment
**Package Requirment :**
- **python** (tested on version 3.10)
- **psutil** (python library)
- **diff** (usually backed in every linux distribution)
- **inotifywait** (inotify-tools package)

**Filesystem Requirments**\
The tool needs **2 directory that lie on 2 different physical drives**. Also these directories must be **automatically mounted at boot**\
To do so we suppose that the `target_directory`, which is the directory were your important file are situated, is in your `/home/$user/...` directory; so it's already mounted ad boot.\
To create the `mirror_directory`, the directory in which files of `target_directory` will be copied to create the mirror, you should:
- create a directory $\rightarrow$ `mkdir /home/$user/.../mirror_directory`\
**Warning : this directory must be empty; any file present in this directory will be removed** when synching whith the `target_directory`
- format your drive if not formatted yet $\rightarrow$ you could use `gparted` (graphical)
- `sudo blkid` $\rightarrow$ grab your disk UUID
- edit `/etc/fstab` accordingly\
Example: `UUID=$previos_UUID  /home/$user/.../mirror_directory   $filesystem_type $some flags`

Now you should be able to mount at boot a drive in your `mirror_directory`.

### Runnig the script
You can now simply
```
python main.py --no-dir
```
after appropriate changes have been made to `config.txt` file.\
Hoever it's recommended to create a systemd daemon to automatically start *Redundancy-Maker* at system boot. To do read `service/README.md` file.  

## Configuration
Please check `src/README.Md` file.

## Future update
Future incoming update:
- params for low load time interval where files can be safely synched
- implementing using cpulimit


Possible features (if heavly requested):
- multiple `target_directory` whith multiple `mirror_directory` 
- install.sh

## Changelog
- 27/11/2022 >> Started testing
- 16/02/2023 >> First release
