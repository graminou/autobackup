#!/usr/bin/python3

# USAGE : $ python3 autobackup.py
# SETTINGS : to be adapted for your own usage

import time
import os
import os.path
import subprocess

from mysettings import INCLUDES, LOG_DIRECTORY, USER, HOST, TARGET, STATS, HD
# from settings import INCLUDES, LOG_DIRECTORY, USER, HOST, TARGET, STATS, HD


# if today log_file exists, remove it
log = LOG_DIRECTORY+time.strftime('%y%m%d')+'.txt'
try:
    with open(log):
        os.remove(log)
except:
    pass

# init log_file
log_file = open(log, 'a')
os.chmod(log_file.name, 0o777)
log_file.write('************************************')
log_file.write('\n* Sauvegarde IN NOMINE du '+time.strftime('%d/%m/%y')+' *')
log_file.write('\n************************************')

#  for each floder in INCLUDES
for SRC in INCLUDES:
    # add specific header to log file
    log_file.write('\n')
    log_file.write('\nSauvegarde du dossier '+SRC+' à '+time.strftime('%H:%M:%S'))
    log_file.write('\n==============================================================\n')
    # synchronise with remote hd
    os.system('rsync -azh --stats --log-file='+STATS+' '+SRC+ ' '+USER+'@'+HOST+':'+TARGET)
    # copy stats in log file
    with open(STATS, 'r') as f:
        lines = f.readlines()
        for n, line in enumerate(lines):
            if 'Number of files' in line:
                break
        for l in lines[n:]:
            log_file.write(l)
    # remove stats.txt
    os.remove(STATS)

# when loop ends, add to log file remote hd stats
volume = subprocess.getoutput('ssh '+USER+'@'+HOST+' "df -h '+HD+'"').splitlines()[1].split(' ')
volume = [o for o in volume if o != '']
log_file.write('\n==============================================================')
log_file.write('\n Espace total : '+volume[1])
log_file.write('\n Espace utilisé : '+volume[2]+' ('+volume[4]+')')
log_file.write('\n Espace libre : '+volume[3])

if int(volume[4].replace('%', '')) > 80:
    log_file.write('\n ATTENTION : IL NE RESTE PLUS BEAUCOUP DE PLACE SUR LE STOCKAGE RESEAU !')

# close log file
log_file.close()

# opens log-file at the end (adapt pluma to your own needs)
os.system('pluma '+log_file.name)
