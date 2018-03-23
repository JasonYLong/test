#/usr/bin/env python

import os

def backup_data():
    shell_str= 'find /tmp/test -name "*.gzip" -mtime -1 | xargs -I {} cp {} /tmp/backup'
    os.system(shell_str)
    
def df():
    os.system('df -h')

def run():
    backup_data()
    df()

if __name__ == '__main__':
    run()
