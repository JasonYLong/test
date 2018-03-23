#/usr/bin/env python

import os

def backup_data():
    shell_str= 'find /tmp -name "*.zip" -mtime -1 | xargs -I {} cp {} /tmp/backup'
    os.system(shell_str)

def run():
    backup_data()

if __name__ == '__main__':
    run()
