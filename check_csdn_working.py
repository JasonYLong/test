#!/usr/bin/env python

import requests
import sys

WEB_URL = 'http://www.csdn.net/'

def run():
    try:
        page = requests.get(WEB_URL)
        if page.status_code == 200 and page.content.decode("utf-8").find('<title>CSDN'):
            print("CSDN is working great.")
        else:
            print ("It looks like CSDN is having trouble , some one please take action.")
            sys.exit(-1)
    except:
        print("It looks like CSDN is having trouble , some one please take action.")
        sys.exit(-1)

if __name__ == '__main__':
    run()
