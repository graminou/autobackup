# Autobackup
Autobackup is a short Python3 script to backup files in remote HD. It's based on rsync upon ssh, and still have been tested only on Debian Jessie (_test on Windows 10 in progress)_

## 1. What's going on ?
I needed to automatebackups file on my remote usb hard drive. 
The script uses your specific settings to launch rsync on the local files you need to backup, and push them _via_ ssh on the target you have chosen.

**_Beware : your ssh connexion must use public-key, and not password, which is evil, we all know it ;o)._**

## 2. settings.py
Your personal settings are to be written in settings.py (comments included)

## 3. autobackup.py
Comments included. Note that rsync is launched to have an incremental backup, with no remove file option. To be changed if other options suit your nedd better.

## 4. Running autobackup
No external library is needed, so no virtual environment.
Simply do : 

```
$ python3 autobackup.py
```

## 5. Cron task
As backups need to be fully automated, the easiest way to do so is to produce a cron task.

```
$ crontab -e
30 12 * * 1-5 /usr/bin/python3 /path/to/script/autobackup.py
```

launches the script at 12.30 PM every weekday of every month.
For me: 

```
$ crontab -e
@reboot /usr/bin/python3 /path/to/script/autobackup.py
```

launches the script each time I open a session on my debian.
