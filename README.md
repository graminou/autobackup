# Autobackup
Autobackup is a short Python3 script to backup files in remote HD. It's based on rsync upon ssh

## 1. What's going on ?
I needed to automatebackups file on my remote usb hard drive. 
The script uses your settings to launch rsync on the local files you need to backup, on the target you have chosen.

# Beware : your ssh connexion must use public-key, and not password, which is evil, we all know it ;o).

## 2. Settings
Your personal settings are to be written in settings.py (comments included)

## 3. Running autobackup
No external library is needed, so no virtual environment.
Simply do : 

$ python3 autobackup.py

## 4. Cron task
As backups need to be fully automated, the easiest way to do so is to produce a cron task.
For me : 

$ crontab -e
30 12 * * 1-5 /usr/bin/python3 /path/to/script/autobackup.py

launches the script at 12.30 PM every weekday of every month.
