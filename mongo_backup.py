#!/usr/bin/env python

import time
from subprocess import call

go_time = time.strftime("%Y-%m-%d_%H")

dir_path = "/data/backup"

def db_backup(user,pwd,host,db):
    
    call("mongodump -u {} -p {} -h {} -d {} --gzip --archive={}/saturn-{}.gz".format(user,pwd,host,db,dir_path,go_time))

if __name__ == '__main__':
    
    db_backup("root","dxhy","10.10.8.12:27017","faster")
