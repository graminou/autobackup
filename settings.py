#!/usr/bin/python3

# Source directories - adapt for your spcific usage
INCLUDES = (
    '/home/XXX/Bureau',
    '/home/XXX/Documents',
    '/var/backups/',
    '/var/lib/',
    '/var/log/',
    '/var/mail/',
    '/var/opt/',
    '/var/spool/',
    '/var/www/',
    '/etc/',
    '/opt/',
    '/usr/local/'
)

# Remote target directory to store the backups
HD = 'path to remote hd'
TARGET = HD+'your remote end folder/'
HOST = 'IP.of.your.ssh.host'
USER = 'your-ssh-user'

# Write locally log file
LOG_DIRECTORY = 'path-to-your-local-log-folder'
STATS = LOG_DIRECTORY+'stats.txt'
